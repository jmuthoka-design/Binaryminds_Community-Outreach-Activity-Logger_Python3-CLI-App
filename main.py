"""
main.py

This is the file you run to start the program.
It shows the menu, asks the user what they want to do, and calls
the right function from records.py or processing.py to do it.
"""

import records
import processing
import data_store


def main():
    # Load any activities that were saved from before.
    # If this is the very first time running the program, this will
    # just give us empty lists to start with.
    saved_records, saved_next_id = data_store.load_data()
    records.records = saved_records
    records.next_id = saved_next_id

    print("====================================")
    print(" COMMUNITY OUTREACH ACTIVITY LOGGER")
    print("====================================")

    program_is_running = True

    while program_is_running:
        print("\n1. Add outreach activity")
        print("2. View all activities")
        print("3. Update activity")
        print("4. Delete activity")
        print("5. Search activities")
        print("6. Filter by GCGO theme")
        print("7. View statistics")
        print("8. View GCGO theme distribution report")
        print("9. View impact report")
        print("10. Exit")

        choice = input("Enter your choice: ")
        choice = choice.strip()

        if choice == "1":
            records.add_activity()
            data_store.save_data(records.records, records.next_id)

        elif choice == "2":
            records.view_all_activities()

        elif choice == "3":
            records.update_activity()
            data_store.save_data(records.records, records.next_id)

        elif choice == "4":
            records.delete_activity()
            data_store.save_data(records.records, records.next_id)

        elif choice == "5":
            processing.search_activities()

        elif choice == "6":
            processing.filter_by_theme()

        elif choice == "7":
            processing.view_statistics()

        elif choice == "8":
            processing.view_theme_distribution_report()

        elif choice == "9":
            processing.view_impact_report()

        elif choice == "10":
            print("Thank you for supporting environmental outreach. Goodbye!")
            program_is_running = False

        else:
            print("Please enter a number from 1 to 10.")


# This makes sure main() only runs when we start this file directly.
if __name__ == "__main__":
    main()
