# Proyecto de Control de Módulo SIM800C con Python

Este proyecto en Python permite interactuar con el módulo SIM800C para enviar y recibir mensajes SMS. El código proporcionado establece una conexión serial con el módulo y ofrece funciones para iniciar el módulo, enviar mensajes SMS y recibir mensajes entrantes.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python en tu sistema. Además, necesitarás instalar el paquete `pyserial`, que se utiliza para la comunicación serial en Python. Puedes instalarlo fácilmente ejecutando el siguiente comando:

```bash
pip install pyserial
```

## Configuración del Módulo SIM800C

1. **Conexión del Módulo**: Conecta el módulo SIM800C a tu dispositivo mediante un cable USB. Asegúrate de que el módulo esté correctamente alimentado y conectado.

2. **Identificación del Puerto COM**: En sistemas Windows, utiliza el Administrador de Dispositivos para encontrar el nombre del puerto COM al que está conectado el módulo SIM800C. Esta información será necesaria para configurar el puerto en el código. Puedes seguir [este enlace](https://live.staticflickr.com/65535/53676398859_8bf74de114_o.png) para ver una imagen de cómo encontrar el Administrador de Dispositivos.

## Uso del Código

El archivo `main.py` contiene el código principal del proyecto. Antes de ejecutarlo, asegúrate de haber configurado correctamente el puerto COM en la línea correspondiente del código:

```python
ser = serial.Serial('COM3', baudrate=9600, timeout=.1, rtscts=0)
```

### Funciones Disponibles:

- **start_gsm()**: Inicia el módulo SIM800C. Esta función debe llamarse primero antes de enviar o recibir mensajes SMS.

- **send_sms(phonenum, msg)**: Envía un mensaje SMS al número de teléfono especificado con el contenido del mensaje proporcionado.

- **receiver_sms()**: Recibe y muestra los mensajes SMS entrantes.

### Ejecución del Proyecto

Una vez que hayas configurado el puerto COM y asegurado la conexión del módulo SIM800C, simplemente ejecuta el archivo `index.py` para interactuar con el módulo y probar las funciones proporcionadas.

## Referencias y Recursos Adicionales

- [GSM-sim800c](https://github.com/AmirhoseinDelavar/GSM-sim800c)
- [Python Exemplarisch - GSM Communication with Python](https://www.python-exemplarisch.ch/index_en.php?inhalt_links=navigation_en.inc.php&inhalt_mitte=raspi/en/gsm.inc.php)
- [PySerial Documentation](https://pythonhosted.org/pyserial/)
- [SIM800C Python Library](https://github.com/nicholac/sim800c/tree/master)

## Imágenes

- [Imagen del Módulo SIM800C](https://live.staticflickr.com/65535/53676398929_8808254ddd_o.png)
- [Otra Imagen del Módulo SIM800C](https://live.staticflickr.com/65535/53676267108_993665130d_o.png)
- [Captura de Pantalla del Administrador de Dispositivos](https://live.staticflickr.com/65535/53676398859_8bf74de114_o.png)

¡Gracias por usar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en contactar al desarrollador. ¡Disfruta explorando las capacidades del módulo SIM800C con Python!
