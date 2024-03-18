print('Basic calculator by Yusuf, using pure Python.'
      '')
print('''Type 1 for add,
2 for substract,
3 for multiply
and 4 for divide under "Select oparation input". 
''')
first_number = input('First Number: ')
second_number = input('Second Number: ')
oparation = input('Select oparation: ')
if oparation == '1':
    print(int(first_number), '+', int(second_number), '= ', int(first_number) + int(second_number))

elif oparation == '2':
        print(int(first_number), '-', int(second_number), '= ', int(first_number) - int(second_number))

elif oparation == '3':
        print(int(first_number), '*', int(second_number), '= ', int(first_number) * int(second_number))

elif oparation == '4':
        print(int(first_number), '/', int(second_number), '= ', int(first_number) / int(second_number))







