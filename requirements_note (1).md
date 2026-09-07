# Requirements Note: Community Outreach Activity Logger

## 1. Problem Statement

Climate change is one of the biggest problems the world is facing
right now. Rising temperatures, stronger storms, rising sea levels,
and unpredictable weather are already affecting communities,
especially small island nations. Fighting climate change is not
only the job of governments and big companies — ordinary people and
local groups also play a real part, through small, everyday actions
like planting trees, cleaning beaches, saving water, and encouraging
others to use less energy.

The problem is that these small climate actions, done by
organizations and individual volunteers, are usually never written
down anywhere. A club might clean a beach today and nobody keeps a
record of how many volunteers came, how many hours they gave, or
what was achieved. Over time, this means the true impact of all
these community efforts is invisible — nobody can see the full
picture of how much climate action is actually happening on the
ground.

This project solves that problem with a simple, easy-to-use
computer program that lets organizations and individuals log every
climate-related outreach activity they take part in, so that this
effort can finally be seen, counted, and celebrated.

## 2. Chosen Scenario

**Community Outreach Activity Logger** — a menu-driven Python
command-line program that lets a user log, view, update, delete,
search, and analyse community activities that help fight climate
change.

## 3. Global Challenge / Mission Interest (GCGO): Climate Change

The Global Challenge our project is built around is **Climate
Change**. Every single activity type built into this program was
chosen because it directly helps reduce or respond to climate
change in some way. Here is how each one connects, explained simply:

- **Beach Cleanup** – Removes plastic and waste from beaches.
  Plastic waste breaks down and releases greenhouse gases, and it
  damages ocean ecosystems that help absorb carbon from the air.
- **Tree Planting** – Trees absorb carbon dioxide (the main gas
  causing climate change) from the air as they grow. Planting more
  trees is one of the most direct ways ordinary people can fight
  climate change.
- **Recycling Campaign** – Making new products from raw materials
  uses a lot of energy and creates a lot of greenhouse gases.
  Recycling reduces the need for this, which means fewer emissions.
- **Community Gardening** – Growing food locally means less fuel is
  burned transporting food long distances, and it protects green
  spaces that help cool our neighborhoods.
- **Sustainable Transport Campaign** – Cars and trucks that burn
  petrol or diesel are one of the biggest sources of greenhouse
  gases. Encouraging walking, cycling, or public transport reduces
  these emissions.
- **Water Conservation Campaign** – Climate change is making clean
  water harder to find in many places. Saving water today helps
  communities cope better with droughts caused by a changing
  climate.
- **Renewable Energy Awareness Workshop** – Burning coal, oil, and
  gas for electricity is a major cause of climate change. Teaching
  people about solar, wind, and other clean energy helps communities
  move away from fossil fuels.
- **Coastal Conservation Activity** – Coastlines, coral reefs, and
  mangroves protect us from rising seas and storms, and they also
  store large amounts of carbon. Protecting them helps communities
  survive climate change and slows it down at the same time.

By logging these activities, this program does not just keep a
record — it helps show, in real numbers, how much a community is
doing to fight climate change.

## 4. Intended Users

- **Organizations** — for example environmental clubs, school
  groups, or NGOs that bring a group of volunteers together for a
  climate action activity.
- **Individuals** — everyday people who take part in a climate
  action activity on their own, without belonging to an
  organization.

## 5. Functional Requirements

The application must let the user do the following:

1. Add a new outreach activity, choosing from a fixed list of 8
   climate-related activity types, and stating whether it was done
   by an Organization or an Individual.
2. View all activities that have been logged so far, grouped by
   Organization and Individual.
3. Update an existing activity's location, number of volunteers,
   hours, or impact description, using its ID number.
4. Delete an existing activity using its ID number.
5. Search activities by typing a keyword that matches the activity
   type, location, or name.
6. Filter activities by their specific climate change connection
   (for example, "carbon absorption" or "reducing emissions"),
   choosing from a list of the connections currently in use.
7. View statistics: the total number of activities, total
   volunteers, total hours, and hours broken down by activity type.
8. View a report showing how activities are spread across the
   different climate change connections, so it is easy to see which
   areas the community is focusing on most.
9. View an impact report summarising what each activity achieved.
10. Exit the program safely.
11. Keep all data saved between runs of the program, using a JSON
    file, so nothing is ever lost.

## 6. Data Fields Stored

Each activity record contains the following fields:

| Field           | Type   | Description                                                        |
|-----------------|--------|----------------------------------------------------------------------|
| id              | number | A unique number given to each activity automatically                |
| activity_type   | text   | One of the 8 fixed climate-related activity types                    |
| theme           | text   | How this activity connects to fighting climate change (looked up automatically) |
| date            | text   | The date the activity was logged (YYYY-MM-DD)                        |
| location        | text   | Where the activity took place                                         |
| user_type       | text   | "Organization" or "Individual"                                        |
| name            | text   | The organization's name, or the individual's name                      |
| num_volunteers  | number | How many volunteers took part (always 1 for an Individual)             |
| hours           | number | How many hours were contributed                                        |
| impact          | text   | A short description of what the activity achieved                     |

All of this is stored using nothing more than Python's built-in
tools — a dictionary that holds two lists, saved to a file called
`data/outreach_data.json` using Python's `json` module. No database
is used, as required for this stage of the module.

```
{
  "Organization": [ {...}, {...} ],
  "Individual":   [ {...}, {...} ]
}
```

## 7. Success Criteria

- The program runs without crashing, even when the user makes a
  mistake — for example typing letters where a number is expected,
  leaving a required field empty, or choosing a menu option that
  doesn't exist.
- Data entered in one run of the program is still there the next
  time the program is opened.
- Every menu option works correctly and gives the user clear
  feedback about what just happened.
- Anyone reading the impact report or the climate connection report
  can clearly see, in simple terms, how the community's efforts are
  helping fight climate change.
