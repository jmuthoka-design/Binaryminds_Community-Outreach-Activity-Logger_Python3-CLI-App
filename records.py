"""
records.py

This file has our activity list, our saved data, and the four
main actions: Add, View, Update, Delete. This is often called
"CRUD" (Create, Read, Update, Delete).

Our data is stored like this:

records = {
    "Organization": [ list of activity dictionaries ],
    "Individual":   [ list of activity dictionaries ]
}

So it is one dictionary that holds two lists inside it.
"""

import datetime
import validation

# Our fixed list of 8 environmental activities.
ACTIVITIES = [
    "Beach Cleanup",
    "Tree Planting",
    "Recycling Campaign",
    "Community Gardening",
    "Sustainable Transport Campaign",
    "Water Conservation Campaign",
    "Renewable Energy Awareness Workshop",
    "Coastal Conservation Activity"
]

# Every activity connects to a GC (Great Challenge) theme.
# This dictionary matches each activity type to its theme, so we
# never have to ask the user to type it themselves - we look it up.
ACTIVITY_THEMES = {
    "Beach Cleanup": "Marine pollution & waste reduction",
    "Tree Planting": "Reforestation, ecosystems & carbon absorption",
    "Recycling Campaign": "Waste reduction & resource conservation",
    "Community Gardening": "Sustainable communities & biodiversity",
    "Sustainable Transport Campaign": "Reducing transport-related emissions",
    "Water Conservation Campaign": "Protecting and conserving water resources",
    "Renewable Energy Awareness Workshop": "Climate-change awareness",
    "Coastal Conservation Activity": "Protecting coastal ecosystems"
}

# This dictionary holds all of our saved activities.
# main.py fills it in with saved data when the program starts.
records = {
    "Organization": [],
    "Individual": []
}

# Every activity gets a unique ID number. This variable keeps track
# of which number to use next. It goes up by 1 every time we add
# a new activity.
next_id = 1


def display_activity_choices():
    """Print the list of 8 activities with numbers next to them."""
    print("\n--- Activity Types ---")
    number = 1
    for activity_name in ACTIVITIES:
        print(str(number) + ". " + activity_name)
        number = number + 1
    print("----------------------")


def find_activity_by_id(activity_id):
    """
    Look for an activity with this ID number.
    First we check the Organization list, then the Individual list.
    We return two things: the activity we found, and which list it
    was in ("Organization" or "Individual"). If we do not find it,
    we return None, None.
    """
    for activity in records["Organization"]:
        if activity["id"] == activity_id:
            return activity, "Organization"

    for activity in records["Individual"]:
        if activity["id"] == activity_id:
            return activity, "Individual"

    return None, None


def get_all_activities_in_one_list():
    """
    Put every activity (organization and individual) into a single
    list. This makes it easier when we want to look at everything
    at once, like for statistics or the impact report.
    """
    all_activities = []

    for activity in records["Organization"]:
        all_activities.append(activity)

    for activity in records["Individual"]:
        all_activities.append(activity)

    return all_activities


def print_one_activity(activity):
    """Print one activity in a neat, readable way."""
    print("ID " + str(activity["id"]) + ": " + activity["activity_type"] + " on " + activity["date"])
    print("   GCGO Theme: " + activity["theme"])
    print("   Location: " + activity["location"])
    print("   " + activity["user_type"] + ": " + activity["name"])
    print("   Volunteers: " + str(activity["num_volunteers"]) + "   Hours: " + str(activity["hours"]))
    print("   Impact: " + activity["impact"])


