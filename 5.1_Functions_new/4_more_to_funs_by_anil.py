# Rule 2: data type should be assignable to a variable
a = "anil"


def some_function(arg):
    print(arg)
    return arg


# Rule 2: data type should be passable into a function
# Rule 3: data type should be returnable from a function
# result = some_function(a)
# print(result)


def rule_functions(arg1):
    print("called")
    arg1()

    # return 1
    def inner_function():
        print("inner")
        return 2

    return inner_function


def passable_function():
    print("passable")


# Rule 1
# result = rule_functions
# result()

# result = rule_functions(passable_function)
# result()


def my_time_decorator(func):
    print("my decorator called")

    def inner_function(*args, **kwargs):
        # record
        func(*args, **kwargs)
        # record time

    return inner_function
    # return 1


@my_time_decorator  # result = my_decorator(decorated_function) --> result()
def ms_data_fetch_function(arg1, arg2):
    print("decorated function called")


@my_time_decorator
def ml_algorithm(arg3):
    print("ml")


ms_data_fetch_function("a", "b")
ml_algorithm("g")

# read_ccsv

# # @remove_emty
# @removee_nulls
# @store_db
# cleanr_csv