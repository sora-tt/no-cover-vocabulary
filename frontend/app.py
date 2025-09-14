import streamlit as st
from backend.modules.app import get_data, compare_vocabularies

def main():
    st.title("No Cover Vocabulary")

    st.write("""
    This application compares vocabularies between two CSV files and identifies words present in the larger file but absent in the smaller one.
    """)

    large_file = st.text_input("Enter the name of the larger CSV file (without .csv):", placeholder="e.g., system")
    small_file = st.text_input("Enter the name of the smaller CSV file (without .csv):", placeholder="e.g., target")

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
