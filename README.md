# Kuesioner Pola Hidup Sehat

Aplikasi Streamlit sederhana berupa kuesioner interaktif untuk menilai pola hidup sehat
berdasarkan kebiasaan tidur, makan, dan olahraga.

#  Fitur
- 3 pertanyaan menggunakan `st.radio`
- menggunakan sistem scoring dan masing-masing opsi memiliki bobot nilai berbeda
- Perhitungan skor otomatis
- Halaman hasil dengan kategori kesehatan "Kamu sangat sehat. Pertahankan!", "Kamu sehat, tapi masih bisa ditingkatkan.", "Kamu perlu memperbaiki pola hidupmu."
- Tombol reset / test ulang
- GIF untuk tampilan lebih interaktif (terdapat file GIF di folder assets)

## 🛠️ Bahasa dan library
- Python
- Streamlit

## ▶️ Cara Menjalankan
- pip install streamlit
- streamlit run app.py
- muncul pertanyaan 1, lalu user menjawab berpindah ke halaman pertanyaan 2
- muncul pertanyaan 2, lalu user menjawab berpindah ke halaman pertanyaan 3
- muncul pertanyaan 3, lalu user menjawab dan menekan tombol "tampilkan hasil" untuk menampilkan hasil berdasarkan bobot scoring yang ada
- hasil yang bisa muncul adalah "Kamu sangat sehat. Pertahankan!", "Kamu sehat, tapi masih bisa ditingkatkan.", "Kamu perlu memperbaiki pola hidupmu."
