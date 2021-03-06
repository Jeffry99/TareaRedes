from tkinter import *
from tkinter import messagebox
import socket
import os
import time
import threading

        

class CapaAplicacion():
    mensaje = ""
    mssg = ""
    host = ""
    puerto = 4440
    modo = ""
    contClick = 0
    listaImagenes = []
    
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
        window.geometry("900x450+300+300")

        frame = Frame(window)
        frame.grid(row = 0, column = 0)
        
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 0)
        
        frame2 = Frame(window)
        frame2.grid(row = 2, column = 0)
        
        frame3 = Frame(window)
        frame3.grid(row = 4, column = 0)
        
        frame4 = Frame(window)
        frame4.grid(row = 3, column = 0)
        
        label4 = Label(frame, text = "Escoja el patrón de figuras que desea enviar:")
        label4.grid(row = 0, column = 0)     

        label8 = Label(frame1, text = "                                                         ")
        label8.grid(row = 0, column = 0)
        label1 = Label(frame1, text = "")
        label1.grid(row = 1, column = 1)
        labelf = Label(frame1, text = "     ")
        labelf.grid(row = 1, column = 3)
        labelf = Label(frame3, text = "     ")
        labelf.grid(row = 0, column = 0)
        label5 = Label(frame1, text = "Host:")
        label5.grid(row = 5, column = 0)
        label6 = Label(frame1, text = "Puerto:")
        label6.grid(row = 6, column = 0)
        
        textoHost = Entry(frame1, width = 30)
        textoHost.grid(row = 5, column = 1)
        #textoHost.insert(0, "")

        textoPuerto = Entry(frame1, width = 30)
        textoPuerto.grid(row = 6, column = 1)
        textoPuerto.insert(0, "4440")

        #Cambiar direccion
        #image = PhotoImage(file = r"Imagenes\Triangulo.png")
        triangulo = PhotoImage(file = r"Imagenes\Triangulo.png")
        botonT = Button(frame1, image = triangulo, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "Triangulo.", frame2, "0"))
        botonT.grid(row = 5, column = 4)
        
        circulo = PhotoImage(file = r"Imagenes\Circulo.png")
        botonC = Button(frame1, image = circulo, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "circulo.", frame2, "1"))
        botonC.grid(row = 5, column = 5)
        
        cuadrado = PhotoImage(file = r"Imagenes\Cuadrado.png")
        botonCu = Button(frame1, image = cuadrado, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "cuadrado.", frame2, "2"))
        botonCu.grid(row = 5, column = 6)
        
        rombo = PhotoImage(file = r"Imagenes\Rombo.png")
        botonR = Button(frame1, image = rombo, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "rombo.", frame2, "3"))
        botonR.grid(row = 5, column = 7)
        
        hexagono = PhotoImage(file = r"Imagenes\Hexagono.png")
        botonH = Button(frame1, image = hexagono, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "hexagono.", frame2, "4"))
        botonH.grid(row = 5, column = 8)
        
        pentagono = PhotoImage(file = r"Imagenes\Pentagono.png")
        botonP = Button(frame1, image = pentagono, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "pentagono.", frame2, "5"))
        botonP.grid(row = 6, column = 4)
        
        estrella = PhotoImage(file = r"Imagenes\estrella.png")
        botonE = Button(frame1, image = estrella, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "estrella.", frame2, "6"))
        botonE.grid(row = 6, column = 5)
        
        x = PhotoImage(file = r"C:Imagenes\X.png")
        botonX = Button(frame1, image = x, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "x.", frame2, "7"))
        botonX.grid(row = 6, column = 6)
        
        pum = PhotoImage(file = r"Imagenes\Pum.png")
        botonPu = Button(frame1, image = pum, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "pum.", frame2, "8"))
        botonPu.grid(row = 6, column = 7)
        
        check = PhotoImage(file = r"Imagenes\Check.png")
        botonCh = Button(frame1, image = check, height = 65, width = 85, command = lambda: self.imagSeleccionada(window, "check.", frame2, "9"))
        botonCh.grid(row = 6, column = 8)
        
        botonBorrar = Button(frame3, text = "Borrar", command = self.borrarImagen, width = 6, height = 1)
        botonBorrar.grid(row = 1, column = 1)
        
        botonAceptar = Button(frame3, text = "Aceptar", command = lambda: self.ObtenerMensaje(self.mssg,textoHost.get(),textoPuerto.get()))
        botonAceptar.grid(row = 1, column = 0)
        
        window.mainloop()
    
    def borrarImagen(self):
        if(len(self.listaImagenes) == 0):
            messagebox.showwarning(title = "Atención", message = "No ha agregado ningúna figura")
        else:    
            self.listaImagenes[-1].grid_forget()
            self.listaImagenes.pop()
            self.contClick = self.contClick - 1
            self.mssg = self.mssg[:-1]
        
    def imagSeleccionada(self, window, figura, frame, cod):
        if(self.contClick < 7):
            img = PhotoImage(file = r"Imagenes\\"+ figura + "png")   
            labelImagen = Label(frame, image = img)
            labelImagen.grid(row = 0, column = self.contClick)
            
            self.mssg += cod
            print(self.mssg)
            self.listaImagenes.append(labelImagen)
            self.contClick = self.contClick + 1
            
        else:  
            messagebox.showwarning(title = "Atención", message = "Puede enviar 7 figuras como máximo")
                
        window.mainloop()

    def VentanaServidor(self, _window):
        _window.destroy()
        window = Tk()
        window.title("Servidor")
        window.geometry("900x450+300+300")
        frame0 = Frame(window)
        frame0.grid(row = 0, column = 0)
        label = Label(frame0, text = "Esperando Conexión")
        label.grid(row = 0, column = 0)
        
        CR = CapaRed()
        CR.modo = "servidor"
        CR.host = self.host
        CR.puerto = self.puerto  
        
        t = threading.Thread(target=CR.definirModalidad)
        t.start()
        
        t2 = threading.Thread(target = self.mostrarMensaje, args = (window, CR, frame0, ))
        t2.start()
         
        window.mainloop()
        
        
        window.mainloop()
    def mostrarMensaje(self, window, CR, frame_):
        CP = CapaPresentacion()
        frame = Frame(window)
        frame.grid(row = 4, column = 0)
        cont = 0
        
        while(True):
                if(CR.mensajeRecibido != ""):
                    CP.mensaje = CR.mensajeRecibido
                    print(CP.decodificar(CP.mensaje))
                    mensajeDecodificado = CP.decodificar(CP.mensaje)
                    label = Label(frame_, text = "Mensaje recibido: " + mensajeDecodificado)
                    label.grid(row = 3, column = 0)
                    CR.mensajeRecibido = ""
                    label = Label(frame_, text = "Conexión realizada con éxito")
                    label.grid(row = 0, column = 0)
                    
                    indice = 0
                    cont = 0
                    while (indice < len(mensajeDecodificado)):
                        letra = mensajeDecodificado[indice]
                        
                 
                        print(letra)

                        if(letra == "0"):
                            figura = "Triangulo"
   
                        if(letra == "1"):
                            figura = "Circulo"
                            
                        if(letra == "2"):
                            figura = "Cuadrado"
         
                        if(letra == "3"):
                            figura = "Rombo"       
                          
                        if(letra == "4"):
                            figura = "Hexagono"
                
                        if(letra == "5"):
                            figura = "Pentagono"
                      
                        if(letra == "6"):
                            figura = "Estrella"
                  
                        if(letra == "7"):
                            figura = "X"
                            
                        if(letra == "8"):
                            figura = "Pum"
                            
                        if(letra == "9"):
                            figura = "Check"
                            
                        #img1 = FitoImage()   
                        #img1.make_fitoImage(figura)
                        #img1 = new PhotoImage(file = r"C:\Users\jeffr\Desktop\Tarea Redes\TareaRedes\Imagenes\\"+ figura + ".png")   
                        #fitoImage = FitoImage(figura, frame, cont)
                        #fitoImage.make_fitoImage(figura, frame, cont)
                        
                        img = PhotoImage(file = r"Imagenes\\"+ figura + ".png") 
                        label = Label(frame, image = img) 
                        label.grid(row = 0, column = cont)
                        
                        time.sleep(1)
                        
                        indice +=1
                        cont += 1
                    
        window.mainloop()
        
    def ObtenerMensaje(self, texto, host_, puerto_):
        
        if(texto == "" or host_ == "" or puerto_ == ""):
            messagebox.showerror(title = "Error", message = "Todos los campos deben llenarse")
        else:        
            self.mensaje = texto
            self.host = host_
            print(host_)
            self.puerto = puerto_   
            print(puerto_)
         
            #enviar a capa de presentacion a codificar
            CP = CapaPresentacion()
            CP.mensaje = self.mensaje
            
            CR = CapaRed()
            CR.texto = CP.codificar(CP.mensaje)
            
            CR.modo = "cliente"
            CR.host = self.host
            CR.puerto = self.puerto
            
            CR.definirModalidad()

