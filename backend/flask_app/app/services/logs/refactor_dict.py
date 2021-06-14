
def del_null_values(myDict):
    newDict = {}
    for key, value in myDict.items():
        
        if type(value) is dict:

            for key2, value2 in value.items():
                if value2 is not None:
                    newDict[key2] = value2
            
        else:
            if key != 'date_time':
                newDict[key] = value
    return newDict


def gen_log(myDict, level):

    newDict = del_null_values(myDict)

    # if level <= 20:
    return gen_simple_log(newDict)
    # elif level > 20:
        # return gen_complete_log(newDict)


def gen_simple_log(myDict):
    theLog = ''
    
    # my_values = ['request','result','your_auth','listart','empid','artid','artdes','dptid','famid','grpid','lpreid','tipart','error_type','error_desc']
    my_values = ['username', 'email', 'user', 'request',
                'cantidad', 'caption', 
                'user', 'follows', 'error_type', 'error_desc',
                'post_id']
    _logged_in = ''
    
    for key, value in myDict.items():
        for attr_log in my_values:
            if key == attr_log:
                if value != '':
                    if key == 'username':
                        _logged_in = value

                    elif key == 'access_token':
                        if len(value) > 64:
                            theLog = theLog + 'logged in ' + str(_logged_in) + ' | '
                        else:
                            theLog = theLog + 'No se ha conectado | '

                    theLog = theLog + key + ': ' + str(value) + ' | '
    return theLog


def gen_complete_log(myDict):
    theLog = ''

    my_values = ['username', 'email', 'user', 'request',
                'cantidad', 'caption', 
                'user', 'follows', 'error_type', 'error_desc',
                'post_id']

    for key, value in myDict.items():
        for attr_log in my_values:
            if key == attr_log:
                if value != '':
                    theLog = theLog + key + ': ' + str(value) + ' | '
    return theLog
