def verifier (transmitted_message,generator):  #it takes the message and the generator and checks if the reminder is zero or not to check errors in the messagge
    reminder_chk=int(crc_div(transmitted_message,generator),2)
    if(reminder_chk==0):
        return True
    else:
        return False

def alter(message,index):           #it converts the bit in the required index
    message=list(message)
    if message[index-1]=='0':

        message[index-1]='1'
    else:

        message[index-1]='0'
    message=''.join(message)       #convert list to string
    return message
