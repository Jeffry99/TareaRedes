from tkinter import *
import socket
import os
import time

cadenaTexto = ""



    
class CapaAplicacion():
    mensaje = ""
    host = ""
    puerto = 4440
    modo = ""

    def VentanaCliente(self, _window):
        _window.destroy()
        window = Tk()
        window.title("Cliente")
        window.geometry("425x200+300+300")
        
      
        label1 = Label(window, text = "")
        label1.grid(row = 1, column = 1)
        label2 = Label(window, text = "")
        label2.grid(row = 2, column = 1)
        label3 = Label(window, text = "")
        label3.grid(row = 3, column = 1)
        label = Label(window, text = "Digite el mensaje que desea enviar:")
        label.grid(row = 4, column = 0)
        label = Label(window, text = "Host:")
        label.grid(row = 5, column = 0)
        label = Label(window, text = "Puerto:")
        label.grid(row = 6, column = 0)
        
        #TextboxMensaje
        texto = Entry(window, width = 30)
        texto.grid(row = 4, column = 1)
        texto.insert(0, "Holiwis")
        #TextboxHost
        textoHost = Entry(window, width = 30)
        textoHost.grid(row = 5, column = 1)
        textoHost.insert(0, "192.168.100.32")
        #TextboxPuerto
        textoPuerto = Entry(window, width = 30)
        textoPuerto.grid(row = 6, column = 1)
        textoPuerto.insert(0, "4440")
        #Boton
        botonAceptar = Button(window, text = "Aceptar", command = lambda: self.ObtenerMensaje(texto.get(),textoHost.get(),textoPuerto.get()))
        botonAceptar.grid(row = 9, column = 1)
               
        window.mainloop
        
        
    def mostrarMensaje(self, _window, CapaRed):
        
        label = Label(_window, text = CapaRed.mensajeRecibido)
        label.grid(row = 3, column = 1)
        
    def VentanaServidor(self, _window):
    
        _window.destroy()
        window = Tk()
        window.title("Servidor")
        window.geometry("425x200+300+300")
        
        CR = CapaRed()
        CR.modo = self.modo
        CR.host = self.host
        CR.puerto = self.puerto
        CR.definirModalidad()
    
        label = Label(window, text = "Mensaje recibido: ")
        label.grid(row = 3, column = 0)
        
        
        window.mainloop
        
    def ObtenerMensaje(self, texto, host_, puerto_):
        print(texto)
        self.mensaje = texto
        self.host = host_
        print(host_)
        self.puerto = puerto_
        print(puerto_)
        
        CR = CapaRed()
        CR.modo = self.modo
        CR.host = self.host
        CR.puerto = self.puerto
        CR.texto = self.mensaje
        CR.definirModalidad()
        
    def graf(self): 
        #Ventana
        window = Tk()
        window.title("Stack de Protocolos")
        window.geometry("425x200+300+300")
        
        #Label 1
        label1 = Label(window, text = "")
        label1.grid(row = 1, column = 1)
        #Label 1
        label2 = Label(window, text = "")
        label2.grid(row = 3, column = 1)
        #Label 1
        label3 = Label(window, text = "")
        label3.grid(row = 4, column = 1)
        #Label 1
        label4 = Label(window, text = "")
        label4.grid(row = 5, column = 1)
        
        #Label 1
        labelCliente = Label(window, text = "           Cliente: Enviar el mensaje           ")
        labelCliente.grid(row = 2, column = 1)
        #Label 1
        labelServidor = Label(window, text = "      Servidor: Recibir el mensaje       ")
        labelServidor.grid(row = 2, column = 4)

        botonCliente = Button(window, text = "Modo Cliente", command = lambda: self.VentanaCliente(window))
        botonCliente.grid(row = 5, column = 1)
        
        botonServidor = Button(window, text = "Modo Servidor", command = lambda: self.VentanaServidor(window))
        botonServidor.grid(row = 5, column = 4)
        window.mainloop()
        
        
     
class CapaPresentacion():
    mensaje = ""
    
    def encriptar(self, msg):
        
        #Variables
         puerto = 44440
         
         host = ""
         i = 0
         j = 0
         d = ""
         b = ""
         c = ''
         contenido = msg
         print("Digite la clave: ")
         
         #limpiar
         d = input()
         print("Digite el host: ")
         #limpiar
         host = input()
         while i<len(contenido):
            c = contenido[i]
            if (ord(c) >= 65 and ord(c) <= 90):
                    c = ord(c) + (ord(d[j])-48)
                    if c > 90:
                            c = c + 64 - 90
            elif ord(c) == 32:
                    c = 126
            b = b + chr(c)
            i = i + 1
            if j<2:
                    j = j+1
            else:
                    j = 0                          
         print(b)
         iniciarCliente(host, puerto, b)

         del host
         del i
         del j
         del d
         del b
         del callable
         
    def desencriptar(mensaje, d):
        i = 0
        j = 0

        b = ""

        c = ''

        contenido = mensaje
        
        while i < len(contenido):
                c = contenido[i]
                if (ord(c) >= 65 and ord(c) <= 90):
                        c = ord(c) - (ord(d[j])-48)
                        if c < 65:
                                c = c - 64 + 90
                elif ord(c) == 126:
                        c = 32
                b = b + chr(c)
                i = i + 1
                if j<2:
                        j = j+1
                else:
                        j = 0
        print (b)
        return b
        
        
        
class CapaRed():
    
    host = ""
    puerto = 4440
    texto = ""
    modo = ""
    mensajeRecibido = ""
    CapaRed = null
    
    def definirModalidad(self):
        if (self.modo == "cliente"):
            print("If de modalidad cliente")
            self.iniciarCliente()

        if (self.modo == "servidor"):
            print("If de modalidad servidor")
            self.iniciarServidor()

    def iniciarCliente(self):
        # print("Cliente inicializado")
        # print("host --> "+ self.host)
        # print("puerto --> "+ self.puerto)
        # print("\n\n")
        
        # c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #objetoSocket 
        # c.connect((self.host,int(self.puerto)))
        # texto = c.recv(1024)
        # #print (texto.decode('utf8'))
        # c.send(texto)
        # c.close()   
        # del c
        
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.host, 4440)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)
        try:

            # Send data
            message = self.texto.encode()
            print(self.texto)
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            # while amount_received < amount_expected:
                # data = sock.recv(16)
                # amount_received += len(data)
                # print('received {!r}'.format(data))

        finally:
            print('closing socket')
            sock.close()
        
    def iniciarServidor(self):
        
        
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (self.host, self.puerto)
        print('starting up on {} port {}'.format(*server_address))
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(5)

        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            try:
                print('connection from', client_address)

                # Receive the data in small chunks and retransmit it
                #while True:
                data = connection.recv(168)
                self.mensajeRecibido = data.decode()
                
                #print('El mensaje recibido es {!r}'.format(data))
                
                # if data:
                    # print('sending data back to the client')
                    # connection.sendall(data)
                # else:
                    # print('no data from', client_address)
                    # break

            finally:
                # Clean up the connection
                connection.close()
        
        
 
#############main###############
CA = CapaAplicacion()
CA.graf()
CP = CapaPresentacion
CP.mensaje = CA.mensaje


    









