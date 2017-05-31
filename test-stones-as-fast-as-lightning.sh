#!/bin/bash

# conveyor-speed=58mm/s

source test_basic_steps.sh

echo "Setting up the hardware in 2 secs" >&2
sleep 2
echo "Set up the hardware now..." >&2
start_hardware &

echo "Waiting 1 secs before we begin with the first stone..." >&2
sleep 1
echo "...and here we go..." >&2

for round in {1..10}
do
    run_blue_stone &
    sleep 0.7
    run_red_stone &
    sleep 0.7
    run_white_stone &
    sleep 0.7
    run_undetected_stone &
    sleep 0.7
done

sleep 6

echo "Finished" >&2
echo "Stop the hardware" >&2
stop_hardware &
