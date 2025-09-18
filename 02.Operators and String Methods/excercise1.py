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
    
def shopping_expierence_old(basket_value):
    total_cost = basket_value
    if discount_check(basket_value):
        discount_total = discount_calculate(basket_value)
        total_cost = basket_value - discount_total
    return total_cost
    
def shopping_expierence(basket_value,is_member):
    total_cost_member = basket_value
    if is_member:
        membership_discount_total = membership_discount_calculate(basket_value)
        total_cost_member = basket_value - membership_discount_total
    return total_cost_member

def nearly_final_value(basket_value, is_member):
    cost_old = shopping_expierence_old(basket_value)
    cost_member = shopping_expierence(basket_value, is_member)
    return cost_old + cost_member 

def final_value(basket_value,is_member):
    first_cost = basket_value
    cost_discounts = nearly_final_value(basket_value,is_member)
    return cost_discounts - first_cost


print(final_value(150,True))
print(final_value(150,False))
print(final_value(70,False))