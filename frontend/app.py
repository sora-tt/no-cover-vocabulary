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

    large_file = st.selectbox("Select the larger vocabulary notebook:", options, index=0, placeholder="e.g., system")
    small_file = st.selectbox("Select the smaller vocabulary notebook:", options, index=0, placeholder="e.g., target")

    col1, col2 = st.columns([3, 8])
    compare_vocabularies_button = col1.button("Compare Vocabularies", key="compare_btn")
    clear_button = col2.button(
        "Clear", 
        disabled=not ('result' in st.session_state and st.session_state['result'] is not None),
        key="clear_btn"
    )
    
    if compare_vocabularies_button:
        if large_file not in ('', "---") and small_file not in ('', "---"):
            dfs = get_data([large_file, small_file])
            large_df = dfs.get(large_file)
            small_df = dfs.get(small_file)
            if large_df is None or small_df is None:
                st.session_state['result'] = None
                st.error(f"Error: '{large_file}.csv' or '{small_file}.csv' not found in data directory.")
            else:
                result = compare_vocabularies(large_df, small_df)
                st.session_state['result'] = result
                st.rerun()
        else:
            st.session_state['result'] = None
            st.error("Please enter both file names.")

    if clear_button:
        st.session_state['result'] = None
        st.rerun()
        
    if 'result' in st.session_state and st.session_state['result'] is not None:
        st.subheader('No Cover Vocabulary Results')
        st.write(f'The number of vocabularies not covered: {len(st.session_state["result"])}')
        if st.session_state['result']:
            for vocab in sorted(st.session_state['result']):
                st.write(vocab)
        else:
            st.write("All vocabularies in the larger file are covered by the smaller file.")

if __name__ == "__main__":
    main()
