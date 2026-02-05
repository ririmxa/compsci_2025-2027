def snake():
    length = int(input("Enter the length of the snake: "))
    if length < 0:
        raise ValueError("Length must be non-negative")
    body = ""
    for i in range(length):
        if i % 2 == 0:
            body += "/"
        else:
            body += "\\"
    body += "*"
    print(body)
    
snake()
