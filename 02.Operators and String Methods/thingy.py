user_amount= int(input("Put some numbers here for a magic trick: "))
total_value=0 

for total_value in range(0,20):
    final_value=total_value + user_amount
user_amount= int(input("One more: "))
print(final_value)