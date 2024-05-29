# Utilizar una imagen base ligera de Python
FROM python:3.8.2

# Instalar la biblioteca necesaria
#RUN pip install cryptography

# Crear el directorio de la aplicación
WORKDIR /usr/src/app

# Copiar los scripts de Python al contenedor
COPY hola.py /usr/src/app/

# Comando por defecto (puede ser sobreescrito en tiempo de ejecución)
CMD ["python", "hola.py"]