
def test02(func):
    # this taks the args from "test01" function and creates a new
    # function called "wrapper()"
    # the lines BELOW the wrapper statement and BEFORE func() will be
    # the new actions added to be executed before the test1 function
    
    def wrapper(*args, **kwargs): 
        print('this was printed from test02-wrapper') # this is the added actions that will be executed before test1 function
        func() # this statement will add the actions from test1 function to the new function "wrapper()" 
        # if any extra actions are needed after test() func is executed
        # it will go here
    
    # this statement will return the new function "wrapper()" to
    # whatever called the test1() function
    # the new function will now be executed by whatever called the
    # test1() function & it will execute all the action BELOW the
    # definition of the "wrapper()" function
    return wrapper 


@test02
# because test1() function is assigned to a decorator, when test1()
# function is called, the "wrapper()" function will be excecuted instead
def test1():
  print('this was printed from test-01 function')


test1()