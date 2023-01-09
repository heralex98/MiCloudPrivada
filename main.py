import os
import sqlite3
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

conn = sqlite3.connect('MiCLoudPrivada')
c = conn.cursor()



def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user

    c.execute("SELECT id FROM usuariosFTP")
    i = c.fetchall()
    cont = 0

    for n in i:
        c.execute("SELECT usuario FROM usuariosFTP")
        usuarioAUX = c.fetchall()
        usuario = listToString(usuarioAUX[cont])
        print(usuario)

        c.execute("SELECT contraseña FROM usuariosFTP")
        passwordAUX = c.fetchall()
        password = listToString(passwordAUX[cont])
        print(password)

        c.execute("SELECT permisos FROM usuariosFTP")
        permisosAUX = c.fetchall()
        permisos = listToString(permisosAUX[cont])
        print(permisos)

        authorizer.add_user(usuario, password, './Almacenamiento/'+usuario, perm=permisos)
        print(n)
        cont = cont+1

    authorizer.add_user('admin1', 'admin1', './Almacenamiento', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())


    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 5000)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


if __name__ == '__main__':
    main()
    crearCarpeta()