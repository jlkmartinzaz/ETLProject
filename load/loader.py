import pandas as pd
from sqlalchemy import create_engine
from config.config import settings, logger
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import multivariate_normal


def load_to_db(df: pd.DataFrame):
    engine = create_engine(settings.database_url)

    logger.info("Cargando datos en la base de datos...")
    df.to_sql("youtube_channels", con=engine, if_exists="replace", index=False, chunksize=5000)
    logger.info("Datos cargados en la base de datos.")


def generate_plots(df: pd.DataFrame):
    logger.info("Generando gráficas...")

    # 1. Gráfica de barras: suscriptores por canal (Top 15 para que sea legible)
    plt.figure(figsize=(12, 6))
    top_channels = df.nlargest(15, "subscribers").sort_values("subscribers", ascending=True)
    plt.barh(top_channels["channel_name"], top_channels["subscribers"], color="skyblue")
    plt.xlabel("Suscriptores")
    plt.ylabel("Canal")
    plt.title("Top 15 canales por suscriptores")
    plt.tight_layout()
    plt.savefig(settings.clean_data_dir / "barras_suscriptores.png")

    # 2. Gráfico de dispersión: videos vs vistas
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="videos", y="views", data=df, alpha=0.7, color="orange")
    plt.xlabel("Número de videos subidos")
    plt.ylabel("Número de vistas")
    plt.title("Relación entre videos subidos y vistas")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(settings.clean_data_dir / "scatter_videos_views.png")

    # 3. Campana de Gauss: distribución conjunta de suscriptores y vistas
    X = df[["subscribers", "views"]].dropna().values
    if len(X) > 2:  # Para que no falle si hay pocos datos
        mu = np.mean(X, axis=0)
        cov = np.cov(X.T)

        x = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
        y = np.linspace(X[:, 1].min(), X[:, 1].max(), 100)
        Xgrid, Ygrid = np.meshgrid(x, y)
        pos = np.dstack((Xgrid, Ygrid))

        rv = multivariate_normal(mean=mu, cov=cov)
        Z = rv.pdf(pos)

        plt.figure(figsize=(8, 6))
        plt.contourf(Xgrid, Ygrid, Z, cmap="viridis", levels=30)
        plt.colorbar(label="Densidad de probabilidad")
        plt.scatter(df["subscribers"], df["views"], c="red", s=20, alpha=0.6, label="Canales")
        plt.xlabel("Suscriptores")
        plt.ylabel("Vistas")
        plt.title("Distribución Gaussiana conjunta: Suscriptores vs Vistas")
        plt.legend()
        plt.tight_layout()
        plt.savefig(settings.clean_data_dir / "gauss_subs_views.png")

    logger.info("Gráficas generadas en data/clean/")
