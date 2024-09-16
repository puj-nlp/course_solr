
# Proyecto Solr para Recuperación de Datos

Este repositorio está dedicado al proyecto de recuperación de información utilizando **Apache Solr**. El objetivo del proyecto es demostrar el uso de Solr para la indexación y búsqueda de una base de datos, así como la creación de una aplicación web interactiva con **Streamlit** para visualizar los resultados de las consultas.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Aplicación Streamlit](#aplicación-streamlit)
- [Docker Compose](#docker-compose)
- [Licencia](#licencia)

## Introducción

Este proyecto tiene como objetivo enseñar el uso de Solr para la recuperación de información en una base de datos. Adicionalmente, se implementa una aplicación en **Streamlit** que permite a los usuarios interactuar con Solr y realizar consultas sobre los datos indexados de forma sencilla y visual.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

- [Apache Solr](https://solr.apache.org/)
- [Python 3.x](https://www.python.org/)
- Bibliotecas de Python:
  - `streamlit`
  - `requests`
  - `pysolr` (para interactuar con Solr desde Python)

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Instalación

### 1. Clonar el repositorio

Clona este repositorio a tu máquina local:

```bash
git clone https://github.com/puj-nlp/course_solr.git
cd course_solr
```

### 2. Configurar Apache Solr

- Descarga e instala Apache Solr siguiendo [esta guía oficial](https://solr.apache.org/guide/).
- Crea un **core** en Solr llamado `lyricrs_example` (o cualquier nombre relevante para tu proyecto).
  
```bash
bin/solr create -c lyricrs_example
```

- Indexa los datos en Solr utilizando los comandos proporcionados en el archivo `index_data.py` dentro del repositorio.

### 3. Ejecutar la aplicación Streamlit

Una vez que Solr esté en funcionamiento y los datos estén indexados, puedes iniciar la aplicación de Streamlit para realizar consultas:

```bash
streamlit run app.py
```

## Uso

1. Accede a la aplicación web generada por Streamlit.
2. Realiza búsquedas en la base de datos indexada a través de la interfaz.
3. Explora las funcionalidades de búsqueda y recuperación de información.

## Estructura del Proyecto

- `app.py`: Código de la aplicación Streamlit para interactuar con Solr.
- `index_data.py`: Script para indexar la base de datos en Solr.
- `requirements.txt`: Lista de dependencias del proyecto.
- `data/`: Carpeta que contiene los archivos de datos que se indexan en Solr.

## Aplicación Streamlit

La aplicación en **Streamlit** permite realizar consultas a través de la API de Solr y mostrar los resultados de manera visual. Algunas características incluyen:

- **Campo de búsqueda**: Permite a los usuarios buscar términos específicos en la base de datos.
- **Filtros**: Opciones adicionales para filtrar los resultados según criterios definidos.
- **Visualización de resultados**: Los resultados de las consultas se muestran en tiempo real en una tabla interactiva.

## Docker Compose

Este proyecto incluye un archivo `docker-compose.yml` que permite ejecutar Apache Solr y otros servicios necesarios para el proyecto de forma automatizada.

Para iniciar Solr y la aplicación con Docker Compose, ejecuta:

```bash
docker-compose up --build
```

Esto levantará el servicio de Solr y otros componentes que se hayan definido en el archivo `docker-compose.yml`.

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).
