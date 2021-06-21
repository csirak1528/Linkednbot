# LinkedIn Bot

Functionality: This bot will automatically open up Google Chrome and Connect and Message people a piece of text you specify. You can also apply whatever search filters you would normally use on LinkedIn. 


Prerequesites (Do this first!): 

1) Open up Terminal on your Mac and run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`. This will install a package manager called Homebrew. 
2) Run `brew install git` to install Git. 
3) Now, run `brew install python3` to install Python3. 
4) Now run `python3 -m pip install selenium` to install Selenium package. 

Setup: 

MacOS Setup Instructions

1) Open up Terminal and Run `cd Desktop` and then `git clone https://github.com/csirak1528/Linkednbot.git`
2) Download and install VSCode from https://code.visualstudio.com/download
3) Open VSCode and go to File -> Open... -> (Find the LinkednBot folder in your file explorer and click it) 
4) Click on main.py; you will need to edit this file. 
5) In the variable called "browser," replace the text with this: /Users/<USERNAME>/Desktop/Linkednbot/chromedriver. USERNAME should be the username of your Mac laptop. (If you don't know this, open a new Terminal and type `cd ..` and type `ls` and you should see your username) 
7) In the field that says, "MESSAGE", place in the text you would like to DM people on LinkedIn with. This message must be under 300 characters. 
8) Scroll down and find a variable called "userData." Change the username field to be the email you use to login into LinkedIn. Change the password field to your LinkedIn password. 
9) Now open LinkedIn on a new Google Chrome window and suppose you want to message anyone who comes up under a search for "early stage investor" To do this, type "early stage investor" in the search bar. Then, click "People". Then click "Connections" and make sure 1st and 2nd ONLY are selected. Then apply any other filters you want (I reccomend using Location filter). Once you are done, copy the URL. 
10) Paste that exact URL into the text for the "search_link" variable. Now we are done editing main.py. 
11) Now we can use this script to automatically launch Google Chrome, open up LinkedIn, run this exact search query, and message people the text you inserted into main.py. 
12) On your VSCode, click `Ctrl ~`
13) This will launch a terminal. In this terminal, type `python3 main.py`. Now, wait a few moments and you will see a Chrome window boot up and do what was discussed above. 

That's it! You have successfully automated LinkedIn! 
Follow the same protocol to run different searches and filters. Please make sure you monitor the application as it runs because there are some edge cases that have not been addressed yet. For example, if it tries to message someone where it requires you to enter the email of that person first, the bot cannot handle this. You must hit "cancel" and X out that window so that it can move onto the next person. 
  


