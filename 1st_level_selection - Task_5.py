'''
Решение задачи 5 из тестового задания на поступление в школу программистов Head Hunter

Рассмотрим спираль, в которой, начиная с 1 в центре, последовательно 
расставим числа по часовой стрелке, пока не получится спираль 5 на 5 

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
Можно проверить, что сумма всех чисел на диагоналях равна 101. 

Чему будет равна сумма чисел на диагоналях, для спирали размером 1169 на 1169?

Created on 7 сент. 2017 г.
@author: HYuHY
'''

def corners_of_square(side):
    corners = [side**2 - (side-1)*n for n in range(0,4,1)]
#    print(corners)
    return corners[::-1]

#print(corners_of_square(7))


def main(long_side=77):
    summ_of_corners = 1
    full_list_corners = []
    for side in range(3,long_side+1,2):
        corners = corners_of_square(side)
        for i in corners:
            full_list_corners.append(i)
            summ_of_corners += i 
    return summ_of_corners, full_list_corners


if __name__ == "__main__":
    long_side = 1091
    summ_of_corners, full_list_corners = main(long_side)
    print("Sum of numbers in corners of spiral with side = %s is \n%s"
           % (long_side, summ_of_corners) )
    print("Full list of corners: \n", full_list_corners)
