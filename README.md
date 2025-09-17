# ETLProject – YouTube Sports Channels Statistics
## Introducción

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para analizar estadísticas de canales de YouTube relacionados con deportes.

A partir de un dataset público de Kaggle, el flujo es el siguiente:

Extract → Carga el CSV con información de canales.

Transform → Limpieza, normalización y renombrado de columnas.

Load → Inserción de los datos en una base de datos SQLite y generación de gráficas exploratorias.

## Estructura del Proyecto
ETLProject/
│
├── config/               # Configuración del proyecto
│   └── config.py
│
├── extract/              # Extracción de datos
│   └── extractor.py
│
├── transform/            # Transformación de datos
│   └── transformer.py
│
├── load/                 # Carga de datos y visualización
│   └── loader.py
│
├── data/                 # Carpeta de datos
│   ├── raw/              # Datos originales (entrada)
│   │   └── yt_sports_channels_stats.csv
│   ├── clean/            # Datos transformados + gráficas
│   │   ├── yt_sports_channels_stats_clean.csv
│   │   ├── distribucion_suscriptores.png
│   │   ├── scatter_views_subs.png
│   │   └── top10_videos.png
│   └── youtube_channels.db   # Base de datos SQLite
│
├── main.py               # Script principal del pipeline
├── .env                  # Variables de entorno
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación

## Instalación
1. Clonar el repositorio
git clone https://github.com/jlkmartinzaz/ETLProject.git
cd ETLProject

2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate   # En Linux / Mac


3. Instalar dependencias
pip install -r requirements.txt

## Configuración

El proyecto utiliza variables de entorno definidas en .env.

## Ejecución

Ejecutar el pipeline completo:

python main.py


## El flujo será:

Lectura del CSV en data/raw/yt_sports_channels_stats.csv.

Transformación y guardado de yt_sports_channels_stats_clean.csv en data/clean/.

Inserción en la base de datos youtube_channels.db.

Generación de gráficas en data/clean/.

## Gráficas Generadas

Distribución de suscriptores → Histograma.

Relación vistas vs suscriptores → Scatter plot.

Top 10 canales por número de videos → Barplot.

Ejemplo de salida:

data/clean/barras_suscriptores.png

data/clean/gauss_subs_views.png

data/clean/scatter_videos_views.png

Tecnologías

Python 3.12

Pandas
 - Manipulación de datos

SQLAlchemy
- Conexión a la base de datos

SQLite
- Base de datos ligera

Seaborn
 y Matplotlib
 - Visualización

Pydantic
 + pydantic-settings
 . Manejo de configuración

Mejoras Futuras
  - Añadir soporte para PostgreSQL o MySQL.

Automatizar descargas de nuevos datasets desde Kaggle API.

Agregar pruebas unitarias (pytest).
Crear dashboard con Streamlit.

Autor: José Luis Martínez
Basado en dataset de Kaggle – YouTube Sports Channels Statistics
https://www.kaggle.com/datasets/kanchana1990/youtube-sports-channels-statistics?resource=download
