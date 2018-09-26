import ftplib
import os

filename = "micTest.wav"
ftp = ftplib.FTP()
ftp.connect("tndusdl73.cafe24.com",21)
ftp.login("tndusdl73","qlalf357")
ftp.cwd("/www/tndus")
fd = open("/home/pi/" + filename,'wb')
ftp.retrbinary("RETR " + filename, fd.write)
fd.close()