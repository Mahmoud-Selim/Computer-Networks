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

print("Welcome to CRC Devisor...")
print()
print("Enter \"generator <file | verifier\" to get the result and the veification,")
print("or enter \"generator <file | alter_arg(index) | verifier\" to alter the transmitted message at the given index and get the verfication and the division result...")
print()
user_input = input()
input_tokens = user_input.split('|')
file_name = input_tokens[0][input_tokens[0].find("<") + 1 : ] # get the file name

file_hand = open(file_name.strip()) # remove any spaces
message = ""
generator = ""
line = ""
for line in file_hand:
    line = line.strip()
    if line == "":
        continue;
    elif message == "":
        message = line
    else:
        generator = line
        break

transmitted_message = Transmit (message,generator)                      # The transmitted message
if(user_input.find("alter_arg") > 0):                                    #if the user wants to alter the transmitted message
    print("Warning... The transmitted message is altered")
    index = input_tokens[1][input_tokens[1].find("(") + 1 : input_tokens[1].find(")")]
    transmitted_message = alter(transmitted_message, int(index))

if(verifier(transmitted_message,generator) == True):                    # CRC division at the receiver is 0
    print("The transmitted message", transmitted_message)
    print("The message was transmitted and recieved successfuly...")
else:                                                                   # CRC division at the receiver is not 0
    print("The transmitted message", transmitted_message)
    print("There was an error within the recieved message...")

input("Press any key to exit..")                                        # hold the output for the user to see.      
