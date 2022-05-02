# fan-pippi

## Requirements

```shell
sudo apt -y install libraspberrypi-bin
pip install -r requirements.txt
```

A reboot is required after the installation to perform `vcgencmd` without a root privilege

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

TODO: Make a graph like [this](https://www.google.com/search?q=cpu+fan+control&tbm=isch#imgrc=uiX82SZ311m20M)
