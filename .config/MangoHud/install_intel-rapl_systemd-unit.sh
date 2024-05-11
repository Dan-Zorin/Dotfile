#!/bin/bash

# Check if script is running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Create the systemd service file
cat << EOF > /etc/systemd/system/mangohud_intel-rapl_permissions.service
[Unit]
Description=MangoHud - Change permissions of intel-rapl file at boot
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/bin/chmod +r '/sys/class/powercap/intel-rapl:0/energy_uj'
RemainAfterExit=yes
User=root

[Install]
WantedBy=multi-user.target
EOF

# Reload the systemd daemon to recognize the new service
systemctl daemon-reload

# Enable the new service so it starts on boot
systemctl enable --now mangohud_intel-rapl_permissions.service

echo "Service installed and enabled successfully"
