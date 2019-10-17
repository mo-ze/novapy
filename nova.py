from bs4 import BeautifulSoup
import requests
import config
import sendemail


 


##      get everything 
source = requests.get(config.target_url).text
##      get the source code
soup = BeautifulSoup(source,"html.parser")
##      get note from thehtml
note = soup.find(class_= config.divid).get_text()


if "alo" in note:
        print('closed')
                
else:
        sendemail.send_email(sendemail.subject, sendemail.msg)
    




