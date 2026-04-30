import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data
file_path = 'air_quality_combined.zip'
try:
    df_air_quality = pd.read_csv(file_path, compression='zip')
except FileNotFoundError:
    st.error(f"Error: File '{file_path}' not found. Please upload the file.")
    st.stop() # Stop the app if file is not found
except Exception as e:
    st.error(f"An error occurred while loading the dataset: {e}")
    st.stop() # Stop the app if there's an error

df = df_air_quality.copy() # Gunakan salinan untuk menghindari modifikasi df_air_quality asli

# Mengubah kolom datetime menjadi tipe datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Menyiapkan Streamlit dashboard
st.set_page_config(page_title="Dashboard Kualitas Udara", layout="wide")
st.title("Dashboard Analisis Kualitas Udara")
st.subheader("Analisis Kualitas Udara Berdasarkan Data Historis")

# --- Sidebar untuk Filter ---
st.sidebar.header("Filter Data")

# Filter Stasiun
selected_stations = st.sidebar.multiselect(
    "Pilih Stasiun",
    options=df['station'].unique(),
    default=df['station'].unique()
)

# Filter Musim
selected_seasons = st.sidebar.multiselect(
    "Pilih Musim",
    options=df['season'].unique(),
    default=df['season'].unique()
)

# Filter Rentang Tanggal
min_date = df['datetime'].min().date()
max_date = df['datetime'].max().date()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Pastikan date_range memiliki 2 elemen
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date # Default jika hanya satu tanggal dipilih

# Menerapkan Filter
df_filtered = df[
    (df['station'].isin(selected_stations)) &
    (df['season'].isin(selected_seasons)) &
    (df['datetime'].dt.date >= start_date) &
    (df['datetime'].dt.date <= end_date)
]

# --- Tampilan Utama Dashboard ---

if df_filtered.empty:
    st.warning("Tidak ada data yang tersedia dengan filter yang dipilih.")
else:
    st.subheader("Ikhtisar Data Terfilter")
    st.write(f"Jumlah baris data: {len(df_filtered)}")
    st.dataframe(df_filtered.head())

    # Metrik Utama
    col1, col2 = st.columns(2)
    with col1:
        avg_pm25 = df_filtered['PM2.5'].mean()
        st.metric("Rata-rata PM2.5", f"{avg_pm25:.2f} µg/m³")

    with col2:
        avg_pm10 = df_filtered['PM10'].mean()
        st.metric("Rata-rata PM10", f"{avg_pm10:.2f} µg/m³")

    st.markdown("--- ")

    # Visualisasi 1: Tren Harian PM2.5
    st.subheader("Tren Harian Konsentrasi PM2.5")
    daily_pm25 = df_filtered.groupby(df_filtered['datetime'].dt.date)['PM2.5'].mean().reset_index()
    daily_pm25.columns = ['Date', 'PM2.5_Avg']

    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=daily_pm25, x='Date', y='PM2.5_Avg', ax=ax1)
    ax1.set_title("Rata-rata PM2.5 Harian")
    ax1.set_xlabel("Tanggal")
    ax1.set_ylabel("Rata-rata PM2.5 (µg/m³)")
    ax1.grid(True)
    st.pyplot(fig1)
    plt.close(fig1)

    st.markdown("--- ")

    # Visualisasi 2: Distribusi PM10 berdasarkan Stasiun
    st.subheader("Distribusi PM10 berdasarkan Stasiun")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df_filtered, x='station', y='PM10', ax=ax2)
    ax2.set_title("Distribusi PM10 per Stasiun")
    ax2.set_xlabel("Stasiun")
    ax2.set_ylabel("PM10 (µg/m³)")
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True)
    st.pyplot(fig2)
    plt.close(fig2)

    st.markdown("--- ")

    # Visualisasi 3: Korelasi antara PM2.5 dan PM10
    st.subheader("Korelasi antara PM2.5 dan PM10")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df_filtered, x='PM2.5', y='PM10', hue='season', ax=ax3, alpha=0.6)
    ax3.set_title("Scatter Plot PM2.5 vs PM10")
    ax3.set_xlabel("PM2.5 (µg/m³)")
    ax3.set_ylabel("PM10 (µg/m³)")
    ax3.grid(True)
    st.pyplot(fig3)
    plt.close(fig3)

# Instruksi untuk menjalankan secara lokal
st.sidebar.markdown("Untuk menjalankan aplikasi ini secara lokal, simpan kode ini sebagai file `.py` (misalnya, `dashboard_aq.py`) dan jalankan di terminal: `streamlit run dashboard_aq.py`")