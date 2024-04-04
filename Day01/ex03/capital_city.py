import sys

def serch_for_state(arg):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    try:
        s = states[arg]
        return s
    except:
        print ('Unknown state')
        quit()

def serch_for_capital_cities(state):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    c = capital_cities[state]
    return c

def parse_and_execute():
    size_of_args = len(sys.argv[1:])
    if size_of_args != 1:
        quit()
    print(serch_for_capital_cities(serch_for_state(sys.argv[1])))

if __name__ == "__main__":
    parse_and_execute()
