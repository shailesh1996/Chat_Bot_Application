
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
        self.view_name = 'P2P_Chat'
        #self.url="abc"
        #print "qqqqq"

    # @property
    # def full_name(self):
    #     first = self.request.matchdict['first']
    #     last = self.request.matchdict['last']
    #     return first + ' ' + last

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        #print("home")
        global sql
        global db
        db = MySQLdb.connect("localhost","root","balaksingh","chatBot" )
        global cursor 
        cursor= db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS chatbot1 (var_id  varchar(255) ,user  varchar(255),msg varchar(255) )"
        cursor.execute(sql)
        return {'view_name':'Chat Bot'}

    @view_config(route_name='chat',renderer='chat.pt')
    def chat(self):
        #print("chat")
        var_id= self.request.params['var_id']
        user = self.request.params['user']
        msg = self.request.params['msg']
        print("You Typed-:")
        print(msg)
        global idd
        idd=var_id
        global userr
        userr=user
        sql="INSERT INTO chatbot1 (var_id,user,msg) VALUES ("+"\""+str(var_id)+"\""+","+"\""+str(user)+"\""+","+"\""+str(msg)+"\""+")"
        #print(sql)
        #print(var_id,user,msg)
        cursor.execute(sql)
        db.commit()
        return {'user':user,'var_id':var_id,'view_name':'Chat Bot'}

    @view_config(route_name='type',renderer='type.pt',request_method='POST')
    def type(self):
        #print("type",userr," lol")
        msg = self.request.params['msg']
        print("You Typed -:")
        print(msg)
        sql="INSERT INTO chatbot1 (var_id,user,msg) VALUES ("+"\""+str(idd)+"\""+","+"\""+str(userr)+"\""+","+"\""+str(msg)+"\""+")"
        cursor.execute(sql)
        db.commit()
        port=6543
        url="http://localhost:"+str(port)+'/obtain'
        payload={'msg' : msg,'idd' : idd ,'userr': userr}
        #print(url,msg)
        #print url1,"final value"
        #print "here"
        resp = requests.post(url,data=json.dumps(payload))
        #print(resp.text), ">>>"
        print("msg sent -: ")

        return {'view_name':'Chat Bot','userr':userr}

    @view_config(route_name='show',renderer='show.pt')
    def show(self):
        idd= self.request.params['var_id']
        sql="select user,msg from chatbot1 where var_id="+str(idd)
        cursor.execute(sql)
        result=cursor.fetchall()
        string=""
        var_name=""
        for each_column_attribute in result:
            var_msg=each_column_attribute[1]
            var_name=each_column_attribute[0]
            string +=var_msg
            string+=", "

        #print(string)
        return {'view_name':'Chat Bot','var_name':var_name,'string':string}

var_bool=0

@view_config(route_name='go',renderer='type1.pt',request_method='POST')
def go(request):
    print("Recieved Message-:")
    req=request.json_body
    #global req1
    #req1=req
    msg=req.get('msg')
    user=req.get('userr')
    id1=req.get('idd')
    

    #print(req.content)
    print(msg)
    #print(msg,"lol",user,id1)
    return {'userr':userr,'view_name' : 'P2P_Chat','msg':msg}


# @view_config(route_name='go',renderer='type1.pt',request_method='GET')
# def go1(request):
#     msg=req1.get('msg')
#     print(msg,"lol")
#     return {'userr':userr,'view_name' : 'P2P_Chat','msg':msg}

# @view_config(route_name='go',renderer='type2.pt',request_method='GET')
# def go1(request):
#     msg=req1.get('msg')
#     #print(req.content)
#     print(msg,"lol")
#     return {'userr':userr,'view_name' : 'P2P_Chat','msg':msg}

