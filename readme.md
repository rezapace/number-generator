# Number Generator

## Deskripsi
Proyek ini adalah sebuah program yang digunakan untuk menghasilkan deretan angka dengan langkah tertentu dan menambahkan teks setelah setiap angka. Program ini mendukung berbagai metode untuk menghasilkan angka, termasuk penggunaan CuPy untuk memanfaatkan GPU, serta penggunaan threading untuk meningkatkan kinerja.

## Kegunaan
Program ini berguna untuk:
- Menghasilkan deretan angka dengan langkah tertentu.
- Menambahkan teks khusus setelah setiap angka.
- Menyimpan hasil deretan angka ke dalam sebuah file teks.

## Fungsi
Program ini terdiri dari beberapa fungsi utama:
1. `generate_numbers()`: Menghasilkan deretan angka berdasarkan input pengguna.
2. `save_to_file(numbers)`: Menyimpan deretan angka yang dihasilkan ke dalam file `output.txt`.
3. `main()`: Fungsi utama yang mengkoordinasikan proses pengambilan input, menghasilkan angka, dan menyimpan hasilnya.

## Bagaimana Menjalankan
1. **Menggunakan Python Biasa**:
   - Jalankan `app.py` atau `app1.py` dengan perintah:
     ```bash
     python app.py
     ```
   - Ikuti instruksi untuk memasukkan angka pertama, angka terakhir, langkah, dan teks tambahan.

2. **Menggunakan Threading**:
   - Jalankan `app2.py` dengan perintah:
     ```bash
     python app2.py
     ```
   - Ikuti instruksi untuk memasukkan angka pertama, angka terakhir, langkah, dan teks tambahan.

3. **Menggunakan CuPy untuk Memanfaatkan GPU**:
   - Jalankan `app3.py` atau `number_generator.ipynb` dengan perintah:
     ```bash
     python app3.py
     ```
   - Atau buka `number_generator.ipynb` di Jupyter Notebook atau Google Colab dan jalankan sel-sel kode.
   - Ikuti instruksi untuk memasukkan angka pertama, angka terakhir, langkah, dan teks tambahan.

## Kesimpulan
Program ini menawarkan berbagai metode untuk menghasilkan deretan angka dengan langkah tertentu dan menambahkan teks setelah setiap angka. Dengan memanfaatkan CuPy, program ini dapat memanfaatkan kekuatan GPU untuk meningkatkan kinerja. Program ini juga mendukung threading untuk mempercepat proses. Hasil akhirnya disimpan dalam file `output.txt`, yang memudahkan pengguna untuk mengakses dan menggunakan data yang dihasilkan.
```

Silakan sesuaikan dan tambahkan detail lebih lanjut sesuai kebutuhan Anda.