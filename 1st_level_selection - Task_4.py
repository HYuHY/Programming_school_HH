'''
Решение задачи 4 из тестового задания на поступление в школу программистов Head Hunter

В некоторых числах можно найти последовательности цифр, которые в сумме дают 10. 
К примеру, в числе 3523014 целых четыре таких последовательности:
352 3014
3 523 014
3 5230 14
35 23014

Можно найти и такие замечательные числа, каждая цифра которых входит в по крайней 
мере одну такую последовательность.
Например, 3523014 является замечательным числом, а 28546 — нет (в нём нет 
последовательности цифр, дающей в сумме 10 и при этом включающей 5). 

Найдите количество этих замечательных чисел в интервале [1, 3100000] 
(обе границы — включительно).

Created on 7 сент. 2017 г.
@author: HYuHY
'''



def check_is_remarkable(number):
    number_list = [int(x) for x in str(number)]
    list_index_and_number = list(enumerate(number_list))
    list_rest = list_index_and_number [:]
    lng = len(number_list)
    for numeric in list_index_and_number:
        sum_10 = 0
        for i in range(numeric[0], lng):
            sum_10 += list_index_and_number[i][1]
            if sum_10 == 10:
                for j in range(i - numeric[0] + 1):
                    try:
                        list_rest.remove(list_index_and_number[numeric[0] + j])
                    except ValueError:
                        pass
            if sum_10 > 10 :
                break
        if list_rest == []:
            return True
        if numeric in list_rest:
            return False      
    

def write_result_to_file(A=1, B=1, 
                        quantity_remarkable = 0, 
                        remarkable_list = [],
                        not_remark_list = []):
    f = open("list_of_remarkable_numbers.txt", 'w')
    f.write("Quantity of remarkable numbers in [%s, %s] is %s" 
            % (A, B, quantity_remarkable)+ '\n')
    f.write("List of remarkable numbers: \n" + str(remarkable_list) + '\n')
    f.close()
    f = open("list_of_NOT_remarkable_numbers.txt", 'w')
    f.write("List of NOT remarkable numbers in [%s, %s]:" 
            % (A, B)+ '\n')
    f.write(str(not_remark_list) + '\n')    
    f.close()        
            
    

def main(A=19000, B=20000):
    remarkable_list = []
    not_remark_list = []
    remarkable_count = 0
    for number in range(A, B+1,1):
        remarkable_flag = check_is_remarkable(number)
        if remarkable_flag == True:
            remarkable_list.append(number)
            remarkable_count += 1
        else:
            not_remark_list.append(number)
    return remarkable_count, remarkable_list, not_remark_list


if __name__ == "__main__":
    A=1
    B=8400000
    quantity_remarkable, remarkable_list, not_remark_list = main(A, B)
    print("Quantity of remarkable numbers in [%s, %s] is %s" % (A, B, quantity_remarkable) )
    
    write_result=input("Press any letter-button to write result to files:\n" \
                       "list_of_remarkable_numbers.txt,\n" \
                       "list_of_NOT_remarkable_numbers.txt,\n" \
                       "(default Enter - refuse to write result in file)\n")
    if write_result.lower()!='':
        write_result_to_file(A, B, 
                             quantity_remarkable, 
                             remarkable_list, 
                             not_remark_list)
        print("Data have written in files")
    input("Press Enter to close program")