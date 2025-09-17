import pandas as pd
from config.config import settings, logger
from pathlib import Path


def read_csv(file_path: str = None) -> pd.DataFrame:
    """
    Lee el CSV desde la carpeta raw.
    """
    path = Path(file_path) if file_path else settings.raw_data_dir / settings.input_csv

    if not path.exists():
        logger.error(f"Archivo no encontrado: {path}")
        raise FileNotFoundError(f"El archivo {path} no existe.")

    logger.info(f"Leyendo CSV desde {path}...")
    df = pd.read_csv(path)
    logger.info(f"Archivo leído con {len(df)} filas y {len(df.columns)} columnas.")
    return df
