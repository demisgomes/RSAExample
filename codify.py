#codify manages operations with simbols and mathematical operations
#codify() may both decrypt and encrypt messages

#to encrypt: C = M**e mod (n)
#to decrypt: M = C**d mod (n)
def codify(message_list, exp_value, n):
    return_list=[]
    for char in message_list:
        char=(char**exp_value)%n
        return_list.append(char)
    return return_list