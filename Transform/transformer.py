class Transformer:
    def __init__(self, df):
        self.df = df

    def run(self):
        """
        Limpia y transforma los datos:
        - Convierte 'Date' a datetime (con precisión ns)
        - Ordena por fecha
        - Llena valores nulos
        - Agrega columnas 'Daily Change' y 'Percent Change'
        """
        if self.df is None:
            return None

        # Cambiar aquí: datetime64[ns]
        self.df['Date'] = self.df['Date'].astype('datetime64[ns]')
        self.df.sort_values('Date', inplace=True)
        self.df.fillna(method='ffill', inplace=True)

        self.df['Daily Change'] = self.df['Close'] - self.df['Open']
        self.df['Percent Change'] = ((self.df['Close'] - self.df['Open']) / self.df['Open']) * 100

        print("[Transformer] Transformación completada")
        return self.df
