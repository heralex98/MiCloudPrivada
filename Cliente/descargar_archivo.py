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



archivo = 'horario.xlsx'
ubicacion_descarga = './archivos_de_prueba/horario.xlsx'



def descargar_archivo_ftp(archivo_descarga, ubicacion):

    with open(ubicacion, 'wb') as local_file:
        ftp.retrbinary('RETR ' + archivo_descarga, local_file.write)



descargar_archivo_ftp(archivo, ubicacion_descarga)