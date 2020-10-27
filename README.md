# Python Couch Potato

python-cp is a command line interface tool used to update sporting events on the Peerplays blockchain by sending data to hosted [bos-auto](https://gitlab.com/PBSA/PeerplaysIO/bos/bos-auto) instances.

The project repo is maintained in the [Peerplays GitLab Repository](https://gitlab.com/PBSA/PeerplaysIO/tools-libs/python-cp).


# System Requirements

Ubuntu 18.04 and 20.04 with at least 2GB of RAM is recommended.

Software Dependencies

```
sudo apt-get update && sudo apt-get install libffi-dev libssl-dev python3-dev python3-pip virtualenv libmysqlclient-dev
```
# Installation

```bash
git clone https://gitlab.com/PBSA/PeerplaysIO/tools-libs/python-cp.git

cd python-cp
```
It is best practice to use python virtual environments. https://docs.python.org/3/tutorial/venv.html

```bash
python3 -m venv env
source env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip3 install -r requirements.txt
```

Copy the exmaple config to a file called config-bos-mint.yaml.
```
cp example.config-bos-mint.yaml config-bos-mint.yaml
```
Update config-bos-mint.yaml with the relevant information.

# Usage
```
python3 cp_local.py
```
Now, to update any created event use 'u' And 
to create any new event use 'c'

```
(env) $ python3 cp_local.py
u: Update event
c: Create event
Enter your choice u/c:
```
