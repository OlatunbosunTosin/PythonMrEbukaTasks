total_bill = float(input("Enter bill: "))
is_member = input("Enter yes/no: ")
 
if total_bill >= 1000 and is_member.lower() == "yes":
    discount = (10 / 100) * total_bill
    final_amount = total_bill - discount
    print(f"10% off\nfinal amount = {final_amount}")
 
elif total_bill >= 1000 and is_member.lower() == "no":
    discount = (5 / 100) * total_bill
    final_amount = total_bill - discount
    print(f"5% off\nfinal amount = {final_amount}")
 
else:
    print(f"No discount\nfinal amount = {total_bill}")

