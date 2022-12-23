from ftplib import FTP

host = '192.168.0.101'
port = 5000
user = 'user'
password = '12345'
ftp = FTP()
ftp.connect(host, port)
ftp.login(user, password)
print(ftp.getwelcome())
print(ftp.cwd(user))

if 'test.txt' in ftp.nlst():
    ftp.delete('test.txt')
    with open('./archivos_de_prueba/test.txt', 'rb') as text_file:
        ftp.storlines('STOR test.txt', text_file)
else:
    with open('./archivos_de_prueba/test.txt', 'rb') as text_file:
        ftp.storlines('STOR test.txt', text_file)


