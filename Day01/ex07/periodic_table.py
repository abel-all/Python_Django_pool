import sys

def parse_and_genarate_html(line):
    list_by_equal = line.split(' = ')
    line1 = f'\t\t  <h4>{list_by_equal[0]}</h4>\n\t\t\t<ul>\n'
    list_by_coma = list_by_equal[1].split(', ')
    i = 1
    list_len = len(list_by_coma)
    while i < list_len - 1:
        list = list_by_coma[i].split(':')
        if i == 1: line1 += f'\t\t\t  <li>No {list[1]}</li>\n'
        elif i == 2: line1 += f'\t\t\t  <li>{list[1].strip()}</li>\n'
        else: line1 += f'\t\t\t  <li>{list[1]}</li>\n'
        i += 1
    line1 += '\t\t\t<ul>\n'
    return line1

if __name__ == '__main__':
    list = '<!DOCTYPE html>\n<html>\n  <head>\n\t<mata charset="UTF-8">\n  </head>\n  <body>\n\t<table>\n\t  <tr>\n'
    with open("periodic_table.txt", 'r') as file:
        for line in file:
            list += '\t\t<td style="border: 1px solid black; padding:10px">\n'
            list += parse_and_genarate_html(line.strip())
            list += '\t\t  </td>\n'
    list += '\t  </tr>\n\t</table>\n  <body>\n</html>'
    with open("periodic_table.html", "w") as file1:
        file1.write(list)
