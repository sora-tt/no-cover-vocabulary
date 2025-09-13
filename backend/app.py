import os
import pandas as pd

def get_data():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    dfs = {}
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(data_dir, filename)
            df_name = os.path.splitext(filename)[0]
            dfs[df_name] = pd.read_csv(filepath, usecols=['Vocabulary'], index_col=None)
    return dfs

def main():
    return

if __name__ == "__main__":
    main()
