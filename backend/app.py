import os
import sys
import pandas as pd
from typing import List

def get_data(references: List[str]) -> dict:
    '''Load CSV files into DataFrames.'''
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    dfs = {}
    for filename in references:
        filepath = os.path.join(data_dir, f'{filename}.csv')
        df_name = os.path.splitext(filename)[0]
        dfs[df_name] = pd.read_csv(filepath, usecols=['Vocabulary'], index_col=None)
    return dfs

def compare_vocabularies(large_df: pd.DataFrame, small_df: pd.DataFrame) -> set:
    '''Compare vocabularies between two DataFrames and return the difference.'''
    large_vocab = set(large_df['Vocabulary'])
    small_vocab = set(small_df['Vocabulary'])
    no_cover_vocab = large_vocab - small_vocab
    return no_cover_vocab

def main() -> None:
    large_file: str = sys.argv[1]
    small_file: str = sys.argv[2]
    references: List[str] = [large_file, small_file]
    dfs: dict = get_data(references)
    large_df = dfs.get(large_file)
    small_df = dfs.get(small_file)
    if large_df is None or small_df is None:
        print(f"Error: '{large_file}.csv' or '{small_file}.csv' not found in data directory.")
        return
    no_cover_vocab = compare_vocabularies(large_df, small_df)
    for vocab in sorted(no_cover_vocab):
        print(vocab)
    return

if __name__ == "__main__":
    main()
