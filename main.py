import serial
import time

puerto_serial = serial.Serial('COM3', 9600, timeout=1)

def enviar_comando_at(comando, espera):
    puerto_serial.write((comando + '\r\n').encode())
    time.sleep(espera)
    respuesta = puerto_serial.read_all().decode().strip()
    return respuesta

def enviar_mensaje(numero, mensaje):
    enviar_comando_at("AT+CMGF=1", 0.2)  # Configurar el módulo para el modo de texto
    enviar_comando_at('AT+CMGS="{}"'.format(numero), 0.2)
    time.sleep(1)
    enviar_comando_at(mensaje + chr(26), 0.2)  # Envío del mensaje y Ctrl+Z para terminar

def leer_mensajes():
    mensajes = []
    respuesta = enviar_comando_at("AT+CMGF=1", 0.25)  # Configurar el módulo para el modo de texto
    if "OK" in respuesta:
        for i in range(1, 10):  # Recorrer los primeros 20 mensajes
            respuesta = enviar_comando_at("AT+CMGR={}".format(i), 0.25)  # Leer cada mensaje individualmente
            if "+CMGR:" in respuesta:  # Si se encuentra un mensaje
                #print("comand: ", "AT+CMGR={}".format(i) ," resp:" , respuesta)
                mensajes.append(respuesta)
    return mensajes

def leer_all_mensajes():
    mensajes = "error"
    respuesta = enviar_comando_at("AT+CMGF=1", 0.1)  # Configurar el módulo para el modo de texto
    if "OK" in respuesta:
        
        respuesta = enviar_comando_at("AT+CMGL=\"ALL\"", 0.6)  # Leer cada mensaje individualmente
        return respuesta
        #if "+CMGR:" in respuesta:  # Si se encuentra un mensaje
        #    #print("comand: ", "AT+CMGR={}".format(i) ," resp:" , respuesta)
        #    return respuesta
    return mensajes

def borrar_primer_mensaje():
    respuesta = enviar_comando_at("AT+CMGD=1", 0.3)  # Borra el primer mensaje
    if "OK" in respuesta:
        print("Primer mensaje borrado con éxito.")
    else:
        print("Error al borrar el primer mensaje.")

if __name__ == "__main__":
    try:
        if not puerto_serial.is_open:
            puerto_serial.open()
        
        if puerto_serial.is_open:
            print("Conexión establecida con éxito con el módulo SIM800C.")

            #numero_telefono = input("Por favor, ingresa el número de teléfono de la SIM insertada: ")
            numero_telefono = "57310XXXXXXX"
            print("Número de teléfono ingresado:", numero_telefono)

            while True:
                opcion = input("Por favor, seleccione una opción:\n1. Enviar mensaje\n2. Leer mensajes\n3. Leer All mensajes\n4. Borrar 1er mensaje\nexit. Salir\n")
                
                if opcion == "1":
                    mensaje = input("Ingrese el mensaje que desea enviar: ")
                    enviar_mensaje(numero_telefono, mensaje)
                    print("Mensaje enviado con éxito.")
                
                elif opcion == "2":
                    mensajes = leer_mensajes()
                    for mensaje in mensajes:
                        print(mensaje.strip())

                elif opcion == "3":
                    mensajes = leer_all_mensajes()
                    print(str(mensajes))

                elif opcion == "4":
                    mensajes = borrar_primer_mensaje()
                    #print(str(mensajes))
                    
                elif opcion == "exit":
                    break
                
                else:
                    print("Opción no válida.")
                
        else:
            print("No se pudo abrir el puerto serial.")
    
    except serial.SerialException as e:
        print("Error al abrir el puerto serial:", e)
    
    finally:
        if puerto_serial.is_open:
            puerto_serial.close()

