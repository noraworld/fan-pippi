# fan-pippi

## Requirements

```shell
sudo apt -y install libraspberrypi-bin
pip install -r requirements.txt
```

A reboot is required after the installation to perform `vcgencmd` without a root privilege.

## Setup

```shell
cp fancontrol.json.sample fancontrol.json
```

## Usage

```shell
python main.py
```

## How to make the fan control your own
TBD

TODO: Make a graph like [this](https://www.google.com/search?q=cpu+fan+control&tbm=isch#imgrc=uiX82SZ311m20M).

## Daemonization
First, create a service file for `systemctl` under the `$HOME/.config/systemd/user/` directory.

```shell
# $HOME/.config/systemd/user/fan-pippi.service

[Unit]
Description=fan-pippi
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/fan-pippi
ExecStart=python main.py # you may need to specify a full path of executable python
TimeoutSec=15
Restart=always

[Install]
WantedBy=default.target
```

Secondly, perform the following commands.

```shell
systemctl --user daemon-reload
systemctl --user enable fan-pippi.service # if you need to
systemctl --user start fan-pippi.service
```

Note that you need to setup and start the service at a user level, not a system wide.
