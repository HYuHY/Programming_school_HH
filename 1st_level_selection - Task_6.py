'''
Решение задачи 6 из тестового задания на поступление в школу программистов Head Hunter

Дано равенство, в котором цифры заменены на буквы:
rzwr + rqwz = tqtq 

Найдите сколько у него решений, если различным буквам 
соответствуют различные цифры (ведущих нулей в числе не бывает).

Created on 9 сент. 2017 г.
@author: HYuHY
'''
#count_variant = 0

#[[current_value, start_range, finish_range], [], []]
#level = 0,1,2,3,4 for t,q,w,z,r

def recursive_equal(list_of_values_ranges, level):
#    global count_variant
    roots = []
    for i in range(list_of_values_ranges[-level-1][1], list_of_values_ranges[-level-1][2]):
        list_of_values_ranges[-level-1][0] = i 
        if level > 0:
            x = recursive_equal(list_of_values_ranges, level-1)
            for j in x:
                roots.append(j)
        if level == 0 :     
            r, z, w, q, t = list_of_values_ranges
            left_part_equal = 1000*r[0] + 100*z[0] + 10*w[0] + r[0] +\
                            + 1000*r[0] + 100*q[0] + 10*w[0] + z[0]
            right_part_equal = 1000*t[0] + 100*q[0] + 10*t[0] + q[0]
            if  left_part_equal == right_part_equal:
                roots.append((r[0], z[0], w[0], q[0], t[0]))
#            count_variant += 1
    return roots        
         
            


def main():
    list_of_values_ranges = [[None,1,10],[None,0,10],[None,0,10],[None,0,10],[None,1,10]]
    level = 4
    roots = recursive_equal(list_of_values_ranges, level)
    print(len(roots))
    for i in roots:
        print(i)
    
if __name__ == "__main__":
    main()
#    print(count_variant)
    input("Press 'Enter' to close program \n")
    