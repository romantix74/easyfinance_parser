#!/usr/bin/python

"""
17.09.2019 21.09.2019 - 490.00 ? - 490.00 ?
Платеж
MOYA
DEREVENKA>K
UGESI RU\643\
**9844 0.00 ? 0.00 ?
17.09.2019 21.09.2019 - 25.00 ? - 25.00 ?
Платеж
MOYA
DEREVENKA>K
UGESI RU\643\
**9844 0.00 ? 0.00 ?
18.09.2019 21.09.2019 - 196.94 ? - 196.94 ?
"""

# для выборки даты
date_words = "09.2019" # "ОКТЯБР"

in_file = []
with open('input_mts.txt', encoding="utf-8") as f:
  in_file = f.readlines()
  
  #in_file = f.read().split(date_words)

# сумма в магазинах    
shops = 0

# сумма не определена
other = 0

# сумма всего , для проверки 
all = 0

# вывод покупок раздельно в строку
def print_pkp(_date,_temp_list):
  global shops
  global other
  global all
  for pkp in ''.join(_temp_list).split("Покупка"):
    if pkp != '':
      
      out = ''.join(pkp.split("\n"))  
	  
	  # 25.09.2019 28.09.2019 - 2,460.00 ? - 2,460.00 ?
      rub = _date.split(" ")[-2].replace(",","")
      rub = int(float(rub))
      print(rub)		  
     
      all += rub
      print(all)		  
	
      if ("MAGNIT" in pkp) or ("GASTRONOM" in pkp) or ("PYATEROCHKA" in pkp) or ("ZVENIGOVSKI" in pkp):
        shops += rub
      else:
        other += rub		
      print(out)

# для временного хренения данных покупки  
temp = []

_date = ""


 
for index,i in enumerate(in_file): #sorted(in_file, reverse=True):
     
  # пропускаем пустые строки
  if i == "":
    continue
        
  if (date_words in i):
        
    #update({_date: pokupki})
    # for pkp in temp:
      # print('{0} pokupka {1}'.format(_date, pkp))
    #print("===================")
    #print(temp)
    print_pkp(_date, temp)
    _date = i.split("\n")[0]
    #print("-------------------\n")
    temp = []
    #print(_date)	
    continue
  if (index == (len(in_file)-1)):
    temp.append(i)
    print_pkp(_date, temp)
  temp.append(i)

  
## ВЫВОД СУММ
print("Магазины: {}".format(shops))
print("не определно: {}".format(other))
  
print("Всего Магазины+Не_определено: {}".format(shops+other))
print("Всего: {}".format(shops+other))
    
  # обработка массива из покупок
  
  
  
    
  # for pokupka in i.split("Покупка"):
    # # не выводим лишние строки
    # if "Я\n" in pokupka:
      # continue
    
    # pokupka = pokupka.split("\n")
    # #if ""
    # print(pokupka)

  #print("-------------------\n")
# for k,v in temp.items():
  # print(k)
  # print("===========")
  # print(v)