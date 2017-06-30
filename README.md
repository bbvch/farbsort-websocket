About
----
This is the python application running the websocket server that functions as a communication bridge between the PRU-Code (https://github.com/bbvch/pru-farbsort) and the Qt Gui (https://github.com/bbvch/farbsort-gui) 



System Requirements:
----

- Linux (Tested on Ubnutu 16.04 x64)
- Python 2.7 
- Tornado Webserver

Setup for non-development
----
_Note_: if setting up for development see further below

Preferably use the binary wheel installer but if unsure about platform support or need for advanced debugging use the source distribution

Installing & running
---
New versions can be installed over any old installed versions, python pip takes care of that. For a version rollback the newer versions have to be uninstalled first

1. Download the latest release for your platform
1. install using pip
  1. for a installation for the current user only use ```$>pip install <path_to_your_package>.whl --user```
  1. For a system whie installation use ```$>sudo pip install <path_to_your_package>.whl --user```
1. run as root using ```sudo python -m farbsort```

Uninstalling
---
1. run ```$>pip uninstall farbsort-websocket```


Setup for development
-----

Checkout:
```
git clone https://github.com/bbvch/farbsort-websocket.git
```

Preparation:
If python pip is installed, the server will automatically download the necessary libraries. 
using 'sudo apt-get install python-pip' will install pip on your system

```
sudo apt-get install python-tornado
```
	*OR* use python pip (if installed)
```
python -m pip install tornado
```
Build pyhton module 
---
run ```$>python setup.py sdist``` to build the source distribution. 
For the binary wheel distributions use ```$>python setup.py bdist_wheel -p linux-x86_64```

For more inforamtion about building packages call ```$>python setup.py --help```


Run in developer mode
---

Run server:
```
sudo python server.py
```

Run server in simulation mode:
```
python server.py --simulate
```


Tests
-----

Run tests:
```
make tests
```

Run simulation test script:
```
./test-one-stone-at-a-time.sh | python server.py --simulate
```
