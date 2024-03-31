file = open("numbers.txt", "r")
list = file.readline().split(',')
list[len(list) - 1] = list[len(list) - 1].strip()
for i in list:
    print(i)
