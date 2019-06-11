items = ['молоко', 'сыр', 'творог', 'кефир', 'яблоко']
# 1 Вариат
# for i, item in enumerate(items):
#     print(i + 1, item)

# 2 Вариат
# len_items = len(items)
# c = 0
# while c != len_items:
#   for i in items:
#     c += 1
#     print(c, i)

# 4 Ваш лунный вес
# your_kg = float(input('Введите Ваш вес: '))
# yar = int(input('Какой сейчас год: '))
# c = 15
# for i in range(1, c + 1):
#   print(your_kg, yar)
#   your_kg += 1
#   yar += 1
# print(your_kg * 0.165, yar)

# 1 Функция лунного веса
# def my(x, y):
#   c = 15
#   yar = int(input('Какой сейчас год: '))
#   for i in range(1, c + 1):
#     print(x, yar)
#     x += y
#     yar += 1
#   print(x * 0.165, yar)

# my(50, 1)

# 2 Функция лунного веса и кол-во лет
# def my(x, y, z):
#   yar = int(input('Какой сейчас год: '))
#   for i in range(1, z + 1):
#     print(x, yar)
#     x += y
#     yar += 1
#   print(x * 0.165, yar)

# my(50, 1, 5)



# 3 Программа для лунного веса
import sys
def my():
  kg = int(sys.stdin.readline()) # Изначальный вес
  yar = int(sys.stdin.readline()) # какой сейчас год
  count = int(sys.stdin.readline()) # сколько прибавлять к весу
  yar_count = int(sys.stdin.readline()) # на сколько лет расчет
  for i in range(1, yar_count + 1):
    print(kg, yar)
    kg += count
    yar += 1
  print(kg * 0.165, yar)

my()
