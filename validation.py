"""
validation.py

validates user input to prevent errors : we have two users(organization and Individual)
"""


def ask_for_a_number():
    """
    We ask the user to type a whole number bigger than 0 so as to find a volunteer activity.
    We use try/except because if someone types letters instead of
    numbers, Python's int() function would normally crash the
    whole program. This keeps that from happening.
    """
    while True:
        text = input("Enter a number bigger than 0: ")
        try:
            number = int(text)
            if number > 0:
                return number
            else:
                print("Please enter a number bigger than 0.")
        except ValueError:
            print("That is not a valid number. Please try again.")



def ask_for_name():
    """
    Ask the user to type their individual or the organisation's name, and make sure they did not
    just press Enter and leave it empty. Required fields will not 
    be allowed to be blank.
    """
   while True:
        name = input("Enter your full name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Please enter a valid name.")
        else:
            return name



def ask_for_user_type():
    """
    Ask if the user is an Organization or an Individual.
    Keep asking until they type something we understand.
    """
    while True:
        answer = input("Is this an (O)rganization or an (I)ndividual? ")
        answer = answer.strip().lower()

        if answer == "o" or answer == "organization":
            return "Organization"
        elif answer == "i" or answer == "individual":
            return "Individual"
        else:
            print("Please type O for Organization or I for Individual.")
