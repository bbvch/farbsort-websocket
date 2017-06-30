About
----
This is the python application running the websocket server that functions as a communication bridge between the PRU-Code (https://github.com/bbvch/pru-farbsort) and the Qt Gui (https://github.com/bbvch/farbsort-gui) 



System Requirements:
----

- Linux (Tested on Ubnutu 16.04 x64)
- Python 2.7 
- Tornado Webserver



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
For more inforamtion about building packages call ```$>python setup.py --help```

Run
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
