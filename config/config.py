from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path
import logging

class Settings(BaseSettings):
    # Directorios
    raw_data_dir: Path = Field(default=Path("data/raw"), env="RAW_DATA_DIR")
    clean_data_dir: Path = Field(default=Path("data/clean"), env="CLEAN_DATA_DIR")

    # Archivos
    input_csv: str = Field(default="yt_sports_channels_stats.csv", env="INPUT_CSV")
    clean_csv: str = Field(default="yt_sports_channels_stats_clean.csv", env="CLEAN_CSV")

    # Base de datos
    database_url: str = Field(..., env="DATABASE_URL")

    # Logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")


def get_settings() -> Settings:
    return Settings()


# Configuración global de logging
settings = get_settings()
logging.basicConfig(
    level=settings.log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("etl")
