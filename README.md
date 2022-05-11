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

If you always want to keep your fancontrol the same as a latest sample JSON, execute below instead of above.

```shell
ln -s fancontrol.json.sample fancontrol.json
```

And then pull from this repository when `fancontrol.json.sample` is updated. No need to restart a daemon. The change will be automatically applied.



## Usage

```shell
python main.py
```



## How to make the fan control your own
You can tune up the fan control values referencing `fancontrol.json.sample`.

| Key               | Description                                                                                  | Type    |
| ----------------- | -------------------------------------------------------------------------------------------- | ------- |
| `min_temperature` | A minimum temperature that the function within the range is applied (include a boundary)     | Integer |
| `max_temperature` | A maximum temperature that the function within the range is applied (not include a boundary) | Integer |
| `min_speed`       | A minimum fan speed within the range of the function                                         | Integer |
| `max_speed`       | A maximum fan speed within the range of the function                                         | Integer |
| `interval`        | A value how often the function is updated                                                    | Integer |

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
ExecStart=python main.py # you may need to specify a full path of a executable python
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



## The origin of this project’s name

This project’s name stands for a CPU **fan** control tool using **Pip** for Raspberry **Pi**.

But, it has one more meaning. "Pippi" is a part of "Kare-pippi" (彼ピッピ), which is a Japanese slang used among high school girls in Japan. It means "more than friends, but not lovers". This project’s concept is "enough cooler, but not noisy", so it's a pun on the meaning "Kare-pippi".
