
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

    if level <= 20:
        return gen_simple_log(newDict)
    elif level > 20:
        return gen_complete_log(newDict)


def gen_simple_log(myDict):
    theLog = ''
    
    # my_values = ['request','result','your_auth','listart','empid','artid','artdes','dptid','famid','grpid','lpreid','tipart','error_type','error_desc']
    my_values = ['username', 'email', 'user', 'request',
                'cantidad', 'caption', 'photo', 'creator',
                'user', 'follows', 'error_type', 'error_desc',
                'post_id']
    
    for key, value in myDict.items():
        for attr_log in my_values:
            if key == attr_log:
                if value != '':
                    
                    # if key == 'listart':
                    #     if value != None:
                    #         theLog = theLog + key + ': ' + str(len(value)) + ' | '                        
                    # elif key == 'error':
                    #     pass
                    #     # for keyErr, valErr in value:
                    #     #     theLog = theLog + keyErr + ': ' + str(valErr) + ' | '                        
                    # elif key == 'your_auth':
                    #     pass
                    # else:
                    theLog = theLog + key + ': ' + str(value) + ' | '
    return theLog


def gen_complete_log(myDict):
    theLog = ''

    my_values = ['request','result','your_auth','listart','empid','artid','artdes','dptid','famid','grpid','lpreid','tipart','error_type','error_desc']

    for key, value in myDict.items():
        for attr_log in my_values:
            if key == attr_log:
                if value != '':
                    if key == 'listart':
                        theLog = theLog + key + ': ' + str(len(value)) + ' | '
                        for article in value:
                            for keyArt, attr in article.items():
                                if keyArt == 'precios':                        
                                    for price in attr:
                                        for keyPrice, valPrice in price.items():
                                            theLog = theLog + keyPrice + ': ' + str(valPrice) + ' | '
                                else:
                                    theLog = theLog + keyArt + ': ' + str(attr) + ' | '
                    elif key == 'error':
                        for keyErr, valErr in value:
                            theLog = theLog + keyErr + ': ' + str(valErr) + ' | '                        
                    elif key == 'your_auth':
                        pass
                    else:
                        theLog = theLog + key + ': ' + str(value) + ' | '
    return theLog
