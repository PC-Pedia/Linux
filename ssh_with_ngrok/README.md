if you want to access **ssh** anywhere without static IP or port forwarding follow this tutorial

*This tutorial has been tested with OrangePi Lite*

###### Tutorial

### 1:Download and install ngrok

  *there are many ways to do that you can google ngrok and download it for your system.
  in this method we are going to download ngrok for Linux_ARM systems like rpi or opi*
  
  open your terminal and type "sudo su" then type your password to access root
  
  download and unzip ngrok:\n
      wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip 
      unzip ngrok-stable-linux-arm.zip
      
  move ngrok to /usr/local/bin:
      mv ngrok /usr/local/bin/ngrok
