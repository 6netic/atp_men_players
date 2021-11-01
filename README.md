This repo is the first part of a Machine Learning project.

At the end we'll be able to predict who the winner will be during a match between 2 tennis players.

That could be useful to bet on gambling websites.

Based on ATP and WTA tennis players ranking we'll scrap datas from www.flashscore.fr/tennis/classements/atp 
and www.flashscore.fr/tennis/classements/wta for collecting datas.

I chose the first 300 tennis men players from the ATP and WTA.
It's not possible to scrap that website directly as there are some JS scripts that prevent user to see 
all information.
He'll have to click on some buttons and links to expand data visualization on the webpage.
This is why I used Selenium to automate these actions.

As a result we'll get 2 types of csv files:
- men_ranking.csv and women_ranking.csv (the current ranking of tennis players)
- men_results.csv and women_results.csv (some match results for each player)

With these acquired data we'll be able to go further in data preparation (part 2) for our ML project.
  
This program is developed with Python v3.8 using a virtual environment.

So create your virtual environment and activate it.
Clone that repo to your computer and install the libraries : `pip install -r requirements.txt`

At the root folder, you need to put chromedriver file to make selenium work.
Depending on your chrome version you will install the appropriate version of chromedriver.
The downloading url page is : https://chromedriver.chromium.org/downloads

Once done type in `python start.py` to launch it.
