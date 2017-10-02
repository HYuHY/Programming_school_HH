'''
Решение задачи 1 из тестового задания на поступление в школу программистов Head Hunter

Условие задачи: 
Если мы возьмем 47, перевернем его и сложим, получится 47 + 74 = 121 — число-палиндром. 

Если взять 349 и проделать над ним эту операцию три раза, то тоже получится палиндром: 
349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337

Найдите количество положительных натуральных чисел меньших 12111 таких, что из них нельзя 
получить палиндром за 50 или менее применений описанной операции 
(операция должна быть применена хотя бы один раз).

Created on 5 сент. 2017 г.
@author: HYuHY

'''

def is_palindrom_in_list (list_sum):
    for i in list_sum:
        if str(i) == str(i)[::-1]:
            return True  
    return False  

def calc_sums (start_number, iteration=50, show_list=False):
    x=start_number
    list_sum=[]
    list_sum.append(x)
    for i in range(iteration):
        x = x + int(str(x)[::-1])
        list_sum.append(x)
    if show_list:
        print("list_sum for ","test_number = ", start_number, " is \n", list_sum)
        
    return list_sum
        
    
    
def write_result_to_file(natural_not_palindrom=None, list_number_not_palindrom=[]):
    f = open("list_of_not_palindrom_numbers.txt", 'w')
    f.write("natural_not_palindrom = " + str(natural_not_palindrom) + '\n')
    f.write(str(len(list_number_not_palindrom)) + '\n')
    f.write("list_of_not_palindrom_numbers = " + str(list_number_not_palindrom) + '\n')
    f.close()
    

def check_single_number(test_number):
    if is_palindrom_in_list(calc_sums(test_number, show_list=True))==False:
        print("Test number = ", test_number, "have not palindrom after iterations")
    else:
        print("Test number = ", test_number, "HAVE palindrom!")


def check_input_integer(default_limit = 12110):
    correct=False
    while correct==False:
        try:
            upper_number=input("Insert upper number of row to research for " \
                                "palindrom after iterations of summation (default = 12110) \n")
                
            upper_number = int(upper_number)
            correct = True
            if upper_number>12110:
                print("upper number must be less than 12111 and more than 0")
                correct = False
        except ValueError:
            if not upper_number:
                upper_number = default_limit
                correct=True
            else:
                print('please, input integer,  0 < x < 12111')
    return upper_number
    

def main(limit_number):   
    natural_not_palindrom=0
    list_number_not_palindrom = []
    for i in range(1, limit_number, 1):
        if is_palindrom_in_list(calc_sums(i))==False: 
            natural_not_palindrom +=1
            list_number_not_palindrom.append(i)
    return natural_not_palindrom , list_number_not_palindrom
    



if __name__ == "__main__":
    
    upper_number = check_input_integer()
    print("upper_number = ", upper_number)
    check_single_number(upper_number)
    
    natural_not_palindrom , list_number_not_palindrom = main(upper_number)
    
    print("natural_not_palindrom = ", natural_not_palindrom)
    print("list_of_not_palindrom_numbers = ", list_number_not_palindrom)
    
    write_result=input("Press any letter-button to write result to file \n"\
                       "list_of_not_palindrom_numbers.txt\"\n"\
                       "(default Enter - refuse to write result in file)\n")
    if write_result.lower()!='':
        write_result_to_file(natural_not_palindrom, list_number_not_palindrom)
        print("Data have written in file")

    input("Press 'Enter' to close program \n")
            
