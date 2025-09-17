import pandas as pd
from config.config import settings, logger


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformaciones básicas al DataFrame.
    """
    logger.info("Iniciando transformaciones de datos...")

    # Renombrar columnas para consistencia
    df = df.rename(columns={
        "channel_title": "channel_name",
        "video_count": "videos",
        "view_count": "views",
        "subscriber_count": "subscribers"
    })

    # Ejemplo de limpieza: eliminar duplicados y nulos
    df = df.drop_duplicates()
    df = df.dropna(how="all")

    logger.info(f"Datos transformados: {len(df)} filas y columnas {list(df.columns)}")
    return df


def save_clean_csv(df: pd.DataFrame) -> str:
    """
    Guarda el CSV limpio en la carpeta clean.
    """
    output_path = settings.clean_data_dir / settings.clean_csv
    settings.clean_data_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.info(f"CSV limpio guardado en {output_path}")
    return str(output_path)
