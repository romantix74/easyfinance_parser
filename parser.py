#!/usr/bin/python


# для выборки даты
date_words = "СЕНТЯБР"

in_file = []
with open('input.txt') as f:
 # in_file = f.readlines()
  in_file = f.read().split(date_words)

 
print(in_file[0])
print(in_file[3])
  
# for i in in_file:
  # if date_words in i: 
    # print(i)