#!/usr/bin/python

import re

"""
from payment MTS 

  FRUKTY I OVOSHHI > Kugesi RU	
−131 руб.
31.10.2019  в 09:55
В обработке
   TATNEFT AZS 469 > RESP. TATARST RU\643\	
−299,71 руб.
30.10.2019  в 13:26
Успешно


"""

# для выборки даты
date_words = "10.2019" # "ОКТЯБР"

in_file = []
with open('input_mts_2.txt', encoding="utf-8") as f:
  in_file = f.readlines()
  
  #in_file = f.read().split(date_words)

# сумма в магазинах    
shops = 0

# сумма не определена
other = 0

# сумма всего , для проверки 
all = 0

# вывод покупок раздельно в строку
def count_pkp(_date,_temp_list):
  global shops
  global other
  global all
  for pkp in ''.join(_temp_list).split("Покупка"):
    if pkp != '':
      
      out = ''.join(pkp.split("\n"))  
	  
	  # ['   FRUKTY I OVOSHHI > Kugesi RU\t\n', '?131 руб.\n']
      rub = _temp_list[-1].replace(" руб.\n","").replace(" ","").replace(",",".")
      rub = re.sub('[\?]', '', rub)
      
	  #rub = int(float(rub))
      print(rub)		  
     
      #all += rub
      print(all)		  
	
      # if ("magnit" in pkp) or ("gastronom" in pkp) or ("pyaterochka" in pkp) or ("zvenigovski" in pkp):
        # shops += rub
      # else:
        # other += rub		
      # print(out)

# для временного хренения данных покупки  
temp = []

_date = ""


 
for index,i in enumerate(in_file): #sorted(in_file, reverse=True):
     
  # пропускаем пустые строки
  if i == "":
    continue
        
  if (date_words in i):
     
    print(i)	 
    #update({_date: pokupki})
    # for pkp in temp:
      # print('{0} pokupka {1}'.format(_date, pkp))
    #print("===================")
    print(temp)
    _date = i.split("\n")[0]
    #print(_date)
    count_pkp(_date, temp)
    
    #print("-------------------\n")
    temp = []
    #print(_date)	
    continue
  if (index == (len(in_file)-1)):
    temp.append(i)
    count_pkp(_date, temp)
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