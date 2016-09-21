# lab-autolog

Automatically record parameters of the lab and store them online. Find the graphs here:

http://kmisiunas.github.io/lab-autolog/

## Setup

### Hardware

 - Raspberry Pi 2 +
 - Sensor Hat
 
We recommend raising the rPI above the sensor to minimise the heating from the processor.

### Software

 - [Raspbian OS](https://www.raspbian.org/)
 - Activate I2C via `raspi-config`
 - Connect rPI to the internet
 
To set it up by SSH into the raspberry pi. Download the program by typing

    cd ~
    git clone https://github.com/kmisiunas/lab-autolog.git
    pip install requests
    

Then edit the start-up script with command `sudo nano /etc/rc.local` to 

    # Auto run our application
    for i in {1..300}; do ping -c1 www.google.com &> /dev/null && break; done
    cd  ~/lab-autolog/
    git pull
    python lab-autolog.py &



## Architecture

New architecture uses GitHub almost exclusively. We use three repositories for this:

 1. `master` for storing the program
 2. `gh-pages` for storing UI for data accessing
 3. `data` for storing collected data

Thus we need to add access keys to the repository to get this repository to work. These should be added to `config.json` that is excluded from the repository. 

The data repository is stored as a separate `data/` folder witch automatically points to the right repository. 

## ToDo

 - [ ] Test and fix if the autostart script works without the user
 - [ ] add outside [weather station](https://www.cl.cam.ac.uk/research/dtg/weather/current-obs.txt)
 - [ ] locally stored values for fast access on http://kmisiunas.github.io/lab-autolog/
 - [ ] migrate to otther chart libraty?
 - [ ] better homepage

## Data Storage


## Technical documentation
 - [GitHub Pages](https://help.github.com/articles/what-are-github-pages/)
