import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend'))

import streamlit as st
from modules.app import get_data, compare_vocabularies

def main():
    st.title("No Cover Vocabulary")

    st.write("""
    This application compares vocabularies between two CSV files and identifies words present in the larger file but absent in the smaller one.
    """)
    st.write("If you find any issues, please report them on [Issues Page](https://github.com/sora-tt/no-cover-vocabulary/issues).")
    
    data_dir = os.path.join(os.path.dirname(__file__), '../backend/data')
    csv_files = [f[:-4] for f in os.listdir(data_dir) if f.endswith('.csv')]
    options = ["---"] + csv_files

    large_file = st.selectbox("Select the larger CSV file (without .csv):", options, index=0, placeholder="e.g., system")
    small_file = st.selectbox("Select the smaller CSV file (without .csv):", options, index=0, placeholder="e.g., target")

    if st.button("Compare Vocabularies"):
        if large_file and small_file:
            dfs = get_data([large_file, small_file])
            large_df = dfs.get(large_file)
            small_df = dfs.get(small_file)
            if large_df is None or small_df is None:
                st.error(f"Error: '{large_file}.csv' or '{small_file}.csv' not found in data directory.")
            else:
                result = compare_vocabularies(large_df, small_df)
                st.subheader("No Cover Vocabulary:")
                if result:
                    for vocab in sorted(result):
                        st.write(vocab)
                else:
                    st.write("All vocabularies in the larger file are covered by the smaller file.")
        else:
            st.error("Please enter both file names.")

if __name__ == "__main__":
    main()
