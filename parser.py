#!/usr/bin/python

# для выборки даты
date_words = "СЕНТЯБР"

in_file = []
with open('input.txt') as f:
  in_file = f.readlines()
  
  #in_file = f.read().split(date_words)

# для временного хренения данных покупки  
temp = {}

# чтобы в словарь записывалть список покупок за день 
pokupki = []
 
for index,i in enumerate(in_file): #sorted(in_file, reverse=True):
  #print("===================")
   
  # не выводим пустые строки
  if i == "":
    continue
   
     
  if (date_words in i) or (index == (len(in_file)-1)):
    pokupki = []
    # if len(temp) > 0:
      # print(temp.split("\n"))
    _date = i
    temp.update({_date: pokupki})
    print(_date)
    print("выводим покупки за число {}".format(_date))	
    continue
  pokupki.append(i)    

    
  # обработка массива из покупок
  
  
  
    
  # for pokupka in i.split("Покупка"):
    # # не выводим лишние строки
    # if "Я\n" in pokupka:
      # continue
    
    # pokupka = pokupka.split("\n")
    # #if ""
    # print(pokupka)

  #print("-------------------\n")
for k,v in temp.items():
  print(k)
  print("===========")
  print(v)