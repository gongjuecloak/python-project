from Chat import send_message
import datetime

def time_send(h,m,s,msg,qq):
    now=datetime.datetime.now()
    if(now.hour==h and now.minute==m and now.second==s):
        send_message(msg,qq,"group")