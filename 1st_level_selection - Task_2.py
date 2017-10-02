'''
Решение задачи 2 из тестового задания на поступление в школу программистов Head Hunter

Условие задачи: 
Число 125874 и результат умножения его на 2 — 251748 можно получить 
друг из друга перестановкой цифр. 

Найдите наименьшее положительное натуральное x такое, что числа 3*x, 
4*x можно получить друг из друга перестановкой цифр.

Created on 6 сент. 2017 г.
@author: HYuHY
'''




def input_integer_multipliers(a=3, b=4):
    pass
    
def is_numbers_match(x_multiple_3, x_multiple_4):
    x_multiple_3 = list(str(x_multiple_3))
    x_multiple_4 = list(str(x_multiple_4))
    if len(x_multiple_3) == len(x_multiple_4):
        for number in x_multiple_3:
            try:
                x_multiple_4.remove(number)
            except ValueError:
                return False
    else:
        return False      
    return True

def main(a=4, b=5, lower_limit=1, upper_limit=150000):
    i=lower_limit
    found=False
    while found==False and i <= upper_limit:
        x_multiple_3 = a * i
        x_multiple_4 = b * i
        if is_numbers_match(x_multiple_3, x_multiple_4) == True:
            found = True
        else:
            i+=1  
    return i  

   

if __name__ == "__main__":
    a=4
    b=5
    lower_limit=1
    upper_limit=150000
    number = main(a, b, lower_limit, upper_limit)
    print("The first number in [%s, %s] is " %(lower_limit, upper_limit), number)
    input("Press 'Enter' key to close program \n") 