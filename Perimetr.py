game_name = 'Периметр Прямоугольника'
data = {'length': {'question': 'Введите длину: ', 'answer': None},
          'width':{'question': 'Введите ширину: ', 'answer': None}
          }

for itm in data:
    while True:
        temp = input(data[itm]['question'] + '\n')
        if itm == 'length':
            if temp.isdigit():
                temp = int(temp)
            else:
                print('Введите числовое значение!')
                continue
        elif itm == 'width':
            if temp.isdigit():
                temp = int(temp)
            else:
                print('Введите числовое значение!')
                continue
        data[itm]['answer'] = temp
        break
print('Периметр прямоугольниака равен: ', data['length']['answer']*2+data['width']['answer']*2)
print('Его площадь равна: ', data['length']['answer']*data['width']['answer'])