class CapaPresentacion():
    mensaje = ""
    
    def codificar(self, msg):
        indice = 0
        cod = ""
        while indice < len(msg):
            
            letra = msg[indice]
            if(letra == "0"):
                cod += "@#"
            elif(letra == "1"):
                cod += "$!"
            elif(letra == "2"):
                cod += "%*"
            elif(letra == "3"):
                cod += "&>"
            elif(letra == "4"):
                cod += "?<"
            elif(letra == "5"):
                cod += ";{"
            elif(letra == "6"):
                cod += ":}"
            elif(letra == "7"):
                cod += "./"
            elif(letra == "8"):
                cod += ".\\"
            elif(letra == "9"):
                cod += "||"
         
            indice += 1
            
        return cod
         
    def decodificar(self, cod):    
    
        indice = 0
        cont=0
        final = ""
        letra = ""
        decod = ""
        
         
        while(indice <= len(cod)):
            if(cont%2 == 0 and cont > 0):
                
                letra = cod[indice-2]
                letra = letra + cod[indice-1]
                
                if(letra == "@#"):
                    decod += "0"
                elif(letra == "$!"):
                    decod += "1"
                elif(letra == "%*"):
                    decod += "2"
                elif(letra == "&>"):
                    decod += "3"
                elif(letra == "?<"):
                    decod += "4"
                elif(letra == ";{"):
                    decod += "5"
                elif(letra == ":}"):
                    decod += "6"
                elif(letra == "./"):
                    decod += "7"
                elif(letra == ".\\"):
                    decod += "8"
                elif(letra == "||"):
                    decod += "9"
                    
            cont += 1 
            indice +=1
        return decod
        
class CapaRed():
    
    host = ""
    puerto = 4440
    texto = ""
    modo = ""
    mensajeRecibido = ""
    
    
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
# CP = CapaPresentacion
# CP.mensaje = CA.mensaje


    









