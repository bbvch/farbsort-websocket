.PHONY: run-server tests install

run-server:
	sudo python server.py

tests:
	nosetests -v .

install:
	cp farbsort-websocket.service /etc/systemd/system/
	sed -i "s|/root/farbsort-websocket|$(CURDIR)|" /etc/systemd/system/farbsort-websocket.service
	cp farbsort-pinmux-and-pru.service /etc/systemd/system/
	sed -i "s|/root/farbsort-websocket|$(CURDIR)|" /etc/systemd/system/farbsort-pinmux-and-pru.service
