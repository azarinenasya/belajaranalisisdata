# Dashboard Analisis Kualitas Udara

## Deskripsi Proyek
Dashboard interaktif ini dikembangkan menggunakan Streamlit untuk menganalisis dan memvisualisasikan data kualitas udara historis. Aplikasi ini memungkinkan pengguna untuk menjelajahi tren konsentrasi PM2.5 dan PM10, mendistribusikan polutan berdasarkan stasiun, dan melihat korelasi antara PM2.5 dan PM10, dengan kemampuan filtering berdasarkan stasiun, musim, dan rentang tanggal.

## Fitur
-   **Filter Interaktif**: Saring data berdasarkan stasiun pemantauan, musim, dan rentang tanggal yang spesifik.
-   **Ikhtisar Data**: Menampilkan jumlah baris data yang difilter dan lima baris pertama dari dataset.
-   **Metrik Utama**: Menampilkan rata-rata konsentrasi PM2.5 dan PM10 secara keseluruhan dari data yang difilter.
-   **Visualisasi Tren Harian PM2.5**: Grafik garis yang menunjukkan rata-rata harian PM2.5.
-   **Distribusi PM10 per Stasiun**: Box plot yang memvisualisasikan distribusi PM10 di berbagai stasiun.
-   **Korelasi PM2.5 dan PM10**: Scatter plot yang menunjukkan hubungan antara PM2.5 dan PM10, dengan poin-poin yang dikelompokkan berdasarkan musim.

## Persyaratan
Pastikan Anda telah menginstal Python 3.7+.

### Dependencies
Proyek ini membutuhkan pustaka Python berikut. Anda dapat menginstalnya menggunakan `pip`:
```bash
pip install streamlit pandas matplotlib seaborn
```
Atau, jika Anda memiliki file `requirements.txt` (yang direkomendasikan):
```bash
pip install -r requirements.txt
```

## Instalasi
1.  **Clone repositori ini** (jika ini adalah repositori GitHub):
    ```bash
git clone <url-repo-anda>
cd <nama-folder-repo>
    ```
2.  **Unduh file data**: Aplikasi ini mengasumsikan adanya file `air_quality_combined.zip` di direktori yang sama dengan skrip aplikasi. Pastikan Anda memiliki file data ini.

## Struktur Data
Aplikasi ini membutuhkan file ZIP yang berisi CSV dengan nama `air_quality_combined.zip`. File CSV di dalamnya harus memiliki kolom-kolom berikut:
-   `datetime`: Timestamp data (akan diubah ke tipe datetime).
-   `station`: Nama atau ID stasiun pemantauan.
-   `season`: Musim saat data diambil.
-   `PM2.5`: Konsentrasi PM2.5 (µg/m³).
-   `PM10`: Konsentrasi PM10 (µg/m³).

## Cara Menjalankan Aplikasi
Setelah menginstal semua dependencies dan memastikan file data ada, jalankan aplikasi Streamlit dari terminal Anda:

```bash
streamlit run your_streamlit_app_file_name.py
```
(Ganti `your_streamlit_app_file_name.py` dengan nama file Python yang berisi kode Streamlit Anda, misalnya `dashboard_aq.py`.)

Aplikasi akan terbuka di browser web default Anda.

## Penggunaan
-   Gunakan sidebar di sisi kiri untuk memfilter data berdasarkan 'Stasiun', 'Musim', dan 'Rentang Tanggal'.
-   Visualisasi dan metrik utama akan diperbarui secara otomatis berdasarkan pilihan filter Anda.
-   Jika tidak ada data yang sesuai dengan filter yang dipilih, pesan peringatan akan ditampilkan.


[Opsional: Tambahkan informasi lisensi di sini, misal MIT License]
