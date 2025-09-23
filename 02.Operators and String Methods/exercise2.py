def discount_calculate(basket_value):
    discount_total = basket_value * 0.1
    return discount_total

def membership_discount_calculate(basket_value):
    membership_discount_total = basket_value * 0.2
    return membership_discount_total

def membership_discount_check(is_member,membership_discount_total,basket_value):
    if is_member==True:
        return membership_discount_total
    else:
        return basket_value

def discount_check(basket_value):
    if basket_value>100:
        return True
    else:
        return False
    
def final_discount(is_member, basket_value):
    if is_member==True and basket_value>100:
        return basket_value - (basket_value * 0.2)
    elif is_member==True or basket_value>100:
        return basket_value - (basket_value * 0.1)
    else:
        return basket_value
    

print(final_discount(True, 150))
print(final_discount(False, 150))
print(final_discount(True, 70))
print(final_discount(False, 70))