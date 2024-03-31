import sys

def serch_by_value(arg):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    for key, value in states.items():
        if value == arg:
            print (key)
            quit()

def serch_for_city(arg):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    for key, value in capital_cities.items():
        if value == arg:
            return key
    return 'none'

args_size = len(sys.argv[1:])
if args_size != 1:
    quit()
s = serch_for_city(sys.argv[1])
if s != 'none':
    serch_by_value(s)
print ('Uknown arg')
