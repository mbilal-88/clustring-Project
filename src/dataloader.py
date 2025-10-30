import pandas 

def data_loader(data_path):
    print("Loading Data...")
    df = pandas.read_csv(data_path)
    return df