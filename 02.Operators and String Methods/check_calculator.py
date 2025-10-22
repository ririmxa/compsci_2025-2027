money_amount= int(input("How much money do you have left?: "))
        
for _ in range (20):
    if money_amount>20:
        break
    print ("Buy more!")
    money_amount=int(input("Do you have any money left?: "))
    if money_amount==0:
        print ("Go rob a bank.")
        money_amount=int(input("Do you have any money left?: "))
    if money_amount % 2==0:
        print ("I still need your money bro..")
        money_amount=int(input("Now..how much money do you have left?: "))
print("Too much! You're making this place look suspicious. Leave!")

user_amount= int(input("Put some numbers here for a magic trick: "))
total_value=0 

for total_value in range(0,20):
    final_value=total_value + user_amount
user_amount= int(input("Put some numbers here for a magic trick: "))
print(final_value)