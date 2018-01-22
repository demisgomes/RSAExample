def convert_to_asc(string):
    asc_numbers=[]
    chars=list(string)
    for char in chars:
        asc_numbers.append(ord(char))
    return asc_numbers

def convert_to_string(asc_list):
    string_list=[]
    for asc in asc_list:
        string_list.append(chr(asc))
    return "".join(string_list)