import pandas as pd
import requests
import bs4
import csv
import sys
import os
import time

response = requests.get('https://volby.cz/')
print(response.status_code)

HEADER = ['kód obce', 'název obce', 'voliči v seznamu', 'vydané obálky', 'platné hlasy',
          'ODS', 'Řád národa', 'Cesta OS', 'ČSSD', 'Pravý blok', 'Radostné Česko',
          'STAN', 'KSČM', 'Strana zelených', 'ROZUMNÍ', 'Spol.Prokop.údolí', 'SSO',
          'Blok proti islámu', 'ODA', 'Piráti', 'Občané 2011', 'Unie H.A.V.E.L', 'ČNF',
          'Referendum o EU', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 'SPR-RSČ', 'KDU-ČSL',
          'ČSSS', 'REALISTÉ', 'SPORTOVCI', 'DSSS', 'SPD', 'SPO', 'Národ sobě']


def main():

    main_tuple = get_links(FIRST_PATH)
    list_of_lists = get_list_of_values(main_tuple)
    election_file(FILE, HEADER, list_of_lists)


def election_file(e_file: str, e_header: list, e_list_of_lists: list) -> csv:
    with open(e_file, 'w') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(e_header)
        f_writer.writerows(e_list_of_lists)


def get_list_of_values(v_tuple: tuple) -> list:
    list_of_values = list()
    for i in range(len(v_tuple[0])):
        path = v_tuple[1][i]
        x1 = v_tuple[0][i]
        d = get_numbers(x1, path)
        list_of_values.append(d)
    return list_of_values


def get_links(l_path: str) -> tuple:
    list_links = list()
    list_numbers = list()
    c1 = list()
    getr = requests.get(l_path)
    soup = bs4.BeautifulSoup(getr.text, 'html.parser')
    c = (soup.find_all('a')[5:-2:2])
    for item in c:
        c1.append(str(item).replace('amp;', ''))
    for i in range(len(c1)):
        x1 = format(c1[i].split('"')[1].split('=')[3].split('&')[0])
        list_numbers.append(int(x1))
        path = os.path.join('https://www.volby.cz/pls/ps2017nss/', format(c1[i]).split('"')[1])
        list_links.append(path)
    return list_numbers, list_links


def get_numbers(x1: int, path: str) -> list:
    seznam = list()

    getr = requests.get(path)
    soup = bs4.BeautifulSoup(getr.text, 'html.parser')
    c = soup.find_all('h3')
    x2 = [(str(c[2]).split()[2])]

    x = dict(pd.read_html(path, encoding='UTF-8')[0])
    x3 = list(x[('Voličiv seznamu', 'Voličiv seznamu')].values)
    x4 = list(x[('Vydanéobálky', 'Vydanéobálky')].values)
    x5 = list(x[('Platnéhlasy', 'Platnéhlasy')].values)
    seznam.extend(x3)
    seznam.extend(x4)
    seznam.extend(x5)

    x = dict(pd.read_html(path, encoding='UTF-8')[1])
    x6 = list(x[('Platné hlasy', 'celkem')].values)
    x6a = list(x[('Strana', 'číslo')].values)
    x6b = list()
    while x6:
        for i in range(1, 16):
            if i in x6a:
                y = x6.pop(0)
                x6b.append(y)
            else:
                x6b.append('0')
    seznam.extend(x6b)

    x = dict(pd.read_html(path, encoding='UTF-8')[2])
    x7 = list(x[('Platné hlasy', 'celkem')].values)
    x7a = list(x[('Strana', 'číslo')].values)
    x7b = list()
    x7c = list()
    if x7[-1] == '-':
        del x7[-1]
    if x7a[-1] == '-':
        del x7a[-1]
    for item in x7a:
        item = int(item)
        x7c.append(item)
    while x7:
        for i in range(16, 32):
            if i in x7c:
                y = x7.pop(0)
                x7b.append(y)
            else:
                x7b.append('0')
    seznam.extend(x7b)
    new_seznam = list()
    for item in seznam:
        item = str(item)
        new_seznam.append(item)
    result = x2 + num_conversion(new_seznam)
    result.insert(0, x1)
    return result


def num_conversion(my_list: list) -> list:
    new_list = list()
    for num in my_list:
        try:
            new_list = [int(num) for num in my_list]
        except ValueError:
            num1 = ''
            for char in num:
                if char.isdigit():
                    num1 += str(char)
                    num = num[1:]
                if char == '\\':
                    num = num[4:]
            new_list.append(int(num1))
    return new_list


if __name__ == '__main__':
    FIRST_PATH = sys.argv[1]  # have to enclose it in double quotes!!!
    FILE = sys.argv[2]
    start = time.time()
    main()
    end = time.time()
    print('it took: ', end - start)

print()
