'''
Author : Niya Pius
Date : 08-10-2024
Python program to format date and time
Version 1.0
'''
from datetime import datetime
print(datetime.now())
current_time =datetime.now()
print(current_time)
format1=current_time.strftime("%Y")
print(format1)
format2=current_time.strftime("%Y-%m-%d %H-%M-%S")
print(format2)
format3=current_time.strftime("%m/%d/%Y")
print(format3)
format4=current_time.strftime("%A,%B %d,%Y")
print(format4)
format5=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format5)
format6=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format6)
format7=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format7)
format8=current_time.isoformat()
print(format8)
format9=current_time.strftime("%d")
print(format9)
format10=current_time.strftime("%H:%M:%S")
print(format10)
format11=current_time.strftime("%B")
print(format11)
format12=current_time.strftime("%Y")
print(format12)



