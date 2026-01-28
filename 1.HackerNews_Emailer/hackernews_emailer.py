import requests # http requests

from bs4 import BeautifulSoup # html parsing web scarping
import smtplib # email sending

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# system data and time manipulation
import datetime

now=datetime.datetime.now()

# email content placeholder
content=''

# extracting Hacker News Stories
def extract_news(url):
    print("Extracting Hacker News Stories...")

    cnt=''
    cnt+=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')

    try:
        response=requests.get(url,timeout=10)
        content=response.content
        soup=BeautifulSoup(content,'html.parser')

        for i,story in enumerate(soup.find_all('span',attrs={'class':'titleline'})):
            link_tag=story.find('a')
            if link_tag:
                cnt+=f"{i+1} :: <a href='{link_tag['href']}'>{link_tag.text}</a>\n<br>"
        return (cnt)  
    
    except Exception as e:
        print("Error:",e)
        return ("<b>Error in extracting news stories</b><br>")


# Prepare Content
cnt=extract_news('https://news.ycombinator.com/')
content+=cnt
content+='<br>------<br>'
content+='<br><br>End of Message'


# Configuration
SERVER='smtp.gmail.com' # "your smtp server"
PORT=587 # your port number
FROM='12pr.chauhan@gmail.com' # "your from email id"
TO='12pr.chauhan@gmail.com' # "your to email ids" # can be a list
PASS='vzao xlzb bsjv pspc'.replace(" ", "") # "your app password"


# Compose Email
print("Composing Email...")
msg=MIMEMultipart()
msg['Subject']='Top News Stories HN [Automated Email]'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From']=FROM
msg['TO']=TO
msg.attach(MIMEText(content,'html'))


# Send Email
try:
     print("Connecting to Server...")
     server=smtplib.SMTP(SERVER,PORT)
     server.set_debuglevel(1)
     server.ehlo()
     server.starttls()
     server.login(FROM,PASS)
     server.sendmail(FROM,TO,msg.as_string())
     server.quit()
     print("Email Sent...")

except Exception as e:
     print("Error:",e)



