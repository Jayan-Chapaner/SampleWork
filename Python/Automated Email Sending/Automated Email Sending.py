'''
    You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

    Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. 
'''
# imports
import schedule
import time

# variable to determine scheduled time, I set it at 15 min b4 EOD incase errors happen
sendTime = "22:53"

# function to send mail (necessary for schedule import)

def sendReports():

    # imports
    import smtplib
    import email
    import os

    # path for file directory that contains the mail list and the attachments initialised in function so only in memory when necessary
    directory_path = (r"C:\Users\jchap\Desktop\Life\KreativStorm\Assignments\Week 2\Test Directory")

    # create mailing list then populate it from the Mailing List File,
    # also create a list of attachments from the directory "Attachments"
    # initialised in function so only in memory when necessary
    mailList = []
    mailLog =[]
    attachmentList = os.listdir(directory_path + "\\Attachments")

    # populate mail list with email addresses
    try:
        with open(directory_path + "\\Mailing List.txt", 'r') as mailFile:
            for mail in mailFile.readlines():
                if mail.find("@") != -1:
                    mailList.append(mail.strip())
    except Exception as e:
        print(e)
        
    # loop through mail list creating a message object per email 
    
    for i in mailList:
        try:
            # create smtp object per email
            with smtplib.SMTP('localhost') as smtpObj:
                # innitialise and populate email object
                message = email.message.EmailMessage()
                message["From"] = "jchapaner@gmail.com"
                message["To"] = str(i)
                message["Subject"] = "Report From Jayan's Company, to " + str(message["To"])
                message.set_content("Find the Report for "+str(message["To"])+" from Jayan's Company attached.")
                # add attachment to email
                try:
                    with open(directory_path + "\\Attachments\\"+str(message["To"])+".pdf", 'rb') as content_file:
                        content = content_file.read()
                        message.add_attachment(content, maintype="application", subtype="pdf", filename= "Report for "+str(message["To"]))
                        smtpObj.send_message(message)
                        mailLog.append("Successfully sent email to : " + str(message["To"]))
                        del message # delete msg object after email is sent
                except Exception as e:
                    mailLog.append("Adding attachment to "+str(message["To"])+" failed, Error: "+ str(e)) # exception for adding attachment 
        except Exception as e:
            mailLog.append("Sending email to "+str(message["To"])+" failed, Error: "+ str(e)) # exception for sending mail
    # write log to Mail Log txt file, rewrite everytime mail is sent
    try:
        with open(directory_path + "\\Mail Log.txt", 'w') as logFile:
            for log in mailLog:
                logFile.write(str(log) + "\n")
    except Exception as e:
        print(e)
    return schedule.CancelJob # terminate scheduling once all emails are sent and Log file is populated

# run function at scheduled time 
schedule.every().day.at(str(sendTime)).do(sendReports)

# loop to check for scheduled time terminate
while True:
    schedule.run_pending()
    if not schedule.jobs: 
        break # once return statement of "sendReports" is hit it will trigger the break 
    time.sleep(1)