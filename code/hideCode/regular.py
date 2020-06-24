import re

def isPixiv(s: str):
    if(bool(re.match("^[0-9]{8}$", s))):
        return True
    return False

def isnhentai(s: str):
    if(bool(re.match("^[0-9]{6}$", s))):
        return True
    return False

def isDigital(s: str):
    if(bool(re.match("^[0-9]*$", s))):
        return True
    return False



#if(isDigital('5341')):
#    print('ok')

