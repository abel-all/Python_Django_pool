def read_nbrs_and_print_it():
    file = open("numbers.txt", "r")
    list = file.readline().split(',')
    list_size = len(list)
    list[list_size - 1] = list[list_size - 1].strip()
    for i in list:
        print(i)

if __name__ == '__main__':
    read_nbrs_and_print_it()
