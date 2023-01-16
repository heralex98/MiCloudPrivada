import sqlite3

conn = sqlite3.connect('MiCLoudPrivada')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS usuariosFTP (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    carpeta TEXT NOT NULL,
    permisos TEXT NOT NULL,
    almacenamiento INTEGER) """)

# los permisos son:
# permisos de lectura:
# e = cambiar directorio
# l = lista de archivos
# r = recuperar archivo o ver archivo
#
# permisos de escritura:
# a = agregar datos o archivos.
# d = borrar archivo o carpeta
# f = renombrar archivo o carpeta
# m = crear directorio
# w = almacenar un archivo en el servidor
# M = cambiar el mode o los permisos del archivo
# T = cambiar la fecha de modificacion

c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Hernani', '00000', './Almacenamiento/Hernani', 'elradfmwMT', 0)")

c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Prueba1', '00000', './Almacenamiento/Prueba1', 'elradfmwMT', 0)")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Prueba2', '00000', './Almacenamiento/Prueba2', 'elradfmwMT', 0)")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Prueba3', '00000', './Almacenamiento/Prueba3', 'elradfmwMT', 0)")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Prueba4', '00000', './Almacenamiento/Prueba4', 'elradfmwMT', 0)")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Prueba5', '00000', './Almacenamiento/Prueba5', 'elradfmwMT', 0)")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, carpeta, permisos, almacenamiento) VALUES ('Prueba6', '00000', './Almacenamiento/Prueba6', 'elradfmwMT', 5)")


conn.commit()

c.execute("SELECT * FROM usuariosFTP")

usuariosExistentes = c.fetchall()
print(usuariosExistentes)

conn.close()