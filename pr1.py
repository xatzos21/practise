# greetings = {
#     "key": "value",
#     "table": "a place to put your food on",
#     "car": "a machine to help a human move from one place to another"
# }

# def full_name(*args,**kwargs):
#     print("--kwargs: ->",kwargs)
#     print("--args: ->", args)
#     first_name = kwargs["first_name"]
#     last_name = kwargs["last_name"]
#     return f"{args[0]}{first_name} {last_name}"

# print(full_name("good morning",first_name= "Jane", last_name ="Doe", location="Berlin")) # how to use it

# #print(full_name=input("What is u name")),

last_name = {"surname": "Doe"}
# "Pass by reference" variables can change
def full_name(last_name):
    # variations 
    last_name ["surname"] = "Eod"
    return last_name

full_name(last_name)
print(last_name)