person_age = 12
parents = True 
height = 1.37 

condition_1 = {
    person_age > 12 and 
    person_age < 65 and 
    height > 1.35 
}

condition_2 = {
    person_age <= 12 and 
    parents == True and 
    height > 1.35 
}

print (condition_1 or condition_2)




