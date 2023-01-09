import sqlite3

conn = sqlite3.connect('MiCLoudPrivada')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS usuariosFTP (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    permisos TEXT NOT NULL,
    carpeta TEXT) """)

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

c.execute("INSERT INTO usuariosFTP (usuario, contraseña, permisos, carpeta) VALUES ('Hernani', '00000', 'elradfmwMT', '')")

c.execute("INSERT INTO usuariosFTP (usuario, contraseña, permisos, carpeta) VALUES ('Prueba1', '00000', 'elradfmwMT', '')")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, permisos, carpeta) VALUES ('Prueba2', '00000', 'elradfmwMT', '')")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, permisos, carpeta) VALUES ('Prueba3', '00000', 'elradfmwMT', '')")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, permisos, carpeta) VALUES ('Prueba4', '00000', 'elradfmwMT', '')")
c.execute("INSERT INTO usuariosFTP (usuario, contraseña, permisos, carpeta) VALUES ('Prueba5', '00000', 'elradfmwMT', '')")

conn.commit()

c.execute("SELECT * FROM usuariosFTP")

usuariosExistentes = c.fetchall()
print(usuariosExistentes)

conn.close()