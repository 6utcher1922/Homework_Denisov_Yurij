# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

def find_mounths(m):
    months_dict = {1:'январь, 31 день', 2:'февраль, 28 дней', 3:'март, 31 день', 4:'апрель, 30 дней', 5:'май, 31 день', 6:'июнь, 30 дней', 7 :'июль, 31 день', 8 : 'август, 31 день', 9 :'сенябрь, 30 дней', 10 :'октябрь, 31 день', 11 :'ноябрь, 30 дней', 12 :'декабрь, 31 день'}
    if m in months_dict:
        return f"Вы ввели {months_dict[m]}"
    else:
        return 'Такого месяца нет!'

print(find_mounths(2))
print(find_mounths(20))
print(find_mounths(3))
print(find_mounths(7))