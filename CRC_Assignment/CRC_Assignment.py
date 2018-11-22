"""
  Function takes two strings of 0's and 1's 
  returns the result of XOR between them
  looping through 2 strings and XORing each element using list comprehension
  and then joining answer into a string
"""
def XOR (str1,str2):
    return "".join([ '0' if i == j else '1' for i,j in zip(str1,str2)])
"""
  Function take message and generator 
  calling CRC function 
  then returns message + remainder 
"""
def Transmit (message,generator):
    remainder = crc_div(message,generator)
    return message + remainder




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
