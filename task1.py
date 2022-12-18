import re
str = input('Введите слова через запятую - ')
strLen = int(input('Введите максимальное число символов - '))

str1 = re.sub("[^А-Яа-я0-9| |,]", "", str)
strList = str1.split(', ')

monthD = {'Январь':1, 'Февраль':2, 'Март':3, 'Апрель':4, 'Май':5, 'Июнь':6, 'Июль':7, 'Август':8, 'Сентябрь':9, 'Октябрь':10, 'Ноябрь':11, 'Декабрь':12}

for mes in monthD.keys():
  for i in range(len(strList)):
    strList[i] = strList[i].capitalize()
    if mes == strList[i]:
      strList[i] = f'{strList[i]}({monthD.get(mes)})'
      
strList[:] = [x for x in strList if len(x) <= strLen]
strList.sort()
str3 = ", ".join(strList)    
print(str3)
