
try:
    # Ask for temperature from  user
    n = float(input("Enter Temperature (# only) --> "))
    
    # Ask for unit (F, C)
    unit = input("Is the temperature in fahrenheit or celsius (name only, no capitalization) --> ").strip().lower()
    
    # conversion from fahrenheit into celsius and kelvin
    if unit == "fahrenheit":
        celsius = (n - 32) * 5/9
        kelvin = celsius + 273.15
        # print results
        print(str(n) + "°F is " + str(round(celsius,2)) + "°C and " + str(round(kelvin,2)) + "K")
        
    # conversion from celsius into fahrenheit and kelvin
    elif unit == "celsius":
        fahrenheit = (n * 9/5) + 32
        kelvin = n + 273.15
        # print results
        print(str(n) + "°C is " + str(round(fahrenheit,2)) + "°F and " + str(round(kelvin,2)) + "K")

 # Error if something other than fahrenheit and celsius is added, or units are spelled wrong.       
    else:
        print("ERROR: Please type 'fahrenheit' or 'celsius'")

# Error if temperature added is not a valid digit
except ValueError:
    print("ERROR: Please enter a valid number")
