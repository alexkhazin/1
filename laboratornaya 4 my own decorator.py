def my_decorator (func):
    def wrapper ():
        return wrapper

def new_function():
    return 'this is something'
print(new_function())
    
def decorator_one(funcone):
    def wrapper_one (*args,**kwargs):
        funcone(*args,*kwargs)
    return wrapper_one

@decorator_one
def printlogpass(login,password):
        print('Enter log , pass', login , password)
    printlogpass ('user','12345')
