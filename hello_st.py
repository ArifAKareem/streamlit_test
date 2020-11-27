import streamlit as st

input = st.selectbox(
    'How would you like to be contacted?',
    ('option1', 'option2', 'option3')
)

# Add a selectbox to the sidebar:
add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    (input, 'something else')
)

uploaded_file = st.file_uploader("Choose a file")
print('done')