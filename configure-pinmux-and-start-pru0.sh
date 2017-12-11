#!/bin/sh

echo "Configuring pins..."
cat <<EOF | config-pin -f
P8.11 pruout  # motor
P8.13 gpio    # compressor
P8.12 pruout  # valve1
P9.25 pruout  # valve2
P9.27 pruout  # valve3
P8.15 pruin   # pulsecounter
P8.16 pruin   # lightbarrier1
P9.24 pruin   # lightbarrier2
P8.14 gpio    # lightbarrier3
P8.17 gpio    # lightbarrier4
P8.19 gpio    # lightbarrier5
P9.30 pruin   # emergency-stop
EOF

echo "Starting pru0..."
echo am335x-pru0-fw > /sys/class/remoteproc/remoteproc1/firmware
echo start > /sys/class/remoteproc/remoteproc1/state
