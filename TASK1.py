#Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))

if (number<1000 and number>99 or number>-1000 and number<-99):
    x = (abs(number)%10+(abs(number)//10)%10+(abs(number)//10//10))
    print(x)
else: print("вы ввели не трехзначное число")