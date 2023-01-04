from ftplib import FTP

###valores de la conexion###

host = '192.168.0.101'
port = 5000
user = 'user'
password = '12345'
ftp = FTP()
ftp.connect(host, port)
ftp.login(user, password)
print(ftp.getwelcome())
print(ftp.cwd(user))

###valores de la funcion###

archivo = 'horario.xlsx'
ubicacion_archivo = './archivos_de_prueba/horario.xlsx'

###funcion###

def subir_archivo(archivo_a_subir, ubicacion):
    if archivo_a_subir.endswith('.txt'):
        if archivo in ftp.nlst():
            ftp.delete(archivo_a_subir)
            with open(ubicacion, 'rb') as text_file:
                ftp.storlines('STOR ' + archivo_a_subir, text_file)
                print('se subio el archivo correctamente')
        else:
            with open(ubicacion, 'rb') as text_file:
                ftp.storlines('STOR ' + archivo_a_subir, text_file)
                print('se subio el archivo correctamente')
    else:
        if archivo in ftp.nlst():
            ftp.delete(archivo_a_subir)
            with open(ubicacion, 'rb') as image_file:
                ftp.storbinary('STOR ' + archivo_a_subir, image_file)
                print('se subio el archivo correctamente')
        else:
            with open(ubicacion, 'rb') as image_file:
                ftp.storbinary('STOR ' + archivo_a_subir, image_file)
                print('se subio el archivo correctamente')

subir_archivo(archivo, ubicacion_archivo)