text = input("Enter your character: ")
if text.isalpha():
    print("This text is a letter")
elif text.isdigit():
    print("This text is a digit")
else:
    print("This text is a special character or symbol")
