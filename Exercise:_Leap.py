n = int(input("Enter Gregorian Year -> ").strip())

if n % 400 == 0:
    print("True")
elif n % 100 == 0:
    print("False")
elif n % 4 == 0:
    print("True")
else:
    print("False")
    
