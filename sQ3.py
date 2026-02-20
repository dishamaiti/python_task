s = "code9"
last_char = s[-1]

if last_char.isdigit():
    print("Ends with digit")
elif last_char.isalpha():
    print("Ends with character")
else:
    print("Ends with special symbol")
