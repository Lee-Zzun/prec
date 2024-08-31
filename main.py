# main.py
# streamlit을 이용한 주가 차트

import streamlit as st
from data_loader import load_data

def main():
    st.title('This is Git Prec')

    df = load_data()

    st.write(df)

if __name__ == '__main__':
    main()