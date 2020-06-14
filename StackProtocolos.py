from tkinter import *
from tkinter import messagebox
import socket
import os
import time
import threading

class CapaAplicacion():
    mensaje = ""
    host = ""
    puerto = 4440
    modo = ""
    flag = False
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
        
        
    def VentanaCliente(self, _window):
        _window.destroy()
        window = Tk()
        window.title("Cliente")
        window.geometry("900x400+300+300")
        
      
        label1 = Label(window, text = "")
        label1.grid(row = 1, column = 1)
        labelf = Label(window, text = "     ")
        labelf.grid(row = 1, column = 3)
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
        texto.insert(0, "aaa")
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
        
        
        #Botones Figuras
        #Cambiar direccion
        #image = PhotoImage(file = r"Imagenes\Triangulo.png")
        triangulo = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Triangulo.png")
        botonT = Button(window, image = triangulo, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "Triangulo."))
        botonT.grid(row = 5, column = 4)
        
        circulo = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Circulo.png")
        botonC = Button(window, image = circulo, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "circulo."))
        botonC.grid(row = 5, column = 5)
        
        cuadrado = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Cuadrado.png")
        botonCu = Button(window, image = cuadrado, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "cuadrado."))
        botonCu.grid(row = 5, column = 6)
        
        rombo = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Rombo.png")
        botonR = Button(window, image = rombo, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "rombo."))
        botonR.grid(row = 5, column = 7)
        
        hexagono = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Hexagono.png")
        botonH = Button(window, image = hexagono, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "hexagono."))
        botonH.grid(row = 5, column = 8)
        
        pentagono = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Pentagono.png")
        botonP = Button(window, image = pentagono, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "pentagono."))
        botonP.grid(row = 6, column = 4)
        
        estrella = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\estrella.png")
        botonE = Button(window, image = estrella, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "estrella."))
        botonE.grid(row = 6, column = 5)
        
        x = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\X.png")
        botonX = Button(window, image = x, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "x."))
        botonX.grid(row = 6, column = 6)
        
        pum = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Pum.png")
        botonPu = Button(window, image = pum, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "pum."))
        botonPu.grid(row = 6, column = 7)
        
        check = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Check.png")
        botonCh = Button(window, image = check, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "check."))
        botonCh.grid(row = 6, column = 8)
        
        window.mainloop()
    def imagSeleccionada(self, window, figura):
        print(figura)
        img = PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\Rombo.png")
        
        label = Label(window, image = img)  
        label.grid(row = 0, column = 1)
        
    def VentanaServidor(self, _window):
        _window.destroy()
        window = Tk()
        window.title("Servidor")
        window.geometry("425x200+300+300")
        
        label = Label(window, text = "Esperando Conexión")
        label.grid(row = 0, column = 0)
        
        CR = CapaRed()
        CR.modo = "servidor"
        CR.host = self.host
        CR.puerto = self.puerto  
        
        t = threading.Thread(target=CR.definirModalidad)
        t.start()
        
        t2 = threading.Thread(target = self.mostrarMensaje, args = (window, CR, ))
        t2.start()
         
        window.mainloop()
        
    def mostrarMensaje(self, window, CR):
        while(True):
                if(CR.mensajeRecibido != ""):
                    label = Label(window, text = "Mensaje recibido: " + CR.mensajeRecibido)
                    label.grid(row = 3, column = 0)
                    CR.mensajeRecibido = ""
                    label = Label(window, text = "Conexión realizada con éxito")
                    label.grid(row = 0, column = 0)
                    
                
    def ObtenerMensaje(self, texto, host_, puerto_):
        
        if(texto == "" or host_ == "" or puerto_ == ""):
            messagebox.showerror(title = "Error", message = "Todos los campos deben llenarse")
        else:        
            self.mensaje = texto
            self.host = host_
            print(host_)
            self.puerto = puerto_   
            print(puerto_)
         
            CR = CapaRed()
            CR.modo = "cliente"
            CR.host = self.host
            CR.puerto = self.puerto
            CR.texto = self.mensaje
            CR.definirModalidad()

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
    msgReceived = False
    
    
    def definirModalidad(self):
        print(self.modo)
        if (self.modo == "cliente"):
            print("If de modalidad cliente")
            self.iniciarCliente()

        if (self.modo == "servidor"):
            print("If de modalidad servidor")
            self.iniciarServidor()

    def iniciarCliente(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.host, 4440)
        print('connecting to {} port {}'.format(*server_address))
        
        try:
            sock.connect(server_address)
            # Send data
            message = self.texto.encode()
            print(self.texto)
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)
            
            messagebox.showinfo(title = None, message = "El mensaje ha sido enviado")
            
        except ConnectionRefusedError:
            messagebox.showerror(title = "Error", message = "El mensaje no ha sido enviado")
            
        finally:
            print('closing socket')
            sock.close()
        
    def iniciarServidor(self):
        
        self.msgReceived = False
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

                data = connection.recv(168)
                self.mensajeRecibido = data.decode()

            finally:
                # Clean up the connection
                connection.close()
        
        
 
#############main###############
CA = CapaAplicacion()
CA.graf()
CP = CapaPresentacion
CP.mensaje = CA.mensaje


    









