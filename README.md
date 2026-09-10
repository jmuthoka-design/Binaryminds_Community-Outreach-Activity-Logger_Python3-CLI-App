# Community Outreach Activity Logger

This is a simple Python command-line program that helps an **Organization**
or an **Individual** to keep track of environmental proctection activities.It will show what activity was done, where, by how many volunteers,
for how many hours, and what impact it had.

This is CLI application (just functions, lists, dictionaries, and a JSON file).

## Features

1. **Add outreach activity** – log a new activity with all its details
2. **View all activities** – see everything logged so far, grouped by
   Organization and Individual
3. **Update activity** – change the location, volunteers, hours, or
   impact of an existing activity using its ID number
4. **Delete activity** – remove an activity using its ID number
5. **Search activities** – find activities by typing a keyword that
   matches the activity type, location, or name
6. **Filter by GCGO theme** – pick a GCGO theme from a list and see
   every activity that connects to it
7. **View statistics** – see totals: number of activities, total
   volunteers, total hours, and hours per activity type
8. **View GCGO theme distribution report** – see how many activities
   and hours belong to each GCGO theme
9. **View impact report** – a readable summary of the impact of
   every activity logged
10. **Exit** – close the program safely

All data is saved automatically to `data/outreach_data.json`, so
nothing is lost when you close the program and run it again.

## The 8 Activity Types

1. Beach Cleanup
2. Tree Planting
3. Recycling Campaign
4. Community Gardening
5. Join a movement
6. Water Conservation Campaign
7. Renewable Energy Awareness Workshop
8. Coastal Conservation Activity

## Our Project Structure

```
outreach_app/
├── main.py           <- run this file to start the program
├── validation.py      <- checks that user input is valid
├── data_store.py       <- saves and loads data from the JSON file
├── records.py           <- add/view/update/delete activities
├── processing.py         <- search, statistics, and impact report
├── data/
│   └── outreach_data.json  <- sample data (and where your data is saved)
└── README.md
```

Each file has a clear job, which makes the program easier to read, understand , and explain

- **main.py** shows the menu and decides which function to call
- **validation.py** makes sure the user cannot type something that
  would crash the program (empty text, letters instead of numbers)
- **data_store.py** is the only file that opens or writes to the
  data file
- **records.py** holds the activity list and does the actual
  Add / View / Update / Delete work
- **processing.py** does the "thinking" work: searching and adding
  up numbers for the statistics and impact report

## How to Run It

1. You have to make sure you have Python 3 installed.
2. Put all the files in the same folder, keeping the `data` folder
   next to `main.py`.
3. Open a terminal in that folder and run:

```
python3 main.py
```

4. Follow the menu by typing a number from 1 to 8 and pressing Enter.

## Sample Data

The `data/outreach_data.json` file already has 3 example activities
in it (a beach cleanup, a tree planting, and a recycling campaign),
so you can try out View, Search, Statistics, and the Impact Report
right away without having to add anything first. You can check.

## Global Challenge Connection (GCGO)

This project connects to the **Climate Change** . Every one of the 8
activity types has its own specific GCGO theme
(for example, Beach Cleanup is linked to "Marine pollution & waste
reduction", and Tree Planting is linked to "Reforestation,
ecosystems & carbon absorption"). 
We want to use this opportunity to get people participate in our environment protection.

## AI Assistance

Parts of this project were developed with help from Claude (an AI
assistant by Anthropic). You can check `ai_disclosure.md` for full details.
https://drive.google.com/file/d/1GYXm0Qd3_rU4lRv8Pu81t9y6rZL3Njm6/view?ts=6aa332ae
