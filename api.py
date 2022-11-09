import bah # business analytics helper

# print all methods from class to console

def print_all_methods(class_object):
    for method in dir(class_object):
        if callable(getattr(class_object, method)):
            print(method)

print(print_all_methods(bah))

# baa.StationarityHelper