first_name = "John"
last_name = "Doe"


def get_initials(first_name, last_name):
    return last_name + " " + first_name[0] + "."

formatted_name  = get_initials(first_name, last_name)
formatted_name2  = get_initials("Володимир","Боклаг")
print(formatted_name)
print(formatted_name2)

text = "Python"
print(text.upper())  
print(text.lower())

text = "  hello       "
print(text.strip())
print(text.lstrip())