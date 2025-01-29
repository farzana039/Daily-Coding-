num=int(input("enter num"))
if((num%4 == 0 and num%100 !=0 ) or (num%400 == 0)):
     print("Leap Year")
else:
     print("Not a Leap year")
