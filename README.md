# junk's COMBO MAKER

The COMBO MAKER is a small every day calandar counter for your desktop, inspired by the likes of Simone Giertz's [Everyday Calendar](https://www.youtube.com/watch?v=-lpvy-xkSNA).

## Materials
+ Raspberry PI Zero WH
+ Waveshare 2.13" e-paper HAT

## Installation

### Raspberry Pi OS Lite

We'll be using the smallest version of Raspberry Pi OS we can, setting up SSH and connecting it to the local wireless network.

<details><summary><b>Show Instructions</b></summary>
  
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

<details><summary><b>Show Instructions</b></summary>
  
</details>

### Clone This Repo

<details><summary><b>Show Instructions</b></summary>
  
</details>
