''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

    The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

    Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

# imports
import schedule
import time

# variable to determine scheduled time, I set it at 15 min b4 EOD incase errors happen
sendTime = "17:45"

# Function to get reports 
def getReports():

    import ftplib
    import os
    import shutil
    import datetime

    dirPath = (r"C:\Users\jchap\Desktop\Life\KreativStorm\Assignments\Week 4\Test Directory")
    localServerPath = (r"C:\Users\jchap\Desktop\Life\KreativStorm\Assignments\Week 4\LocalServer" + "\\" + str(datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y")))
    ftpToLocalLog = []
    localToNetworkLog = []

    # get list of local files, create the directory if it does not exist
    print("Initialise Local Directory")
    try:
        if os.path.exists(dirPath):
            localFileList = os.listdir(dirPath)
        else:
            os.makedirs(dirPath)
            localFileList = os.listdir(dirPath)
            # Create Log Files
            ftp = open(dirPath + "\\FTP TO LOCAL Log.txt","x")
            ftp.close()
            local = open(dirPath + "\\LOCAL TO NETWORK Log.txt","x")
            local.close()
    except Exception as e:
        print(e)


    # declare FTP Variables
    ftpHost = "ftp.otenet.gr"
    ftpPort = 21
    ftpUserName = "speedtest"
    ftpPassword = "speedtest"


    # connect to ftp server to get file list
    try:

        ftpClient = ftplib.FTP(timeout=30)
        ftpClient.set_pasv(False)

        print("Connecting to FTP Server")
        ftpClient.connect(ftpHost,ftpPort)
        ftpClient.login(ftpUserName, ftpPassword)

        print("Getting File List")
        ftpFileList = ftpClient.nlst()

        #compare contents of local librarty to ftp server and get list of missing files
    
        missingFileList = set(ftpFileList).difference(localFileList)

        #download missing files from ftp, record log

        print("Downloading missing files")
        for fileName in missingFileList:
            with open(dirPath + f"\\{fileName}", "wb") as file:
                retCode = ftpClient.retrbinary(f"RETR {fileName}", file.write)
            if retCode.startswith("226"):
                ftpToLocalLog.append(f"Successfully downloaded {fileName}")
            else:
                ftpToLocalLog.append(f"Failed to downloaded {fileName} error code : {retcode}")

    # Close connection
        ftpClient.quit()
    except Exception as e:
        print(e)

    print("Writing FTP TO LOCAL Log")
    try:
        with open(dirPath + "\\FTP TO LOCAL Log.txt", 'w') as logFile:
            for log in ftpToLocalLog:
                logFile.write(str(log) + "\n")
    except Exception as e:
        print(e)
        
    try:
        print("Moving Files to local Server")
        shutil.move(dirPath,localServerPath)
        localToNetworkLog.append("Files successfully moved to local network")
        print("Writing LOCAL TO NETWORK Log")
        with open(localServerPath + "\\LOCAL TO NETWORK Log.txt", 'w') as logFile:
            for log in localToNetworkLog:
                logFile.write(str(log) + "\n")
    except Exception as e:
        print(e)

    return schedule.CancelJob # terminate scheduling once all emails are sent and Log file is populated


#run function at scheduled time 
schedule.every().day.at(str(sendTime)).do(getReports)

# loop to check for scheduled time terminate
while True:
    schedule.run_pending()
    if not schedule.jobs: 
        break # once return statement of "sendReports" is hit it will trigger the break 
    time.sleep(1)