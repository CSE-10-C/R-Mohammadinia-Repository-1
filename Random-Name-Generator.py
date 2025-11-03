import random

# Start
# x = number of which student is chosen in the class list

class_list = input("Enter student names separated by commas: ").split(',')

if len(class_list) == 0:
    print("No students available.")
else:
    x = random.randint(1, len(class_list))
    
    selected_student = class_list[x - 1]
    
    print(f"The random selected name is: {selected_student}")
