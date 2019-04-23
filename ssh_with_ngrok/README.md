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
        download Gmail.py and change lines below with sudo nanu Gmail.py :
        gmail_user = 'gmailaccount@gmail.com'
        gmail_password = 'password'
        to = ['yourgmail@gmail.com']
        
   #### run ssh.py :
        download ssh.py and run the python code
        
  ## 3:SSH to your system!
     if everything works then gmail.py will sent an email to you to acces ssh
     open terminal and type the ssh parameters from email:
        ssh username@0.tcp.ngrok.io -p <port>
 
        
 **Now whenever you reboot your system the Gmail.py will send you the new ip for ssh login**
