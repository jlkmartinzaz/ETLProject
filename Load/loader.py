from Config.config import OUTPUT_PATH

class Loader:
    def __init__(self, df, output_path=OUTPUT_PATH):
        self.df = df
        self.output_path = output_path

    def run(self):
        """
        Guarda el DataFrame limpio en CSV
        """
        if self.df is None:
            print("[Loader] No hay datos para cargar")
            return

        self.df.to_csv(self.output_path, index=False)
        print(f"[Loader] Datos cargados en: {self.output_path}")
