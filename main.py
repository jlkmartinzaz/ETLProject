from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

def main():
    # Extract
    extractor = Extractor()
    df = extractor.run()

    # Transform
    transformer = Transformer(df)
    df_transformed = transformer.run()

    # Load
    loader = Loader(df_transformed)
    loader.run()

if __name__ == "__main__":
    main()
