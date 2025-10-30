import os
from src.dataextractor import extract_data
from src.dataloader import data_loader
from src.datacleaner import data_cleaner
from src.datasplitter import data_splitter
from src.datatransformer import data_transform
from train import model
from predict import data_Encoder,data_scaler

ZIP_PATH = "artifacts/Mall Customers.zip"
OUTPUT_PATH = "artifacts"
DATA_PATH = "artifacts/Mall_Customers.csv"

def main():
    if os.path.exists(DATA_PATH):
        print("Found CSV data...")
    else:    
        extract_data(zip_path=ZIP_PATH,
                    output_path=OUTPUT_PATH)

    data = data_loader(DATA_PATH)
    data = data_cleaner(data)
    x = data_splitter(data)
    t_data = data_transform(x)
    model(t_data,x)
    
if __name__ == "__main__":
    main()