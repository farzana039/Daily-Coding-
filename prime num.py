def is_prime(num):
    if num<=1: #if number is less than 1 ,it is not a prime number .then return false
        return False
    for i in range(2,int(num**0.5)+1):# ranges from 2 to square root of the number
        if num%i == 0:
            return False
        return True
num=int(input("Enter a num"))
if is_prime(num):
        print("Is a prime")
else:
        print("Is not a prime")
        
