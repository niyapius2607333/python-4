'''
Author : Niya Pius
Date : 15-10-2024
Python program to use loop toprint odd numbers
Version 1.0
'''
limit=int(input("Enter the limit:"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2
