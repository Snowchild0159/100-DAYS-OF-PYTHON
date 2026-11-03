first_name = input("Enter your fisrt name :")
last_name = input("Enter your last name :")
def format_name(first_name, last_name) :
    """
    Take a first and last name and format it to return the title case version of the name
    """
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    fromated_first_name = first_name.title()
    fromated_last_name = last_name.title()
    return f"Hello {fromated_first_name} {fromated_last_name}"
print(format_name(first_name, last_name))


