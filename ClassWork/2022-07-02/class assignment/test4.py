import logging
import vlc
from PyPDF4 import PdfFileMerger
import smtplib
import imaplib
import email
import traceback
import datetime
from skimage import io
import os
from gtts import gTTS
from windows_tools.installed_software import get_installed_software
import smtplib
from playsound import playsound
import socket
logging.basicConfig(filename='log4.log',level=logging.INFO)

class While:
    #q1 : Try to print this by using while loop
    def starsteps(self):
        logging.info('printing star steps')
        i = 1
        while i < 11:
            print('* ' * i)
            i+=1
    #q2 : try to print below by using while loop
    """
    A
    B H 
    C I N
    D J O S
    E K p T W
    F L Q U X z
    G M R V Y 
    """
    def alphasteps(self):
        logging.info('printing alphabets steps')
        alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        i = 0
        lines = 7
        while i < lines:
            print(alphabets[i] + '   ',end='')
            j = 0
            column = i + lines - 1
            while j < i:
                if column < len(alphabets):
                    print(alphabets[column] + '   ',end='')
                    column = column + lines - j - 2
                else:
                    j = i
                j+=1
            else:
                print('\n')
            i+=1

    #q3 : Try to print all the number divisible by 3 in between a range of 40 - 400
    def getnumby3(self,lower,upper):
        logging.info('printing all the number divisible by 3 in between a range')
        e = []
        for i in range(lower,upper,3):
            e.append(i)
        return e
    
    #q4 : Try to filter out all the vowels form below text by using while loop : 
    def filtervowels(self,string):
        logging.info('printing all vowels from string')
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowellist = []
        i = 0
        while i < len(string):
            if string[i] in vowels:
                vowellist.append(string[i])
            i+=1
        print(vowellist)
        
    #q5 : Try to generate all the even number between 1- 1000
    def geteven(self):
        logging.info('printing all teven number between 1- 1000')
        e = []
        for i in range(2,101,2):
            e.append(i)
        return e

    #q6 : Define a function for all the above problem statememnt.

    def q3(self,start,end,divisor):
        logging.info('printing numbers divisible within a range')
        result = []
        for i in range(start, end+1):
            if i%divisor == 0:
                result.append(i)
        return result

    def getvowels(self,string):
        logging.info('printing all vowels from string')
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowellist = []
        i = 0
        while i < len(string):
            if string[i] in vowels:
                vowellist.append(string[i])
            i+=1
        return vowellist

    def even(self,start,end):
        logging.info('printing all teven number between 1- 1000')
        result = []
        for i in range(start, end+1):
            if i%2 == 0:
                result.append(i)
        return result

    #q7 : write a code to get a time of your system
    def gettime(self):
        logging.info('getting current time')
        now = datetime.datetime.now()
        print(now.time())

    #q8 : Write a code to fetch date form your system
    def getdate(self):
        logging.info('getting current date')
        now = datetime.datetime.now()
        print(now.date())


    #q9 : Write a code to send a mail to your friend
    def sendmail(self):
        logging.info('sending email to your friend')
        try: 
            #Create your SMTP session 
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 

        #Use TLS to add security 
            smtp.starttls() 

            #User Authentication 
            smtp.login("ajayatm@gmail.com","*******************")

            #Defining The Message 
            message = "Message_you_need_to_send" 

            #Sending the Email
            smtp.sendmail("ajayatm@gmail.com", "ajayatm@gmail.com",message) 

            #Terminating the session 
            smtp.quit() 
            print ("Email sent successfully!") 

        except Exception as ex: 
            print("Something went wrong....",ex)

    #q10 : write a code to trigger alarm for you at scheduled time
    def triggeralarm(self):
        logging.info('triggering alarm')

        alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

        alarm_hour = alarm_time[0:2]
        alarm_min = alarm_time[3:5]
        alarm_sec = alarm_time[6:8]
        alarm_period = alarm_time[9:].upper()

        while True:
            now = datetime.datetime.now()

            current_hour = now.strftime("%I")
            current_min = now.strftime("%M")
            current_sec = now.strftime("%S")
            current_period = now.strftime("%p")

            if alarm_period == current_period:
                if alarm_hour == current_hour:
                    if alarm_min == current_min:
                        if alarm_sec == current_sec:
                            playsound('D:/Ajay/Education/Jupyter Notebook/FSDS/FSDS May 2022/Class Assignments/Alarm05.wav')
                            break

    #q11 : write a code to check ip address of your system
    def checkip(self):
        logging.info('getting ip address')
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])

    #q12 : Write a code to check a perticular installation in your system
    def getsoftware(self):
        for software in get_installed_software():
            print(software['name'], software['version'], software['publisher'])

    #q13 : Write a code to convert any text in to voice
    def texttovoice(self):
        logging.info('converting text to voice')
        text = 'Welcome to FSDS!'
        voice = gTTS(text=text, lang='en', slow=False)
        voice.save("texttovoice.mp3")
        print('Text converted to voice')

    #q14 : you have to write a fun which will take string and return a len of it without using a inbuilt fun len
    def stringlength(self, string):
        logging.info('getting length of a string')
        if type(string) is str:
            i = 0
            for k in string:
                i+=1
            result = "The length of string is " + str(i)
        else:
            result = "Invalid input"
        return result

    #q15 :write a fun which will be able to print an index of all premitive element which you will pass
    def primIndex(self,l):
        logging.info('getting index of primitives')
        types = ['int', 'float', 'str', 'bool']
        result = []
        if type(l) is list:
            for i in range(len(l)):
                if type(l[i]) is int or type(l[i]) is float or type(l[i]) is str or type(l[i]) is bool:
                    result.append(i)
        else:
            result = 'Invalid input'
        return result       

    #q16 : Write a fun which will take input as a dict and give me out as a list of all the values 
    #even in case of 2 level nesting it should work .

    def dictvalues(self,d):
        logging.info('getting all values from dictionary')
        dvalues = []
        if type(d) is dict:
            for i in d:
                if type(d[i]) is dict:
                    for j in d[i]:
                        dvalues.append(d[i][j])
                else:
                    dvalues.append(d[i])
            result = dvalues
        else:
            result = 'Invalid input'
        return result

    #q17 : write a function whihc will take multiple list as a input and give me concatnation of all the element 
    #as and output
    def conclists(self,*args):
        logging.info('joining lists')
        combinedlist = []
        for x in args:
            if type(x) is list:
                for y in x:
                    combinedlist.append(y)
        return combinedlist
    
    #q18 : Write a function which will whould return list of all the file name from a directory.
    def listfiles(self,directory):
        logging.info('getting list of all the file name from a directory')
        os.chdir(directory)
        l1 = []
        l = os.listdir()
        for i in l:
            if i.count('.',1) == 1:
                l1.append(i)
        return l1

    #q19 : write a function whihc will be able to read a image file and show it to you.

    def seeimage(self,image):
        logging.info('reading an image and displaying')

        img = io.imread(image)
        io.imshow(image)
        print('Did you see image?')

    #q20 : write a function by which you will be able to append two PDF files.

    def mergePDF(self,i1,i2,i3):
        logging.info('appending two PDF files')
        merger = PdfFileMerger()
        pdf_files = [i1, i2]
        for x in pdf_files:
            print(x)
            merger.append(fileobj=open(x, 'rb'))
        merger.write(fileobj=open(i3, 'wb'))
        merger.close()
        return 'Success'

    #q21 : write a function which can help you to filter only word file from a directory.

    def listword(self,directory):
        logging.info('filter one word from dictionary')
        os.chdir(directory)
        l1 = []
        l = os.listdir()
        for i in l:
            if i.count('.doc') == 1:
                l1.append(i)
        return l1

    #q22 : write a function which can read video file and play for you .

    def playvideo(self,file):
        logging.info('reading video and playing')
        video = vlc.MediaPlayer(file)
        video.play()

    #q23 : write a function which will be able to shutdonw your system .

    def shutdown(self):
        logging.info('shutting down system')
        os.system('shutdown -s')

    #q24 : Write a function which will whould return list of all the file name from a directory .

    def listfiles(self,directory):
        logging.info('getting files from dictionary')
        os.chdir(directory)
        l1 = []
        l = os.listdir()
        for i in l:
            if i.count('.',1) == 1:
                l1.append(i)
        return l1

    #q25 : write a function whihc will be able to access your mail.

    def readgmail(self,password):
        logging.info('trying to access your email')
        # -------------------------------------------------
        #
        # Utility to read email from Gmail Using Python
        #
        # ------------------------------------------------
        ORG_EMAIL = "@gmail.com" 
        FROM_EMAIL = "ajayatm" + ORG_EMAIL 
        FROM_PWD = password 
        SMTP_SERVER = "imap.gmail.com" 
        SMTP_PORT = 993

        def read_email_from_gmail():
            try:
                mail = imaplib.IMAP4_SSL(SMTP_SERVER)
                mail.login(FROM_EMAIL,FROM_PWD)
                mail.select('inbox')

                data = mail.search(None, 'ALL')
                mail_ids = data[1]
                id_list = mail_ids[0].split()   
                first_email_id = int(id_list[0])
                latest_email_id = int(id_list[-1])

                for i in range(latest_email_id,first_email_id, -1):
                    data = mail.fetch(str(i), '(RFC822)' )
                    for response_part in data:
                        arr = response_part[0]
                        if isinstance(arr, tuple):
                            msg = email.message_from_string(str(arr[1],'utf-8'))
                            email_subject = msg['subject']
                            email_from = msg['from']
                            print('From : ' + email_from + '\n')
                            print('Subject : ' + email_subject + '\n')

            except Exception as e:
                print(e)

        read_email_from_gmail()

