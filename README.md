python-cp stands for Pyhton Couch Potato
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

Install other packages with

`sudo apt-get update`

`sudo apt-get install libffi-dev libssl-dev python3-dev python3-pip virtualenv`

`sudo apt-get install libmysqlclient-dev`

Install
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

How to Run
==========
```
python3 cp_local.py
```


TO DO
=====

Other
=====
Use the command `deactivate` to exit from virtualenv
