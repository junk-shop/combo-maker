# junk's COMBO MAKER

The COMBO MAKER is a small every day calandar counter for your desktop, inspired by the likes of Simone Giertz's [Everyday Calendar](https://www.youtube.com/watch?v=-lpvy-xkSNA).

![combo-maker](combo-maker.jpg)

## Materials
+ Raspberry PI Zero WH
+ Waveshare 2.13" e-paper HAT
+ Right Angle 40-Pin Header for Raspberry Pi

## Assembly
(TODO:  UPDATE WITH PICURES)

1. Print the enclosure
2. Attach the right angle header to the Raspberry Pi
3. Attach the e-paper display to the header
4. Place the display face down on a flat surface and carefully bend the right angle pins to a 60 degree angle


## Installation

### Raspberry Pi OS Lite

We'll be using the smallest version of Raspberry Pi OS we can, setting up SSH and connecting it to the local wireless network.

<details open><summary><b>Hide/Show Instructions</b></summary>
  
  1.  Use the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to flash Raspberry Pi OS Lite onto the PI Zero's SD card.
  2.  Open the `boot` folder and create a new file named `ssh`. This will automatically enable SSH.
      + To do this on Windows, I right click > New > Text Document and remove the file extension when renaming.
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
      NOTE: If you're anything like me, you may screw things up by this point and want to start over. In case you've SHH'd into your Pi already, you may be presented with a screen saying `WARNING: POSSIBLE DNS SPOOFING DETECTED!`. To fix this, you can run the following line in PowerShell, of course replacing `hostname` with whichever hostname you entered, or `raspberrypi` for the default:
      
      ```
      ssh-keygen -R hostname
      ```
      
      The default password for the `pi` user is `raspberry`.
      You may get a warning about permanently adding the PI to your hosts file, type `yes` when prompted.
      Once in, we'll change some system settings through the build in config menu:
      ```
      sudo raspi-config
      ```
      We will need to
        + Update Configuration Tool
          + Update
        + Change the default password
          + System Options > Password
        + Change the default hostname
          + System Options > Hostname
        + Enable SPI
          + Interface Options > SPI > Yes
        + Change the timezone
          + Localisation Options > Timezone

      Select `Finish`, this will require a reboot once completed It should prompt you, if not just do it yourself silly.
      Note: You'll want to use the new hostname and password you entered to SSH into your PI.
      After that, we'll go through the regular housekeeping after install:
      
      ```
      sudo apt-get update && sudo apt-get upgrade && sudo reboot
      ```
      
      That marks the Pi Zero ready to be worked on!
  
</details>

### Install Modules & More

We'll need to install a couple things in order to get the project working.

<details open><summary><b>Hide/Show Instructions</b></summary>
  
  1.  Install Python Libraries
  
      ```
      sudo apt install python3-pip
      sudo pip3 install RPI.GPIO spidev flask
      ```
      
  2.  Install git & more
  
      ```
      sudo apt-get install git python3-pil python3-numpy
      ```
  
</details>

### Clone This Repo

<details open><summary><b>Hide/Show Instructions</b></summary>
  
  1.  Change your directory by typing `cd` and pressing enter.
  
  2.  Clone this repo with this command:
  
      ```
      git clone https://github.com/junk-shop/combo-maker/
      ```
      
  3.  Move the folder we need and delete the rest (we really just need a way to clone just the subdirectory without the extra files, but this will do for now...)
  
      ```
      sudo mv /home/pi/combo-maker/pi-zero-w /home/pi && sudo rm -rv /home/pi/combo-maker
      ```
  
    
</details>

### Schedule Scripts to Run at Boot

<details open><summary><b>Hide/Show Instructions</b></summary>
  
  1.  Edit the `rc.local` file:
  
      ```
      sudo nano /etc/rc.local
      ```
  
  2.  Add the following lines to the end of the file, before `exit 0`:
  
      ```
      sudo python3 /home/pi/pi-zero-w/epaper/PPT.py &
      sudo python3 /home/pi/pi-zero-w/webapp/app.py &
      ```
      
      This will run the calendar check script once at boot, and then start up the web app. The ampersands, `&`, allow the scripts to run while the boot continues in the background. Without them, the Pi will not boot.
      
### DONE!

At this point, your combo-maker is ready! You should be able to connect to the webpage from any device that's connected to the same network, just go to `hostname:5000` in your web browser.

If you run into any issues, submit them! I'd love to improve this project as much as possible! This is a really rough project but with some polish it can be a really nice tool to have in your life.
      
</details>

## Planned Features (at the moment!)

+ One-Script Installation & Configuration
+ Multiple Calendar Support
+ Leap Year Handling
