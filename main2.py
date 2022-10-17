import names

def parametr(a):
    if a == 2:
        return 'male'
    elif a == 1:
        return 'female'

def name(b):
    if b == 3:
        print(names.get_first_name(gender=parametr))
    elif b == 1:
        print(names.get_full_name(gender=parametr))
    elif b == 2:
        print(names.get_last_name())

c = input('Вітаємо у вигадувальнику імен, почнімо? ')
while c.lower() == "так":
    parametr(int(input("Для кого вигадуємо ім'я? (ч/ж - 1/2) ")))
    name(int(input("Ви хочете отримати повне ім'я, прізвище чи просто ім'я? (1, 2, 3) ")))
    c = input('Продовжуємо? ')