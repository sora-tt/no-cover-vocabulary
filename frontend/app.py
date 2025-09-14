import streamlit as st
import subprocess

def main():
    st.title("No Cover Vocabulary")

    st.write("""
    This application compares vocabularies between two CSV files and identifies words present in the larger file but absent in the smaller one.
    """)

    large_file = st.text_input("Enter the name of the larger CSV file (without .csv):", placeholder="e.g., system")
    small_file = st.text_input("Enter the name of the smaller CSV file (without .csv):", placeholder="e.g., target")

    if st.button("Compare Vocabularies"):
        if large_file and small_file:
            try:
                result = subprocess.run(
                    ["python3", "backend/app.py", large_file, small_file],
                    capture_output=True,
                    text=True,
                    check=True
                )
                st.subheader("No Cover Vocabulary:")
                st.text(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error(f"An error occurred: {e.stderr}")
        else:
            st.error("Please enter both file names.")

if __name__ == "__main__":
    main()
