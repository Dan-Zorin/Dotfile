#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
lxsession &
#xrandr --output HDMI-0 --mode 1440x900 --primary -r 75 &
feh --bg-fill .Wallpaper/neon.jpg &
picom --config $HOME/.config/picom/picom.conf --experimental-backends &
run nm-applet &
run volumeicon &
dunst &
