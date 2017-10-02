'''
Решение задачи 3 из тестового задания на поступление в школу программистов Head Hunter

Условие задачи: 
Наименьшее число m, такое, что m! делится без остатка на 10 — это m=5 (5! = 120). 
Аналогично, наименьшее число m, такое, что m! делится без остатка на 25 — это m=10. 
В общем случае, значение функции s(n) равно наименьшему числу m, такому что m! 
без остатка делится на n. Определим функцию S(M, N) = ∑s(n) для всех n ∈ [M, N]. 
К примеру, S(6, 10) = 3 + 7 + 4 + 6 + 5 = 25. Найдите S(4600000, 4700000).

Created on 6 сент. 2017 г.
@author: HYuHY
'''

def divisors_for_number(number):
    """
    Find and return all simple divisors for number
    According to the basic theorem of arithmetic 
    the factorization of a number into prime factors 
    exists and is unique.
    Also
    The search must also continue until d=n**(1/2). 
    After the end of this algorithm, if the number 
    n does not equal 1, then the remaining value 
    is also simple, since it is not divisible by 
    any number that does not exceed the root of 
    the remaining value; so we add it to the list 
    of simple divisors
    """
    divisors_number = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            divisors_number.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        divisors_number.append(number)
#    print(divisors_number)
    return divisors_number

def evristik_m(divisors_n):
    """
    This function determines the unique divisors and
    quantity and minimum m for m!  for each of them.
     
    Minimum m for m! in numerator s(n) must contain
    neseccary divisors from n; for example:
    m!/n = m!/(1*2*2*2*3*3*3*3*5*5*7)
    that means 3 must appear in m! at least 4 times,
    in 3, 6, 9, 12. For divisors 5 and 7 it happen 
    in 5, 10 and 7. Obviously, minimum m for m! will
    be maximum from prioduct of unique divisors by a
    its quantity. Result this multiplication return 
    in sorted list on third position of every tuple.  
    
    """
    divisors_unique_count = []
    previous_i = 0
    for i in divisors_n:
        if i != previous_i:
            previous_i = i
            count_i = divisors_n.count(i)
            divisors_unique_count.append((i, count_i, i*count_i))
    
    divisors_unique_count.sort(key = lambda x: x[2])
#    print(divisors_unique_count)
    return divisors_unique_count

def main (M=5, N=15):
    summ_M_N = 0
    list_n_m = []
    for n in range(M,N+1,1):
        divisors_n = divisors_for_number(n)
        divisors_unique_count = evristik_m(divisors_n)
        m = divisors_unique_count[-1][2]
        summ_M_N += m
        list_n_m.append((n,m))
        
    return summ_M_N, list_n_m


if __name__ == "__main__":
    M=4600000
    N=4700000
    summ_M_N, list_n_m = main(M, N)
    print("S(",M,", ",N,") = ", summ_M_N)
#    print(list_n_m)
    input("Press Enter to close program \n")
