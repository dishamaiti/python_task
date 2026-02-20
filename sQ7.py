s = "ABZ"

if len(s) > 0 and s[0] == "A":
    if s[-1] == "Z":
        print("Valid AZ string")
    else:
        print("Starts with A but invalid end")
else:
    print("Invalid string")
