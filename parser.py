#!/usr/bin/python

# master vetka

"""
формат такой примерно
1 ОКТЯБРЯ
Покупка OOO GAMMA-7, карта ********2746
OOO GAMMA-7>Kugesi RU
741,30 ₽
Покупка PYATEROCHKA 4354, карта ********2746
PYATEROCHKA 4354>KUGESI RU
535,98 ₽
"""

# для выборки даты
date_words = "СЕНТЯБР" # "ОКТЯБР"

in_file = []
with open('input.txt', encoding="utf-8") as f:
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
        #print(_date + ';'  +''.join(pkp.split("\n")))
        out = ''.join(pkp.split("\n"))  
        if "RU" in out:
          rub = out.split(" ")[-2].split("RU")[-1].replace(',', '.')
          rub = int(float(rub))
          print(rub)		  
		  # Mir Shkolnika, карта ********2746Mir Shkolnika>P KUGESI RU41 ?
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