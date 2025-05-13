# CS39_Scan

<div>
  <img src="https://img.shields.io/badge/-python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/-Nmap-6933FF?style=for-the-badge&logo=nmap&logoColor=white" />
</div>

Programa creado en Python para el escaneo de puertos de la dirección IP introducida por el usuario.

Tras pedir una dirección IP, está es validada para asegurar que existe. En caso contrario, se acaba el programa y se muestra un mensaje avisando. Seguidamente se crea una instancia de la clase *PortScanner* (traída de la librería *nmap*) y se realiza el escaneo de la IP facilitada con el metodo *scan*. Además de indicar los parámetro '-n' para no hacer la resolución de dominios, '-Pn' para no lanzar un *ping* y '-T4' para hacer el escaneo más rápido.

Por pantalla se mostrará el *host* (la IP proporcionada) y el estado en el que se encuentra, es decir si está levantado o no. A continuación, se iteran cada uno de los protocolos que se han detectado en el escaneo (por ejemplo, los típicos TCP y UDP). Dentro de cada protocolo, se obtienen y muestran los puertos encontrados, junto con su estado (abierto, cerrado, filtrado...).

Finalmente, se imprime un comando *nmap* con los puertos detectados y la IP proporcionada, junto con los comandos '-sV', para mostrr la versión que corre en cada puerto, '-O' para obtener el sistema operativo que está corriendo en la dirección que se está analizando, y '-sC' para pasar los *scripts* de vulnerabilidades por defecto de *map*.

Además, se permite cancelar la ejecución en cualquier momento e informar de la acción.
