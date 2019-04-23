import json
import os 
import time
import smtplib
gmail_user = 'gmailaccount@gmail.com'
gmail_password = 'password'
sent_from = gmail_user
to = ['yourgmail@gmail.com']
subject = 'Important email about server IP'
nmsg=""
ipd=0
while(1):
	try:
		os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
		with open('tunnels.json') as data_file:
    			datajson = json.load(data_file)
		for i in datajson['tunnels']:
  			msg = i['public_url'] +'\n'
		print (msg)
		ipd=1
		time.sleep(5)
		if msg != nmsg:
			print("changed ip")
			nmsg=msg
			body =msg
			email_text = """\
			From: %s
			To: %s
			Subject: %s

			%s
			""" % (sent_from, ", ".join(to), subject, body)

			try:
    				server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    				server.ehlo()
    				server.login(gmail_user, gmail_password)
    				server.sendmail(sent_from, to, email_text)
    				server.close()
    				print ('Email sent!')
			except:
    				print ('Something went wrong...')
		else:
			print("ok")
	except:
		if ipd==1:
                        body = 'your ip is down'

                        email_text = """\
                        From: %s  
                        To: %s  
                        Subject: %s

                        %s
                        """ % (sent_from, ", ".join(to), subject, body)

                        try:  
                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                server.ehlo()
                                server.login(gmail_user, gmail_password)
                                server.sendmail(sent_from, to, email_text)
                                server.close()
                                print ('Email sent!')
				ipd=0
                        except:
                                print ('Something went wrong...')
		print("ip down")
		time.sleep(5)
