from extract.extractor import read_csv
from transform.transformer import transform_data, save_clean_csv
from load.loader import load_to_db, generate_plots
from config.config import logger


def run_etl():
    logger.info("=== Iniciando ETL ===")

    # 1. Extraer
    df = read_csv()

    # 2. Transformar
    df_clean = transform_data(df)
    clean_file = save_clean_csv(df_clean)

    # 3. Cargar
    load_to_db(df_clean)

    # 4. Visualizar
    generate_plots(df_clean)

    logger.info("=== Proceso ETL completado ===")


if __name__ == "__main__":
    run_etl()
