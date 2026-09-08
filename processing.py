"""
processing.py

This file processes and analyses our data. It has:
  - a search/filter feature
  - two analysis/report features (statistics, and an impact report)

It uses functions from records.py to get the data it needs.
"""

import records
import validation


def search_activities():
    """Find activities that match a keyword the user types in.
    This is our search/filter feature."""
    keyword = input("Type a word to search for (activity, location, or name): ")
    keyword = keyword.strip().lower()

    all_activities = records.get_all_activities_in_one_list()
    matching_activities = []

    for activity in all_activities:
        activity_type_lower = activity["activity_type"].lower()
        location_lower = activity["location"].lower()
        name_lower = activity["name"].lower()

        if keyword in activity_type_lower or keyword in location_lower or keyword in name_lower:
            matching_activities.append(activity)

    if len(matching_activities) == 0:
        print("No activities matched that search.\n")
    else:
        print("\n--- Search Results ---")
        for activity in matching_activities:
            records.print_one_activity(activity)
        print("----------------------\n")


def filter_by_theme():
    """
    Show the list of GCGO themes in use, let the user pick one,
    and list every activity that matches it. This is our second
    search/filter feature, focused on the GCGO theme instead of
    a free-typed keyword.
    """
    all_activities = records.get_all_activities_in_one_list()

    if len(all_activities) == 0:
        print("\nNo activities have been saved yet.\n")
        return

    # Build a list of themes that are actually being used right now,
    # without any repeats.
    themes_found = []
    for activity in all_activities:
        theme = activity["theme"]
        if theme not in themes_found:
            themes_found.append(theme)

    print("\n--- GCGO Themes In Use ---")
    number = 1
    for theme in themes_found:
        print(str(number) + ". " + theme)
        number = number + 1
    print("--------------------------")

    theme_choice = validation.ask_for_a_number("Choose a theme number: ")

    while theme_choice < 1 or theme_choice > len(themes_found):
        print("Please choose a number from the list above.")
        theme_choice = validation.ask_for_a_number("Choose a theme number: ")

    chosen_theme = themes_found[theme_choice - 1]

    print("\n--- Activities for theme: " + chosen_theme + " ---")
    for activity in all_activities:
        if activity["theme"] == chosen_theme:
            records.print_one_activity(activity)
    print("--------------------------------------------------\n")


def view_theme_distribution_report():
    """
    Analysis feature: show how many activities and hours belong to
    each GCGO theme. This shows the environmental impact spread
    across the different global challenge themes.
    """
    all_activities = records.get_all_activities_in_one_list()

    if len(all_activities) == 0:
        print("\nNo activities have been saved yet.\n")
        return

    # This dictionary will count activities and hours for each theme.
    activities_per_theme = {}
    hours_per_theme = {}

    for activity in all_activities:
        theme = activity["theme"]

        if theme in activities_per_theme:
            activities_per_theme[theme] = activities_per_theme[theme] + 1
            hours_per_theme[theme] = hours_per_theme[theme] + activity["hours"]
        else:
            activities_per_theme[theme] = 1
            hours_per_theme[theme] = activity["hours"]

    print("\n--- GCGO Theme Distribution Report ---")
    for theme in activities_per_theme:
        count = activities_per_theme[theme]
        hours = hours_per_theme[theme]
        print(theme)
        print("   Activities: " + str(count) + "   Hours: " + str(hours))
    print("---------------------------------------\n")


def view_statistics():
    """
    Analysis feature 1: show totals like number of activities,
    total hours, total volunteers, and hours per activity type.
    """
    all_activities = records.get_all_activities_in_one_list()

    if len(all_activities) == 0:
        print("\nNo activities have been saved yet.\n")
        return

    total_activities = len(all_activities)
    total_hours = 0
    total_volunteers = 0

    for activity in all_activities:
        total_hours = total_hours + activity["hours"]
        total_volunteers = total_volunteers + activity["num_volunteers"]

    organization_count = len(records.records["Organization"])
    individual_count = len(records.records["Individual"])

    # This dictionary will count hours for each activity type.
    hours_by_activity_type = {}

    for activity in all_activities:
        activity_name = activity["activity_type"]

        if activity_name in hours_by_activity_type:
            hours_by_activity_type[activity_name] = hours_by_activity_type[activity_name] + activity["hours"]
        else:
            hours_by_activity_type[activity_name] = activity["hours"]

    print("\n--- Statistics ---")
    print("Total activities: " + str(total_activities))
    print("  From organizations: " + str(organization_count))
    print("  From individuals: " + str(individual_count))
    print("Total volunteers: " + str(total_volunteers))
    print("Total hours: " + str(total_hours))

    print("\nHours per activity type:")
    for activity_name in hours_by_activity_type:
        hours = hours_by_activity_type[activity_name]
        print("  " + activity_name + ": " + str(hours) + " hours")
    print("------------------\n")


def view_impact_report():
    """
    Analysis feature 2: show a readable report describing the
    impact of every activity that has been logged.
    """
    all_activities = records.get_all_activities_in_one_list()

    if len(all_activities) == 0:
        print("\nNo activities have been saved yet.\n")
        return

    print("\n--- Impact Report ---")
    for activity in all_activities:
        print(activity["activity_type"] + " at " + activity["location"] + " on " + activity["date"])
        print("  By: " + activity["name"] + " (" + activity["user_type"] + ")")
        print("  Volunteers: " + str(activity["num_volunteers"]) + "   Hours: " + str(activity["hours"]))
        print("  Impact: " + activity["impact"])
        print("")
    print("----------------------\n")
