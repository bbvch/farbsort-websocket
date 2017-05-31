#!/bin/bash

# conveyor-speed=58mm/s

source test_basic_steps.sh

echo "Setting up the hardware in 2 secs" >&2
sleep 2
echo "Set up the hardware now..." >&2
start_hardware &

echo "Waiting 2 secs before we begin with the first stone..." >&2
sleep 2
echo "...and here we go..." >&2

run_blue_stone &
sleep 5
run_red_stone &
sleep 5
run_white_stone &
sleep 10

echo "Finished" >&2
echo "Stop the hardware" >&2
stop_hardware &
