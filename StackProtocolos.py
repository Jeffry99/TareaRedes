from tkinter import *

cadenaTexto = ""

class CapaAplicacion():
    mensaje = ""
    
    def ObtenerMensaje(self, texto):
        print(texto)
        self.mensaje = texto
        
    def graf(self): 
        #Ventana
        window = Tk()
        window.title("Stack de Protocolos")
        window.geometry("700x500")

        #Label 1
        label = Label(window, text = "Digite el mensaje que desea enviar:")
        label.grid(row = 1, column = 0)

        #Textbox
        texto = Entry(window, width = 60)
        texto.grid(row = 1, column = 1)


        #Boton
        botonAceptar = Button(window, text = "Aceptar", command = lambda: self.ObtenerMensaje(texto.get()))
        botonAceptar.grid(row = 1, column = 5)

         
        
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
        
#############main##############
CA = CapaAplicacion()
CA.graf()
CP = CapaPresentacion
CP.mensaje = CA.mensaje


    









