import os
import pandas as pd
from typing import List

def get_data(references: List[str]) -> dict:
    '''Load CSV files into DataFrames.'''
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
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
