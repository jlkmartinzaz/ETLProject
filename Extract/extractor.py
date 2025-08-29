import pandas as pd
from Config.config import DATA_PATH

class Extractor:
    def __init__(self, file_path=DATA_PATH):
        self.file_path = file_path

    def run(self):
        """
        Extrae los datos del CSV y retorna un DataFrame
        """
        try:
            df = pd.read_csv(self.file_path)
            print(f"[Extractor] Datos extraídos: {len(df)} filas")
            return df
        except FileNotFoundError:
            print(f"[Extractor] Archivo no encontrado: {self.file_path}")
            return None
