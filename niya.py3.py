purchase_amount=int(input("Enter the purchase amount:"))
if purchase_amount>500:
    discount=purchase_amount*0.20
    final_amount=purchase_amount-discount
    print("Final Amount=",final_amount)
elif (purchase_amount>=200) and (purchase_amount<500):
    discount=purchase_amount*0.10
    final_amount=purchase_amount-discount
    print("Final Amount:",final_amount)
else:
    print("Final Amount:",purchase_amount)
