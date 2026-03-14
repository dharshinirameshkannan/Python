

amount=int(input("Enter the purchase amount:"))
if amount>5000:
    discount=20
elif amount>3000 and amount<5000:
    discount=15
elif amount>1000 and amount<3000:
    discount=10
else:
    discount=5
dis_amt=(amount*discount)/100
total_amt=amount-dis_amt
print("Purchase amount:",amount)
print("Discount Percentage:",discount,"%")
print("Discount Amount:",dis_amt)
print("Total Amount:",total_amt)