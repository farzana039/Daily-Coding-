def mirror(n):
    for i in range(1,n+ 1):#upper triangle
        print(" " * (n- i) + "* " * i)
    for i in range(n, 0, -1):#mirror image of upper triangle
        print(" " * (n- i) + "* " * i)
n = int(input())
mirror(n)
