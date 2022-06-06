arr = ['a','b','c','d','e','f','g']
print(arr)

def m1(*argsList):
    for argx in argsList:
        print(argx)


def m2(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

m1("sunday","Monday","tuesday", 'thursday')
m2(City = "Hyderabd", pin = 533232, Mobile = "2532532530")