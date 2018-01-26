# encoding = utf-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self,length,atlest):
        Exception.__init__(self)
        self.length = length
        self.atleast = atlest

    try:
        text = input("enter something")
        if len(text)<3:
            raise ShortInputException(len(text),3)
    except EOFError:
        print('why did you do an eof on me')
    except ShortInputException as ex:
        print(('ShortInputException:The input was'+
               '{0}long,expected at least {1}').format(ex.length,ex.atleast))
    else:
        print('No exception was raised')

