import os
import pandas as pd
from typing import List

def get_data(references: List[str], japanese_translation_option: bool = False) -> dict:
    '''Load CSV files into DataFrames.'''
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    dfs = {}
    for filename in references:
        filepath = os.path.join(data_dir, f'{filename}.csv')
        df_name = os.path.splitext(filename)[0]
        if japanese_translation_option:
            usecols=['Vocabulary', 'Meaning']
        else:
            usecols=['Vocabulary']
        dfs[df_name] = pd.read_csv(filepath, usecols=usecols, index_col=None)
    return dfs

def compare_vocabularies(large_df: pd.DataFrame, small_df: pd.DataFrame, japanese_translation_option: bool = False) -> set:
    '''Compare vocabularies between two DataFrames and return the difference.'''
    if 'Vocabulary' not in large_df.columns or 'Vocabulary' not in small_df.columns:
        raise ValueError("Both DataFrames must contain 'Vocabulary' column.")
    if japanese_translation_option:
        if 'Meaning' not in large_df.columns or 'Meaning' not in small_df.columns:
            raise ValueError("Both DataFrames must contain 'Meaning' column when Japanese translation option is enabled.")
        large_vocab = {vocab: meaning for vocab, meaning in zip(large_df['Vocabulary'], large_df['Meaning'])}
        small_vocab = set(small_df['Vocabulary'])
        no_cover_vocab = set((vocab, meaning) for vocab, meaning in large_vocab.items() if vocab not in small_vocab)
    else:
        large_vocab = set(large_df['Vocabulary'])
        small_vocab = set(small_df['Vocabulary'])
        no_cover_vocab = large_vocab - small_vocab
    return no_cover_vocab