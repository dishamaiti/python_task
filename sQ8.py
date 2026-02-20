s = "12ab"

if s[:2].isdigit() and s[-2:].isalpha():
    print("Valid format")
else:
    print("Invalid format")
