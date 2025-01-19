def maximum_money(N,K):
    if (N%2 == 0):
        return (N//2)*K #if the number of the houses are even then the answer is just number of houses by 2 because of alternate houses multiplied by amount
    
    else:
        return ((N//2) +1 )*K #if the number of houses are odd it simply equal to N//2 +1 *k

N=int(input("Enter Number Of Houses:"))
K=int(input("Enter Maximum Money in each house:"))
output=maximum_money(N,K)
print(output)      
