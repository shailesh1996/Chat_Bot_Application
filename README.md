# Chat_Bot_Application



OVERVIEW -: ...This is the P2P ChatBot Application by using pyramid (python Web Frame Work)and Mysql Database. it has following functionality

    i can chat to any number of user's but one at a time
    i can store my chat info with any user in database for further memory and in order to store chat info, i have used Mysql.

DESCRIPTION -: so initially in the home page i can type the user name, to whom i want to chat. Then i can send messages to the selected user through Post request method.and that message will render on the listening port of the selected user. And from their he can reply to my chat and send a post request. And his text will render on my home page.

CONCLUSION-: So it has basically two end point (me and the selected user).

END POINTS
http://localhost:6543/

[home_page]: Get Parameter's-:

Post Parameter's-: user_id,user_name Displays the Home page
http://localhost:6543/show/history
(show_history]

Get Parameter's-: user_id, user_name

Post Parameter's-: msg it lists the past history
http://localhost:6543/send/node
[me_sending_msg_to_The_Connected_user]

get parameter's-: user_id

post Parameter's-: msg ---In it just type the msg to be send to the selected user
http://localhost:6543/rcv/send
[Reciever_Node_listen_and_reply]

get parameter's-: msg

post parameter's-: msg

---here connected user can see the msg send by me and also reply back
http://localhost:6543/send/reply
[page_render_after_me_send_msg_to_the_user]

get parameter's-: msg_typed_by_me

post parameter's-: msg

---here i can type the message to be sent and also it render the message typed by me, in this page and also in the reciver side.
