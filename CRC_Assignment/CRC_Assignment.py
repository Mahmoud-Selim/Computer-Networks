def crc_div(data,generator):
    m = len(generator)                                  #generator length
    frame = data + ("0"*(m-1))                          #frame with appended zeros
    remainder = XOR(frame[:m], generator)               #first XOR
    for i in range (len(data)-1):
        remainder = remainder[1:m] + frame[m + i]       #delete most significant bit and add new bit from frame
        if(remainder[0]=="1"):                          #check for XOR
            remainder = XOR(remainder,generator)
    remainder = remainder[1:m]                          #delete most significant bit
    return remainder




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
