from ftplib import FTP, all_errors

host = '192.168.0.101'
port = 5000
user = 'user'
password = '12345'
ftp = FTP()
ftp.connect(host, port)
ftp.login(user, password)
print(ftp.getwelcome())
print(ftp.cwd(user))

try:
    ftp.delete('test.txt')
except all_errors as error:
    print(f'Error deleting file: {error}')