# junk's COMBO MAKER

The COMBO MAKER is a small every day calandar counter for your desktop, inspired by the likes of Simone Giertz's [Everyday Calendar](https://www.youtube.com/watch?v=-lpvy-xkSNA).

## Materials
+ Raspberry PI Zero WH
+ Waveshare 2.13" e-paper HAT

## Installation

### Raspberry Pi OS Lite

We'll be using the smallest version of Raspberry Pi OS we can, setting up SSH and connecting it to the local wireless network.

<details open><summary><b>Hide/Show Instructions</b></summary>
  
  1.  Use the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to flash Raspberry Pi OS Lite onto the PI Zero's SD card.
  2.  Open the `boot` folder and create a new file named `ssh`. This will automatically enable SSH.
  3.  In the `boot` folder, create a new file named `wpa_supplicant.conf`. Edit the file and add the following:
      ```
      country=<ENTER TWO-LETTER COUNTRY CODE>
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
      update_config=1

      network={
      ssid="NETWORK-NAME"
      psk="NETWORK-PASSWORD"
      }
      ```

  4.  Connect the PI Zero to power, it's time to SSH into it. You can do this using PowerShell with the `ssh` command:
      ```
      ssh pi@raspberrypi
      ```
      Once in, we'll change some system settings through the build in config menu:
      ```
      sudo raspi-config
      ```
      We will need to
        + Change the default password
        + Change the default hostname
        + Change the timezone
        + Enable SPI

      This will require a reboot once completed.
      After that, we'll go through the regular housekeeping after install:
      
      ```
      sudo apt-get update
      sudo apt-get upgrade
      sudo reboot
      ```
      
      That marks the Pi Zero ready to be worked on!
  
</details>

### Install Modules & More

We'll need to install a couple things in order to get the project working.

<details open><summary><b>Hide/Show Instructions</b></summary>
  
  1.  Install Python Libraries
  
      ```
      sudo apt install python3-pip
      sudo pip3 install Pillow (DO I NEED THIS?)
      sduo pip3 install RPI.GPIO
      sudo pip3 install spidev
      ```
      
  2.  Install git & more
  
      ```
      sudo apt-get install git
      sudo apt-get install python3-pil
      sudo apt-get install python3-numpy
      sudo apt-get install libopenjp2-7
      ```
  
</details>

### Clone This Repo

<details show><summary><b>Hide/Show Instructions</b></summary>
  
</details>
