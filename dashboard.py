import streamlit as st
import pandas as pd

day_df = pd.read_csv('day_clean.csv')
hour_df = pd.read_csv('hour_clean.csv')

st.header('Data Analysis and Visualization')


### Menampilkan Peminjaman Sepeda Musiman ###
st.subheader('Peminjaman Sepeda berdasarkan Musim')

season_mapping = {
    0: 'Spring',
    1: 'Summer',
    2: 'Fall',
    3: 'Winter'
}

# Mapping bilangan bulat indeks asli DataFrame menjadi nama musim
hour_df.index = hour_df.index.map(season_mapping)

# Menampilkan bar chart dengan data yang telah diolah
st.bar_chart(hour_df['cnt'])

### Menampilkan Peningkatan Peminjaman Sepeda Bulanan Selama 2 Tahun ###
st.subheader('Peningkatan Peminjaman Sepeda Bulanan Selama 2 Tahun')

# Konversi indeks menjadi (tahun, bulan) (biar rapih hehehe)
def convert_to_month_year(index):
    year = index // 12 + 2011
    month = index % 12 + 1
    if month < 10:
        return f'({year}, 0{month})'
    else:
        return f'({year}, {month})'

# Mengubah indeks DataFrame
day_df.index = day_df.index.map(convert_to_month_year)

# Menampilkan line chart
st.line_chart(day_df['cnt'], use_container_width=True)