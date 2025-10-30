import zipfile

def extract_data(zip_path, output_path):
    with zipfile.ZipFile(zip_path) as file:
        file.extractall(output_path)
    print(f"Data Saved at {output_path}")