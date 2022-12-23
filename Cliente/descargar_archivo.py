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

with open('./archivos_de_prueba/local_test.txt', 'w') as local_file:  # Open local file for writing
    # Download `test.txt` from server and write to `local_file`
    # Pass absolute or relative path
    response = ftp.retrlines('RETR test.txt', local_file.write)

    # Check the response code
    # https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes
    if response.startswith('226'):  # Transfer complete
        print('Transfer complete')
    else:
        print('Error transferring. Local file may be incomplete or corrupt.')
