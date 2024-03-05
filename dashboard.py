import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('Analisis Penggunaan Sepeda')
    st.sidebar.title("Visualisasi Dataset Analisis Penggunaan Sepeda")
    tabs = st.sidebar.radio("Menu", ["Pertanyaan 1", "Pertanyaan 2"])
    
    if tabs == "Pertanyaan 1":
        dela_daily = pd.read_csv('C:/Users/ASUS/Downloads/dashboard/all_data.csv')  
        jumlah_pengguna_per_musim = dela_daily.groupby('season')['cnt'].sum()
        st.title("Visualisasi Data")
        fig, ax = plt.subplots()
        ax.bar(jumlah_pengguna_per_musim.index, jumlah_pengguna_per_musim)
        ax.set_xlabel('Musim')
        ax.set_ylabel('Jumlah Pengguna Sepeda')
        ax.set_title('Jumlah Pengguna Sepeda per Musim')
        st.pyplot(fig)

    elif tabs == "Pertanyaan 2":
        dela_daily = pd.read_csv('C:/Users/ASUS/Downloads/dashboard/all_data.csv')
        penyewaan_per_hari = dela_daily.groupby(['workingday', 'holiday'])['cnt'].sum()
        st.title("Visualisasi Data")
        fig, ax = plt.subplots()
        penyewaan_per_hari.unstack().plot(kind='bar', stacked=True, ax=ax)
        ax.set_xlabel('Hari')
        ax.set_ylabel('Jumlah Penyewaan Sepeda')
        ax.set_title('Perbandingan Penyewaan Sepeda pada Hari Kerja dan Hari Libur')
        ax.legend(title='Libur', labels=['Bukan Libur', 'Libur'], loc='upper right')
        st.pyplot(fig)

if __name__ == "__main__":
    main()
