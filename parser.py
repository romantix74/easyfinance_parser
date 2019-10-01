#!/usr/bin/python


# для выборки даты
date_words = "СЕНТЯБР"

in_file = []
with open('input.txt') as f:
 # in_file = f.readlines()
  in_file = f.read().split(date_words)

 

  
for i in in_file:
  #print("===================")
  for pokupka in i.split("Покупка"):
    # не выводим лишние строки
    if "Я\n" in pokupka:
      continue
    
    pokupka = pokupka.split("\n")
	#if ""
    print(pokupka)

  #print("-------------------\n")