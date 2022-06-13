# fan-pippi
A scalable fan control tool for Raspberry Pi.



## Requirements

```shell
sudo apt -y install libraspberrypi-bin
pip install -r requirements.txt
```

A reboot is required after the installation so that `vcgencmd` can be performed without a root privilege.



## Setup
### `fancontrol.json`
Choose what you prefer from `fancontrol.sample/`.

```shell
cp fancontrol.sample/<EITHER>.json fancontrol.json
```

If you always want to keep your fancontrol the same as one of the latest sample JSON files, execute below instead of above.

```shell
ln -fs fancontrol.sample/<EITHER>.json fancontrol.json
```

And then pull from this repository when `fancontrol.sample/` is updated. No need to restart a daemon. The changes will be automatically applied.

### `.env`

```shell
cp .env.sample .env
```

| Key        | Description                                                                                               | Type    | Sample value |
| ---------- | --------------------------------------------------------------------------------------------------------- | ------- | :----------: |
| `FAN_PIN`  | A GPIO pin number in which a fan control cable (a blue cable in general) is plugged (see the image below) | Integer | `14`         |
| `PWM_FREQ` | A PWM frequency                                                                                           | Integer | `45`         |

![](https://prismic-io.s3.amazonaws.com/rpf-products/3495afb8-59f5-4972-86df-cd292b234745_Case+Fan+Instructional+diagram.png)
_References: https://www.raspberrypi.com/products/raspberry-pi-4-case-fan/_



## Usage

```shell
python main.py
```



## How to make the fan control your own
You can tune up the fan control values referencing `fancontrol.sample/`.

| Key               | Description                                                                                  | Type    |
| ----------------- | -------------------------------------------------------------------------------------------- | ------- |
| `min_temperature` | A minimum temperature that the function within the range is applied (include a boundary)     | Integer |
| `max_temperature` | A maximum temperature that the function within the range is applied (not include a boundary) | Integer |
| `min_speed`       | A minimum fan speed within the range of the function                                         | Integer |
| `max_speed`       | A maximum fan speed within the range of the function                                         | Integer |
| `interval`        | A value how often the function is updated                                                    | Integer |

TODO: Make a graph like [this](https://www.google.com/search?q=cpu+fan+control&tbm=isch#imgrc=uiX82SZ311m20M).

TIPS: As you may know, the more a CPU fan speed gets down, the more a CPU temperature goes up. Try to find out your best preference while tuning up.



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
This project’s name stands for a CPU "**fan**" control tool using "**Pip**" for Raspberry "**Pi**".

But, it has one more meaning. "Pippi" is a part of "Kare-pippi" (彼ピッピ), which is a Japanese slang used among high school girls in Japan. It means "more than friends, but not lovers." This project’s concept is "enough cooler, but not noisy", so it's a pun on the meaning "Kare-pippi."
