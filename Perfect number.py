def perfect_number(num):
    if num <= 1:
        return False
     #using list comprehension ,looping through i in range num divided by 2 and passing a condition that num modulo of i is equal to 0.which means it is divisible by num
    divisors_sum = sum(i for i in range(1, num // 2 + 1) if num % i == 0)
    return divisors_sum == num
num=int(input())
print(perfect_number(num))
