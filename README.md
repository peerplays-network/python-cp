# Python Couch Potato

python-cp is a command line interface tool used to update sporting events on the Peerplays blockchain by sending data to hosted [bos-auto](https://gitlab.com/PBSA/PeerplaysIO/bos/bos-auto).

The project repo is maintained in the [Peerplays GitLab Repository](https://gitlab.com/PBSA/PeerplaysIO/tools-libs/python-cp).

## Installation

It is best practice to use python virtual environments. https://docs.python.org/3/tutorial/venv.html

```bash
python3 -m venv env
source env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

Update config_cp.yaml with relevant information

## Usage
```bash
ipython3 -i cp_local.py
```
```
self.Create()
self.Update()
```
