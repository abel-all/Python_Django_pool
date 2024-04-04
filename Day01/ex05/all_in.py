import sys

def print_msg(city, state):
    print(city, 'is the capital of', state)

def search_for_key(keyword):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    try:
        print_msg(capital_cities[states[keyword]], keyword)
    except:
        for key, value in capital_cities.items():
            if value == keyword:
                for key_, value_ in states.items():
                    if value_ == key:
                        print_msg(value , key_)
                        return
        print(keyword, 'is neither a capital city nor a state')

def parse_and_execute():
    args_size = len(sys.argv[1:])
    if args_size != 1:
        sys.exit(1)

    list_of_arg = sys.argv[1].split(',')

    list_of_arg = [x.strip(' ').title() for x in list_of_arg]

    for i in list_of_arg:
        if i == '': continue
        search_for_key(i)

if __name__ == "__main__":
    parse_and_execute()
