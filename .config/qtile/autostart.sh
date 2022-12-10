#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
lxsession &
xrandr --output DVI-D-0 --mode 1920x1080 -r 144 &
xrandr --output DP-0 --mode 2560x1440 --primary -r 144 &
nitrogen --restore
picom --config $HOME/.config/picom/picom.conf --experimental-backends &
run nm-applet &
run volumeicon &
dunst &
