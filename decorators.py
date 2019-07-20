# def hello(name='SK'):
    
#     def greet():
#         return '\t This is inside the greet() function'
    
#     def welcome():
#         return "\t This is inside the welcome() function"
    
#     if name == 'SK':
#         return greet()
#     else:
#         return welcome()

# print(hello())



def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()