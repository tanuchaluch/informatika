

import json
a='input.json'
def a2(a):
    with open('input.json', 'r') as f:
        data = json.load(f) # Загружаем данные из JSON в переменную data
    k=sum((i['score']*i['weight']) for i in data)  # Считаем сумму произведений для каждого элемента
    return round(k,3) #округляем
l=a2(a)
print(l)