try:
    whileobject = While()
    logging.info('creating while class object')
    whileobject.starsteps()
    d = {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8}
    l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
    videofile = 'D:\desktop\V_20170415_224817.mp4'
    whileobject.alphasteps()
    print(whileobject.getnumby3(10,100))
    string = 'Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation'
    whileobject.filtervowels(string)
    print(whileobject.geteven())
    print(whileobject.q3(1,2000,37))
    print(whileobject.getvowels(string))
    print(whileobject.even(30,58))
    whileobject.gettime()   #--- 7
    whileobject.getdate()
    whileobject.sendmail()
    #whileobject.triggeralarm() #---  10
    whileobject.checkip()
    whileobject.getsoftware()
    whileobject.texttovoice()
    print(whileobject.stringlength(string))
    k = [1,2,3,4, ["ineuron","data science"]]
    print(whileobject.primIndex(k))
    print(whileobject.dictvalues(d))    #16
    print(whileobject.conclists([1,2,3,4], ["ineuron","data science"]))
    print(whileobject.listfiles('D:\Ajay'))
    #whileobject.seeimage('D:\Ajay\Sagini\Sagini OHIP back.jpeg')
    print(whileobject.mergePDF('D:\Ajay\Driver license.pdf','D:\Ajay\Driver license.pdf','merged.pdf'))
    print(whileobject.listword('D:\Ajay'))
    whileobject.playvideo(videofile)
    print(whileobject.listfiles('D:\Ajay'))
    whileobject.readgmail('*******************')
except Exception as e:
    logging.critical(e)
    print(e)

    