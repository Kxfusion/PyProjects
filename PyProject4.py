from twilio.rest import Client

id = input("give Twilio id - ")
token = input("give Twilio token - ")
twi_num = input("give Twilio number - ")
rec_num = input("give Recipient number - ")
mssge = input("give message - ")
client = Client(id, token)

message = client.messages.create(body = mssge,
                                     to = rec_num,
                                     from_= twi_num)
print (message.sid)

                          
