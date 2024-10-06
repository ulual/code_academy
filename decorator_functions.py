# Decorators with Parameters

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        print_name_function(*args, **kwargs)
    return wrapper
@title_decorator # This line has to stay above the function below.
def print_my_name(name, age):
    print(name + " you are " + str(age))

print_my_name("Shelby", 50)