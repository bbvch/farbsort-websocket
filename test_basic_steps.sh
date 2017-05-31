start_hardware () {
    echo "conveyor=running"
    echo "compressor=start"
}

stop_hardware () {
    echo "conveyor=stopped"
    echo "compressor=stop"
}

run_blue_stone () {
    echo "lightbarrier1=on"
    sleep .1
    echo "lightbarrier1=off"
    sleep 1.5
    echo "color=blue"
    sleep 1.5
    echo "lightbarrier2=on"
    sleep .1
    echo "lightbarrier2=off"
    sleep .4
    echo "valve1=on"
    sleep .1
    echo "valve1=off"
    sleep .1
    echo "lightbarrier3=on"
    sleep 1
    echo "lightbarrier3=off"
}

run_red_stone () {
    echo "lightbarrier1=on"
    sleep .1
    echo "lightbarrier1=off"
    sleep 1.5
    echo "color=red"
    sleep 1.5
    echo "lightbarrier2=on"
    sleep .1
    echo "lightbarrier2=off"
    sleep 1.3
    echo "valve2=on"
    sleep .1
    echo "valve2=off"
    sleep .1
    echo "lightbarrier4=on"
    sleep 1
    echo "lightbarrier4=off"
}

run_white_stone () {
    echo "lightbarrier1=on"
    sleep .1
    echo "lightbarrier1=off"
    sleep 1.5
    echo "color=white"
    sleep 1.5
    echo "lightbarrier2=on"
    sleep .1
    echo "lightbarrier2=off"
    sleep 2.2
    echo "valve3=on"
    sleep .1
    echo "valve3=off"
    sleep .1
    echo "lightbarrier5=on"
    sleep 1
    echo "lightbarrier5=off"
}

run_undetected_stone () {
    echo "lightbarrier1=on"
    sleep .1
    echo "lightbarrier1=off"
    sleep 1.5
    echo "color=transparent"
    sleep 1.5
    echo "lightbarrier2=on"
    sleep .1
    echo "lightbarrier2=off"
}
