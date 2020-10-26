python-cp stands for Pyhton Couch Potato
This project is part of peerplays block chain tech catering sports feed for bos-auto. 
The purpose of this project is to develop a mechanism for gathering information about sporting events collectively.

The code is expected to run in a server/machine with a fixed IP so that witnesses can enable access to those specific python-cp servers.

python-cp is a command line interface for couch potatos to update sporting events to peerplays witnesses running bos-auto.

The project repo is maintained at `Peerplays Gitlab Repo <git@gitlab.com:PBSA/PeerplaysIO/tools-libs/python-cp.git>`

Install
=======
```
git clone https://gitlab.com/PBSA/PeerplaysIO/tools-libs/python-cp/-/tree/passive
cd python-cp
git checkout passive
```

Recommend running in a virtual environment

```
virtualenv -p python3 env        to create virtualenv
source env/bin/activate          to activate virtualenv
pip3 install -r requirements.txt
```

Update config-bos-mint.yaml with relevant information

How to Run
==========
```
python3 cp_local.py
```

or

```
ipython3 -i cp_local.py
self.Create()
self.Update()
```

TO DO
=====

Other
=====
Use the command <deactivate> to exit from virtualenv
