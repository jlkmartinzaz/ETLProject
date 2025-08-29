import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Config/
DATA_PATH = os.path.join(BASE_DIR, "..", "Extract", "Files", "Nvidia.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "Extract", "Files", "Nvidia_clean.csv")
