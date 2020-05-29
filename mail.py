#!/usr/bin/env python
# coding: utf-8

# In[4]:


f= open("/root/tensor/file.txt" ,"r")
a=f.read()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "samsonjac53@gmail.com"
host_pass = "****"
guest_address = "samsonjac53@gmail.com"
subject = "Regarding Success of your model "
content = "congratulations your model trained successfully with"+ str(a)+ "accuracy";
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
