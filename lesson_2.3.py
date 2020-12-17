# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['spring', 'summer', 'autumn', 'winter']
season_dict = {1 : 'spring', 2 : 'summer', 3 : 'autumn', 4 : 'winter'}
month = int(input('Введите число от 1 до 12'))
if month == 3 or month == 4 or month == 5:
    print(season_dict.get(1))
    print(season_list[0])
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(2))
    print(season_list[1])
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(3))
    print(season_list[2])
elif month == 12 or month == 1 or month == 2:
    print(season_dict.get(4))
    print(season_list[3])
else:
    print('Введите корректное число месяца')