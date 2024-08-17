
# create add() function to return sum of all inputs

def add(*args):
    total = 0
    for n in args:
        total += n
    return total

result = add(12,3,4,5,56,3)
print(result)

def calc(n, **kwargs):
    # print(kwargs)
    # print(kwargs['add'])
    # result = [key for key, value in kwargs.items()]
    # print(result)
    n *= kwargs["multiply"]
    n += kwargs["add"]

    return n

calc(2, add=3, multiply=5) #--> {'add': 3, 'multiply': 5} returns a dict


class Human:
    def __init__(self, **kw):
        # self.ethnicity = kw["ethnicity"] #this way --> its required --> must fill in when init
        # self.gender = kw["gender"]
        self.ethnicity = kw.get("ethnicity") #this way is optional


npc = Human(ethnicity="white",gender="female")
npc.ethnicity
npc.gender

npc2= Human()
print(npc2.ethnicity)

def test(*args):
    print(args)
 
test(1,2,3,5)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
