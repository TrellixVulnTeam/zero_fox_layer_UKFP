
def test02(func):
    # this taks the args from "test11" function and creates a new
    # function called "wrapper()"
    # the lines BELOW the wrapper statement and BEFORE "func()" will
    # be the new actions added to be executed before the test1
    # function


    # "*args & **kwargs" are called unpack operators
    # "*args" will accept any number of positional arguments (args)
    # "**kwargs" will accept any number of key-word args
    # "*args, **kwargs" will accept any number of key-word OR
    # positional args 
    def wrapper(*args, **kwargs): 
        print('this was printed from test02-wrapper') # this is the added actions that will be executed before test1 function
        
        read_in_var1 = kwargs['test1_val1']
        read_in_var2 = kwargs['test1_val2']
        from_wrapper = f'this was read-in from inside the wrapper function: {read_in_var1}\n this was read-in from inside the wrapper function: {read_in_var2}'
        print(from_wrapper)
        # this statement will add the actions from test1 function to the new function "wrapper()"
        # "*args, **kwargs" will hold the value of any args passed-in
        # when the test1() function was called
        # "rv = func(*args, **kwargs)" function test() will be
        # executed and the values is stored in the variable "rv" 
        rv = func(*args, **kwargs) 
        # if any extra actions are needed after test() func is executed
        # it will go here
        

      # after all the actions from test() function & the additional
      # actions are added to the new function "wrapper()" the return
      # value from the execution of the original test() is returned
        return rv
    
    # this statement will return the new function "wrapper()" to
    # whatever called the test1() function
    # the new function will now be executed by whatever called the
    # test1() function & it will execute all the action BELOW the
    # definition of the "wrapper()" function
    return wrapper 


@test02
# because test1() function is assigned to a decorator, when test1()
# function is called, the "wrapper()" function will be excecuted instead
def test1(test1_val1, test1_val2):
  from_test1 = f'the value passed-in to test1() func is: {test1_val1}\n the 2nd value passed to test() func is: {test1_val2}'
  return from_test1

print(test1(test1_val1='boobs', test1_val2='tits'))



