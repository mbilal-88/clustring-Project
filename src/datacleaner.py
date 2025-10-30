import pandas

def data_cleaner(data):
    print("Data Cleaning...")
    data.drop("CustomerID", axis=1, inplace=True)
    return data
