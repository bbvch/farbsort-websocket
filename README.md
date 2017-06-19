System Requirements:
----

- Linux (Tested on Ubnutu 16.04 x64)
- Python 2.7 
- Tornado Webserver 

Setup
-----

Checkout:
```
git clone https://github.com/bbvch/farbsort-websocket.git
```

Preparation:
```
sudo apt-get install python-tornado
```
	*OR* use python pip (if installed)
```
python -m pip install tornado
```

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
