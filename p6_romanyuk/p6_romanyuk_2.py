index = input("Enter ZIP Code: ")
if len(index) != 3:
    print("Error. ZIP Code hasn't 3 symblos.")
    exit()
elif  not index[0].isalpha() or not index[2].isalpha() or not index[1].isdigit():
    print("Error. Your ZIP Code isn't correct.")
    exit()
province = {
    'Newfoundland':'A',
    'Nova Scotia':'B',
    'Prince Edvard Island':'C',
    'New Brunswick':'E',
    'Quebec':('G','H','J'),
    'Ontario':('K','L','M','N','P'),
    'Manitoba':'R',
    'Saskatchewan':'S',
    'Alberta':'T',
    'British Columbia':'V',
    'Nunavut':'X',
    'Northwest Territories':'X',
    'Yukon':'Y'}
x = ''
for i in province.keys():
    if isinstance(province[i], str):
        if province[i] == index[0].upper():
            x += i + ''
    else:
        if index[0].upper() in province[i]:
            x += i + ''
if x == '':
    print("There is no such ZIP Code in our databasa.")
    exit()
print("The name of the province: " + x)
if index[1] != 0:
    print('city')
else:
    print('village')