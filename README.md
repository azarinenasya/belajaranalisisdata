<img width="1427" height="815" alt="image" src="https://github.com/user-attachments/assets/fa129c73-8a3b-49b5-893f-7469cb6cf9fe" />## Air Quality Dashboard ✨

Dashboard ini menyajikan analisis kualitas udara, fokus pada tren Karbon Monoksida (CO) dan kondisi kritis Nitrogen Dioksida (NO2).

## Setup Environment - Anaconda
```bash
conda create --name air-quality-env python=3.9
conda activate air-quality-env
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```bash
mkdir air_quality_dashboard
cd air_quality_dashboard
pip install virtualenv
virtualenv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## requirements.txt
Anda dapat membuat file `requirements.txt` dengan konten berikut:
```
streamlit
pandas
matplotlib
seaborn
numpy
```

## Run Streamlit App
1. Simpan kode Streamlit dari notebook ini ke dalam sebuah file Python, misalnya `dashboard.py`.
2. Jalankan aplikasi menggunakan perintah berikut di terminal:
```bash
streamlit run https://azarinenasya-belajaranalisisdata-dashboard-cr3u9c.streamlit.app/

```