def add_activity():
    """Ask the user questions and save a new activity. (Create)"""
    global next_id

    display_activity_choices()
    choice_number = validation.ask_for_a_number("Choose an activity type (1-8): ")

    while choice_number < 1 or choice_number > len(ACTIVITIES):
        print("Please choose a number from the list above.")
        choice_number = validation.ask_for_a_number("Choose an activity type (1-8): ")

    # Lists start counting at 0, so we subtract 1 to get the right activity.
    activity_type = ACTIVITIES[choice_number - 1]

    location = validation.ask_for_text("Where did this activity happen? ")
    user_type = validation.ask_for_user_type()
    name = validation.ask_for_text("Enter the name of the " + user_type.lower() + ": ")

    # Only organizations tell us how many volunteers came.
    # An individual is always just 1 person.
    if user_type == "Organization":
        number_of_volunteers = validation.ask_for_a_number("How many volunteers took part? ")
    else:
        number_of_volunteers = 1

    hours = validation.ask_for_a_number("How many hours were contributed? ")
    impact = validation.ask_for_text("What impact did this activity have? ")

    today = datetime.date.today()
    today_text = str(today)

    # Look up the GC theme that matches this activity type.
    theme = ACTIVITY_THEMES[activity_type]

    new_activity = {
        "id": next_id,
        "activity_type": activity_type,
        "theme": theme,
        "date": today_text,
        "location": location,
        "user_type": user_type,
        "name": name,
        "num_volunteers": number_of_volunteers,
        "hours": hours,
        "impact": impact
    }

    # Put the new activity into the correct list.
    if user_type == "Organization":
        records["Organization"].append(new_activity)
    else:
        records["Individual"].append(new_activity)

    print("\nActivity saved! It was given ID number " + str(next_id) + ".\n")

    next_id = next_id + 1


def view_all_activities():
    """Show every activity that has been saved so far. (Read)"""
    if len(records["Organization"]) == 0 and len(records["Individual"]) == 0:
        print("\nNo activities have been saved yet.\n")
        return

    print("\n=== Organization Activities ===")
    if len(records["Organization"]) == 0:
        print("(none yet)")
    else:
        for activity in records["Organization"]:
            print_one_activity(activity)

    print("\n=== Individual Activities ===")
    if len(records["Individual"]) == 0:
        print("(none yet)")
    else:
        for activity in records["Individual"]:
            print_one_activity(activity)
    print()


def update_activity():
    """Let the user change one detail of an existing activity. (Update)"""
    view_all_activities()

    all_activities = get_all_activities_in_one_list()
    if len(all_activities) == 0:
        return

    activity_id = validation.ask_for_a_number("Enter the ID of the activity to update: ")
    activity, user_type = find_activity_by_id(activity_id)

    if activity is None:
        print("Sorry, no activity has that ID.\n")
        return

    print("\nWhat do you want to update?")
    print("1. Location")
    print("2. Number of volunteers")
    print("3. Hours")
    print("4. Impact")
    field_choice = input("Enter your choice (1-4): ")
    field_choice = field_choice.strip()

    if field_choice == "1":
        activity["location"] = validation.ask_for_text("Enter the new location: ")
        print("Location updated.\n")

    elif field_choice == "2":
        if activity["user_type"] == "Individual":
            print("An individual is always 1 volunteer, so there is nothing to update.\n")
        else:
            activity["num_volunteers"] = validation.ask_for_a_number("Enter the new number of volunteers: ")
            print("Number of volunteers updated.\n")

    elif field_choice == "3":
        activity["hours"] = validation.ask_for_a_number("Enter the new number of hours: ")
        print("Hours updated.\n")

    elif field_choice == "4":
        activity["impact"] = validation.ask_for_text("Enter the new impact description: ")
        print("Impact updated.\n")

    else:
        print("That was not a valid choice. Nothing was changed.\n")


def delete_activity():
    """Remove an activity from our records using its ID. (Delete)"""
    view_all_activities()

    all_activities = get_all_activities_in_one_list()
    if len(all_activities) == 0:
        return

    activity_id = validation.ask_for_a_number("Enter the ID of the activity to delete: ")
    activity, user_type = find_activity_by_id(activity_id)

    if activity is None:
        print("Sorry, no activity has that ID.\n")
        return

    records[user_type].remove(activity)
    print("Activity " + str(activity_id) + " has been deleted.\n")
