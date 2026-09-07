# **Requirements Note: Community Outreach Activity Logger**

**1\. Problem Statement**

According to a new UN Environment Programme report , the global temperature rise is set to cross 1.5°C, likely within the next few years, pushing climate risks and impacts to increasingly dangerous heights, but it is still possible to bring temperatures down and achieve global goals in the Paris Agreement(UNEP,2026). Climate change is presently one of the largest issues that the world faces. Communities are already being impacted by rising temperatures, freer storms, sea level rise and unpredictable weather particularly among small island nations. Building a more climate-resilient world is everyone's responsibility, not just governments or big companies the actions of ordinary individuals and groups can make a difference in the little things you do every day, such as planting trees, cleaning up the beach, conserving water, and sharing tips with others to reduce their energy consumption.

The problem is that these small climate actions, done by organizations and individual volunteers, are usually never written down anywhere. A club may clean a beach now and no one records the number of volunteers that turned up, the number of hours they spent, or the effect they had. The Community Outreach Activity Logger is a solution.A simple, easy-to-use computer program enabling organisations and individuals to log each climate related output that they engage in, with the results of this effort finally being visible, accessible and countable, and therefore celebrated.

**2\. Chosen Scenario**

Written in Python and designed to be run from the command-line, Community Outreach Activity Logger is a menu-driven program to record, view, update, delete, search, and analyse the community action projects that address climate change.

**3\.** Our project is centred around the Global Challenge , Climate Change. All activity types included in this programme have been selected because they all play a role in climate change reduction or mitigation in one or more ways. Each connected by the following simple explanations:

\-Beach Cleanup : Cleans plastic and rubbish off beaches. Plastic waste can pollute the oceans and leach out greenhouse gases, as well as harm ocean ecosystems that can sequester airborne carbon.

\-Tree Planting : Trees take in CO2 (the primary gas contributing to climate change).Trees make fantastic efforts to cope with climate change – one way ordinary people can do the same is to plant more trees.

\-Recycling Campaign : The use of raw materials for making new products requires a lot of energy and greenhouse gases are produced. The fewer ones needed because of recycling, the less emissions there will be.

\-Community Gardening : If food is grown locally, there will be local employment, less energy is used when transporting food long distances, and the green vegetation in the neighbourhood  will help keep neighbourhoods cool.

\-Join a movement : conducting campaigns to create more awareness about environmental conservation and climate action.

\-Water Conservation Campaign :Clean water is becoming more difficult to obtain in many areas due to climate change. Conserving water today will make communities more resilient against drought resulting from climate change.

\-Renewable Energy Awareness Workshop : Coal, oil and gas power generation are among the leading contributors to climate change. Educating the public on the benefits and use of solar, wind and other clean energy technologies can help communities transition away from fossil fuels.

\-Coastal Conservation Activity : Coastlines, coral reefs and mangroves defend us against rising sea level and storm surges, and they also capture a tremendous amount of carbon. Defending them achieves community survival from climate change and also slows down climate change at the same time. .

These activities can be logged providing not only a record, but also a measure in real numbers of what a community is doing to combat climate change.

**4\. Intended Users**  
\-Organisations : such as environmental clubs, school groups, or NGOs which organise a team of volunteers for an environmental action moment.

\-Individual: those who engage in a climate action activity independently, without joining a group/organization.

**5\. Functional Requirements**

The application should include a way for the user to be able to do the following:

\-Add a new outreach activity, choose from a fixed list of 8 climate-related activity types, and stating whether it was done by an Organization or an Individual.  
\-View all activities that have been logged so far, grouped by Organization and Individual.  
\-Update an existing activity's location, number of volunteers, hours and impact description, using its ID number.  
\-Delete an existing activity using its ID number.  
\-Search activities by entering a keyword that matches the type of activity, location, or name.  
\-Filter activities by GCGO themes (for example, "carbon absorption" or "reducing emissions")/ choosing from a list of the connections currently in use.  
\-View Statistics ; total of activities, total of volunteers, total of hours, and by activity type.  
\-View a report showing how activities are spread across the different climate change connections, so it is easy to see which areas the community is focusing on most.  
\-View an impact report highlighting the outcomes of each activity.  
\-Exit the Program properly.  
\-Save every type of data between runs of the program using a JSON file, without losing anything.

**6\. Data Fields Stored**

Each activity record contains the following fields:

| Field | Data Type | Description |
| :---- | :---- | :---- |
| id | integer | A unique number given to each activity automatically |
| activity\_type | string | One of the 8 fixed climate-related activity types |
| theme | string | How this activity connects to fighting climate change (looked up automatically) |
| date | string | The date the activity was logged (YYYY-MM-DD) |
| location | string | Where the activity took place |
| user\_type | string | "Organization" or "Individual" |
| name | string | The organization's name, or the individual's name |
| num\_volunteers | integer | How many volunteers took part (always 1 for an Individual) |
| hours | integer/float | How many hours were contributed |
| impact | string | A short description of what the activity achieved |

All of this is stored using nothing more than Python's built-in tools ;a dictionary that holds two lists, saved to a file called data/outreach\_data.json using Python's json module. No database is used, as required for this stage of the module.

{  
  "Organization": \[ {...}, {...} \],  
  "Individual":   \[ {...}, {...} \]  
}

**7\. Success Criteria**

\-This program doesn't crash under any circumstances, even when the user enters a mistake such as typing a letter in the place of a number or leaving a field blank or typing the wrong menu option.  
\-Information added during any running of the program remains until the next time the program is used.  
\-All the menu items function as intended and provide feedback to the user of what they have done.  
\-Anyone reading the impact report or the climate connection report can clearly see, in simple terms, how the community's efforts are helping fight climate change.

**Reference**

Programme, U. N. E. (2026, September 2). UNEP: World set to cross 1.5°C global warming, but can still limit, adapt to and return from higher temperatures. UN Environment; United Nations Environment Programme. [https://www.unep.org/news-and-stories/press-release/unep-world-set-cross-15degc-global-warming-can-still-limit-adapt-and](https://www.unep.org/news-and-stories/press-release/unep-world-set-cross-15degc-global-warming-can-still-limit-adapt-and)  
