import ftplib
import os

filename = "micTest.wav"
ftp = ftplib.FTP()
ftp.connect("tndusdl73.cafe24.com", 21)    #Ftp 주소 Connect(주소 , 포트)
ftp.login("tndusdl73", "qlalf357")         #login (ID, Password)
ftp.cwd("/www/tndus")   #파일 전송할 Ftp 주소 (받을 주소)
os.chdir(r"/home/pi") #파일 전송 대상의 주소(보내는 주소)
myfile = open(filename, 'rb')       #Open( ~ ,'r') <= Text파일은 됨, Open( ~ ,'rb') <= 이미지파일 됨
ftp.storbinary('STOR ' + filename, myfile)
myfile.close()
ftp.close()