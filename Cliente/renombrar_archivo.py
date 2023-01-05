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

nombre_original = 'horario.xlsx'
nombre_nuevo = 'prueba.xlsx'
def renombrar_archivo_ftp(archivo,nombre):
        try:
                ftp.rename(archivo, nombre)
        except all_errors as error:
                print(f'Error no se pudo renombrar el archivo: {error}')

renombrar_archivo_ftp(nombre_original,nombre_nuevo)