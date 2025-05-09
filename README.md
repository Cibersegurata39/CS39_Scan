# CS39_Scan

<img src="https://img.shields.io/badge/-python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

Programa creado en Python para el escaneo de puertos de la dirección IP introducida por el usuario.

Tras pedir una dirección IP, está es validada para asegurar que existe. En caso contrario, se acaba el programa y se muestra un mensaje avisando. Seguidamente se crea una instancia de la clase *PortScanner* (traída de la librería *nmap*) y se realiza el escaneo de la IP facilitada con el metodo *scan*. Además de indicar los parámetro '-n' para no hacer la resolución de dominios, '-Pn' para no lanzar un *ping* y '-T4' para hacer el escaneo más rápido.

Por pantalla se mostrará el *host* (la IP proporcionada) y el estado en el que se encuentra, es decir si está levantado o no. A continuación
