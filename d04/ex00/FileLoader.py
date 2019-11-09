import pandas as pd


class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {len(data.index)} x {len(data.columns)}")
        return data

    def display(self, df, n):
        if n < 0:
            print(df[n:])
        else:
            print(df[:n])
