'''
DNS Class Loader
Resouce record types sit in ./RecordTypeClasses

Author: junzhengrice@gmail.com
'''
classRoot = 'RecordTypeClasses'

def LoadClass(className):
    classPath = classRoot+'.'+className
    try:
        mod = __import__(classPath)
        mod = getattr(mod,className)
    except:
        raise ImportError
    return mod