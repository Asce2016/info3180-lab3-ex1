import smtplib 
from_addr = 'asce2016@gmail.com' 
to_addr  = 'alfansobarr@yahoo.com'

from_name = 'alfano'
to_name ='kemo'
subject = 'never say die'
msg = 'never give up, never give in'

message = """From: {} <{}> 
To: {} <{}> 
Subject: {} 
{} 
""" 
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 









# Credentials (if needed) 
username = 'asce2016@gmail.com' 
password = 'tvevpfspboqqyffb' 


# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, 
password) 
server.sendmail(from_addr, to_addr, message_to_send) 
print( 'message sent')
server.quit() 