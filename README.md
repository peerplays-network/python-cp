python-cp stands for Pyhton Couch Potato.

This project is part of peerplays block chain tech catering sports feed for bos-auto. 
The purpose of this project is to develop a mechanism for gathering information about sporting events collectively.

The code is expected to run in a server/machine with a fixed IP so that witnesses can enable access to those specific python-cp servers.

python-cp is a command line interface for couch potatos to update sporting events to peerplays witnesses running bos-auto.

The project repo is maintained at `Peerplays Gitlab Repo <git@gitlab.com:PBSA/PeerplaysIO/tools-libs/python-cp.git>`

System Requirements
==================
Ubuntu Linux 18.04 and 20.04 recommended.
RAM: More than 2 GB recommended.

Software Dependencies
====================
`python3`
`virtualenv`

Python is installed by default in Ubuntu Linux.

Install other packages
=======================

`sudo apt-get update`

`sudo apt-get install libffi-dev libssl-dev python3-dev python3-pip virtualenv`

`sudo apt-get install libmysqlclient-dev`

Install Python_cp
=======
```
git clone https://gitlab.com/PBSA/PeerplaysIO/tools-libs/python-cp.git
cd python-cp
git checkout passive
```

Recommend running in a virtual environment

```
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt
```

Update config-bos-mint.yaml with relevant information
=====================================================
- In case to to make python_cp 'chain' sepcfic from 'Gladiator' spicific
```
change connection to `use: ChainName` from `use: gladiator`
```

- In case to change the gladiator node

```
gladiator:
        node:
            - ws://96.46.49.16:8090
```
Change above node to any desired node



How to Run CP
==========
```
python3 cp_local.py
```
Now, to update any created event use 'u' And 
to create any new event use 'c'

```
(env) ubuntu@ip-172-31-27-119:~/cp/python-cp$ python3 cp_local.py
u: Update event
c: Create event
Enter your choice u/c:

```

Creating new event with selection of 'c'
=======================================

- First need to select sports on which user want to create a new event

```
Enter your choice u/c: c

Select Sport
0 Baseball
1 Basketball
2 Soccer
3 Ice Hockey
4 AmericanFootball
Enter index of key:
```

- If user want want to create event on 'Baseball' sports, then need to select '0' index

```
Enter index of key: 0

Select Event Group
0 MLB#RegSeas
1 MLB#Playoffs
2 MLB#WorldSeries
Enter index of key:
```
- Now, select a 'Event group' for the selected sports, for ' MLB#RegSeas' select '0' index

```
Enter index of key: 0

Select Home Team
0 Arizona Diamondbacks
1 Atlanta Braves
2 Baltimore Orioles
3 Boston Red Sox
4 Chicago Cubs
5 Chicago White Sox
6 Cincinnati Reds
7 Cleveland Indians
8 Colorado Rockies
9 Detroit Tigers
10 Houston Astros
11 Kansas City Royals
12 Los Angeles Angels
13 Los Angeles Dodgers
14 Miami Marlins
15 Milwaukee Brewers
16 Minnesota Twins
17 New York Mets
18 New York Yankees
19 Oakland Athletics
20 Philadelphia Phillies
21 Pittsburgh Pirates
22 San Diego Padres
23 San Francisco Giants
24 Seattle Mariners
25 St. Louis Cardinals
26 Tampa Bay Rays
27 Texas Rangers
28 Toronto Blue Jays
29 Washington Nationals
Enter index of key:
```
- Here, need to select 'Home team' for the event. For 'Chicago Cubs', choose index '4'

```
Enter index of key: 4

Select Away Team
0 Arizona Diamondbacks
1 Atlanta Braves
2 Baltimore Orioles
3 Boston Red Sox
4 Chicago Cubs
5 Chicago White Sox
6 Cincinnati Reds
7 Cleveland Indians
8 Colorado Rockies
9 Detroit Tigers
10 Houston Astros
11 Kansas City Royals
12 Los Angeles Angels
13 Los Angeles Dodgers
14 Miami Marlins
15 Milwaukee Brewers
16 Minnesota Twins
17 New York Mets
18 New York Yankees
19 Oakland Athletics
20 Philadelphia Phillies
21 Pittsburgh Pirates
22 San Diego Padres
23 San Francisco Giants
24 Seattle Mariners
25 St. Louis Cardinals
26 Tampa Bay Rays
27 Texas Rangers
28 Toronto Blue Jays
29 Washington Nationals
Enter index of key:
```

- Choose 'Away team' now. For 'Chicago White Sox' , choose index '5'

```
Enter index of key: 5

Enter Start Time in the format 2020-08-25T22:00:00Z :
```

- Here, need to enter the start time in '2020-08-25T22:00:00Z' format
```
Enter Start Time in the format 2020-08-25T22:00:00Z :2020-10-29T21:00:00Z
(env) mach :~/pytoncouchpotato/python-cp$
```



TO DO
=====


Other
=====
Use the command `deactivate` to exit from virtualenv
