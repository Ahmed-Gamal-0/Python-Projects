import smtplib # to deal with SMTP protocol which used to Send Email 

to = input("Enter The Recipent Email:\n")
content = input("Enter The Content of The Email:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
     # type email and password of sender to log in
    server.login('senderEmail@gmail.com', 'senderEmailPassword')
    
    server.sendmail('senderEmail@gmail.com', to, content)
    
    server.close()
    
    

sendEmail()