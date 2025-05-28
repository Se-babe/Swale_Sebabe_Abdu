'''python error handling
errors occur when a program encounters unexpected situation during execution
types of errrors
1.syntax error
2.runtime errors
3.logical errors

Block of codes try,except, else and finally
1.try 
2.except
3.else
4.finally
'''
#example trying to divide 5/0(causes a zero division error)
try:
    result = 5/0
    except ZeroDivisionError:
    print('cannot divide by zero')
     else:
        print('division successful',result)

finally:
print('run completed')

#exercise five
#raise a custom exception that checks for positive number
class NotPositiveNumberError(Exception):
    '''exception raised when a number is not positive'''
    def__init__(self,number);
    super().__init__('number is not positive')

# format 2 of the exercise
try:
    1
    except:
        print(number is positive)
   else:
    print('error has occured')      
    finally:
        print('number was positive')                                                                                                                                                       