if you want to access **ssh** anywhere without static IP or port forwarding follow this tutorial

*This tutorial has been tested with OrangePi Lite*

# Tutorial

## 1:Download and install ngrok

  *there are many ways to do that you can google ngrok and download it for your system.
  in this method we are going to download ngrok for Linux_ARM systems like rpi or opi*
  
  open your terminal and type "sudo su" then type your password to access root
  
  #### download and unzip ngrok:
      wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip 
      unzip ngrok-stable-linux-arm.zip
      
  #### move ngrok to /usr/local/bin:
      mv ngrok /usr/local/bin/ngrok
  #### ngrok Tunnel Authtoken:
   visit and signup below then youcan get your Authtoken:
   
          https://dashboard.ngrok.com/user/signup
          
   type your Authtoken in terminal:
   
          ./ngrok authtoken **************************************
          
## 2:Run the code for Free plan!
   
   if you have ngrok free plan then when you reboot your system the ssh ports will change so we are going to write a code to sent a gmail to our account when the port changes.
   
   #### turn on Less secure app access for gmail account:
   go to: google account > security > Less secure app access > turn on
       
   #### run Gmail.py :
   download gmail.py:
   
        https://github.com/Farzin-Abdi/Linux/blob/master/ssh_with_ngrok/gmail.py
   
   change lines below with sudo nanu gmail.py :
   
        gmail_user = 'gmailaccount@gmail.com'
        gmail_password = 'password'
        to = ['yourgmail@gmail.com']
        
   #### run ssh.py :
   download ssh.py and run the python code
   
        https://github.com/Farzin-Abdi/Linux/blob/master/ssh_with_ngrok/ssh.py
        
        python ssh.py
        
  ## 3:SSH to your system!
   if everything works then gmail.py will sent an email to you to acces ssh
   open terminal and type the ssh parameters from email:
   
        ssh username@0.tcp.ngrok.io -p <port>
 
  ## 4:autorun the python codes:
we want to autostart ssh.py file, open terminal and type:
  
        sudo nano /lib/systemd/system/sship.service
        
add lines below and change /home/path/ssh.py to your ssh.py directory:
  
        [Unit]
        Description=My Script Service
        After=multi-user.target

        [Service]
        Type=idle
        ExecStart=/usr/bin/python /home/path/ssh.py

        [Install]
        WantedBy=multi-user.target
save it with ctrl+x and exit

and also for autostart gmail.py file create a service:

        sudo nano /lib/systemd/system/gmail.service
        
add lines below and change /home/path/gmail.py to your gmail.py directory:
  
        [Unit]
        Description=My Script Service
        After=multi-user.target

        [Service]
        Type=idle
        ExecStart=/usr/bin/python /home/path/gmail.py

        [Install]
        WantedBy=multi-user.target
  save it with ctrl+x and exit
  
  now we want to enable services:
     
     sudo systemctl daemon-reload
     sudo systemctl enable ssh.service
     sudo systemctl enable gmail.service
     sudo reboot
        
        
 **Now whenever you reboot your system the gmail.py will send you the new ip for ssh login**
