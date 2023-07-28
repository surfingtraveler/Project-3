# Global Shark Attacks

## This is a full-stack data visualization web application that allows users to interactively explore data extracted from opendatasoft's dataset on Global Shark Attacks.

### Overview

Shark attacks are always a possibility when venturing out into the ocean. Whether going swimming at the beach, hitting some waves, or deep diving for treasure, the thought of being attacked by a shark is floating in the back of our minds. But how often do shark attacks actually happen? This question of curiosity sparked the interest of this analysis. Displayed in this interactive application are the recorded shark attacks for the last five years.

### Tools and Framework

1. MongoDB database
2. Python
3. Flask Application
4. Javascript
5. HTML/ CSS
6. Dataset from opendatasoft's Global Shark Attack-World

## Instructions for accessing interactive map

To access the Shark Attacks Dashboard Page, open the following file names in VS Code:
mongodb_script.py
dashboard.py
dashboard.js
dashboard.html
sharks.css

Open a terminal window and make sure in directory where folders are located.

    Enter: python mongodb_script.py

    Enter: python dashboard.py

Optional: Open MongoDB Compass to view database.

In terminal window in VS Code, Ctrl + click on http://127.0.0.01:5000 link.

Now open a separate browser window in browser of your choice and go to:

localhost:5000/dashboard.html

Wait for page to load. Be patient as it may take a bit for all markers and drop downs to load.

Once page has finished loading, should see world map. Can filter by Year, Fatal/Non-Fatal attacks. Can click on makers on map to get shark attack data.

## Instructions for accessing charts

To access the Shark Attacks Charts Page, open the following file names in VS Code:
mongodb_script.py
app2.py
logic.js
index.html

Open a terminal window and make sure in directory where folders are located.

    Enter: python mongodb_script.py

    Enter: python app2.py

In terminal window in VS Code, Ctrl + click on http://127.0.0.01:5000 link.

This opens a separate browser window in browser and direct you to:

localhost:5000/dashboard.html

The Chart with Attacks by Sex will load. The data is for the years 2019 - 2023. An element will apprear when
the cursor hoovers over a bar providing the details to the data.

### Resources

https://www.chartjs.org/docs/latest/
https://www.geeksforgeeks.org/how-to-connect-mongodb-compass-to-flask/
https://www.mongodb.com/docs/manual/core/aggregation-pipeline/
https://www.mongodb.com/docs/manual/reference/operator/aggregation/
https://www.mongodb.com/docs/manual/reference/operator/aggregation/

Example charts used in presentation:
Year of attack chart source - https://vizthis.wordpress.com/2016/11/17/data-in-the-water-shark-attacks-visualized/
Global Land-Ocean Temperature Index: https://www.ecoclimax.com/2016/12/global-temperature-increase-1880-2015.htm
