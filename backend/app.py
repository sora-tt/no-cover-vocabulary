import os
import pandas as pd

def get_data():
    # TODO: We should refactor here because this function reads all CSV files in the data directory.
    # For now, we assume there are only two files: system.csv and target.csv.
    # We should ensure that only needed files are read.
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    dfs = {}
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(data_dir, filename)
            df_name = os.path.splitext(filename)[0]
            dfs[df_name] = pd.read_csv(filepath, usecols=['Vocabulary'], index_col=None)
    return dfs

def compare_vocabularies(large_df, small_df):
    large_vocab = set(large_df['Vocabulary'])
    small_vocab = set(small_df['Vocabulary'])
    no_cover_vocab = large_vocab - small_vocab
    return no_cover_vocab

def main():
    dfs = get_data()
    # TODO: Let's eliminate these kinds of hard-coded names.
    # We should make the function more flexible to handle different filenames.
    system_df = dfs.get('system')
    target_df = dfs.get('target')
    if system_df is None or target_df is None:
        print("Error: 'system.csv' or 'target.csv' not found in data directory.")
        return
    no_cover_vocab = compare_vocabularies(system_df, target_df)
    print("No Cover Vocabulary:")
    for vocab in sorted(no_cover_vocab):
        print(vocab)
    return

if __name__ == "__main__":
    main()
