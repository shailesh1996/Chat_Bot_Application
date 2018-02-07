
from pyramid.view import (
    view_config,
    view_defaults
    )
import requests
import json
import MySQLdb


@view_defaults(route_name='hello')
class TutorialViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'Two_Point_ChatBot'
        #self.url="abc"
        #print "qqqqq"
    # @property
    # def full_name(self):
    #     first = self.request.matchdict['first']
    #     last = self.request.matchdict['last']
    #     return first + ' ' + last

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        print("home")
        global db
        db = MySQLdb.connect("localhost","root","balaksingh","chatBot" )
        global cursor 
        cursor= db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS chatbot1 (var_id  varchar(255) ,user  varchar(255),msg varchar(255) )"
        cursor.execute(sql)
        return {'view_name':'Chat Bot'}

    @view_config(route_name='send_node',renderer='chat.pt')
    def send_node(self):
        print("chat")
        var_id= self.request.params['var_id']
        user = self.request.params['user']
        global glob_user
        global glob_var_id
        glob_var_id=var_id
        glob_user=user
        return {'user':user,'var1_id':glob_var_id,'view_name':'Chat Bot'}

    @view_config(route_name='send_reply',renderer='type.pt',request_method='POST')
    def send_reply(self):
        # print("type",glob_user," lol")
        #print self.request
        # print self.request.json_body
        # print("shaily")
        # print self.request.params
        x=self.request.params
        str1=str(x)
        print("final....",x)
        str2=str1[27:]
        msg=""
        for i in str2:
            if i =='\'':
                break
            if i ==',':
                break
            msg=msg+i
        for i in msg:
            if i=="\"":
                msg=msg[1:-1]
                break
            else:
                break
            
        
        cnt=0
        print(msg , "HJJK")
        print(msg)
        #msg= self.request.params['msg']
        # print type(x),"aaaa"
        # print x[0],"bbb"
        # print x[1],"cccc"
        # print type(x[1])
        #print (x[0])
        #reqq=self.request.json_body
        
        #print("You Typed -:")
        #print(msg)
        sql="INSERT INTO chatbot1 (var_id,user,msg) VALUES ("+"\""+str(glob_var_id)+"\""+","+"\""+str(glob_user)+"\""+","+"\""+msg+"\""+")"
        #print("do ",sql)
        cursor.execute(sql)
        db.commit()
        port=6543
        url="http://localhost:"+str(port)+'/rcv/send'
        payload={'msg' : msg,'user_id' : glob_var_id ,'user_name': glob_user,'var_bool':0}
        #print(url,msg)
        #print url1,"final value"
        #print "here"
        request1 = requests.post(url,data=json.dumps(payload))
        #print(resp.text), ">>>"
        msg1=msg
        print(msg1," jj")
        print("msg sent -: ")
        return {'view_name':'Chat Bot','user':glob_user,'message':msg1}

    @view_config(route_name='show_history',renderer='show.pt')
    def show_history(self):
        glob_var_id= self.request.params['var_id']
        sql="select user,msg from chatbot1 where var_id="+str(glob_var_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        string=""
        var_name=""
        for each_column_attribute in result:
            user_msg=each_column_attribute[1]
            user_name=each_column_attribute[0]
            string +=user_msg
            string+=", "

        #print(string)
        return {'view_name':'Chat Bot','user_name':user_name,'string':string}

    # @view_config(route_name='type2',renderer='type2.pt')
    # def type2(self):
    #     print("Recieved Message-:")
    #     msg_recieved=self.request.params['reply']
    #  
    #   return {'userr':userr,'view_name' : 'P2P_Chat',"msg_recieved":msg_recieved}

@view_config(route_name='rcv_send',renderer='type1.pt',request_method='POST')
def rcv_send(request):
    print("Recieved Message-:")
    global req1
    req1=request.json_body
    user=req1.get('user_name')
    #print(req.content)
    msg=req1.get('msg')
    #print(msg,"lol",user,id1)
    return {'userr':user,'view_name' : 'P2P_Chat','msg':msg}


@view_config(route_name='rcv_send',renderer='type1.pt',request_method='GET')
def rcv_sendx(request):
    msg=req1.get('msg')
    print(msg,"lol")
    return {'userr':glob_user,'view_name' : 'P2P_Chat','msg':msg}


@view_config(route_name='send_reply',renderer='type.pt',request_method='POST',request_param='form.reply')
def reply_back(request):
    print("hello")
    msg=request.params['msg']
    global glob_var_id
    global var_id
    #print("lolllll ",msg)
    port=6543
    url="http://localhost:"+str(port)+'/send/reply'
    payload={'msg' : msg,'glob_var_id' : glob_var_id ,'user': glob_user,'var_bool':1}
    print json.dumps(payload),"qwerty"
    request2=requests.post(url,data=json.dumps(payload))
    #print("zero")

    return {'view_name':'Chat Bot','user':glob_user,'message':msg}



# @view_config(route_name='go',renderer='type2.pt',request_method='GET')
# def go1(request):
#     msg=req1.get('msg')
#     #print(req.content)
#     print(msg,"lol")
#     return {'userr':userr,'view_name' : 'P2P_Chat','msg':msg}

