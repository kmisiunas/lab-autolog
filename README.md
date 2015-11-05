# lab-autolog

Automatically record parameters an experimental setup and send them online. 

Development in progress. 

## You will need

## How to setup

### Hardware

 - Raspberry Pi 2
 - Sensor Hat

### Software

To set it up by SSH into the raspberry pi. Configure network access, I2C and the sensor hat.

Download the program by typing

    cd ~
    git clone https://github.com/kmisiunas/lab-autolog.git
    pip install requests
    
Create configuration file with your keys from https://data.sparkfun.com/

    cd ~/lab-autolog/
    nano keys.json
    
Where you add `{ "public" : "publicKey", "private": "privateKey" }` with your keys. Then save by clicking Ctrl+X and saving.

Then edit the start-up script with command `sudo nano /etc/rc.local` to 

    # Auto run our application
    for i in {1..300}; do ping -c1 www.google.com &> /dev/null && break; done
    cd  ~/lab-autolog/
    git pull
    python lab-autolog.py &



## Architecture

 - [X] Send data every 5 min to data.sparkfun.com
 - [ ] Actively collect vibration data 

## ToDo

 - [ ] Test and fix if the autostart script works without the user

## Data Storage

### data.sparkfun.com

https://data.sparkfun.com/streams/OGzNYR7mdEFgYOON7g8m


