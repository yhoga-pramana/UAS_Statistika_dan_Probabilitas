# Prediksi Tarif Ongkos Naik Haji Kota Palu Menggunakan Regresi Linear

## Deskripsi Proyek

Proyek ini bertujuan untuk memprediksi tarif Ongkos Naik Haji Kota Palu pada tahun 2026, 2027, dan 2028 menggunakan metode Regresi Linear.

## Dataset

Data yang digunakan berasal dari BPS Kota Palu.

| Tahun | Tarif Haji (Rp)|
|-------|----------------|
| 2021  | 37.052.602     |
| 2022  | 41.362.590     |
| 2023  | 50.792.201     |
| 2024  | 56.510.444     |
| 2025  | 57.235.421     |

## Metode

Metode yang digunakan adalah Regresi Linear.

Persamaan:

Y = a + bX

Keterangan:

- Y = Tarif Haji
- X = Tahun
- a = Konstanta
- b = Koefisien Regresi

## Library yang Digunakan

- NumPy
- Pandas
- Matplotlib
- Scikit-Learn

## Instalasi

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Cara Menjalankan Program

```bash
python Prediksi_Tarif_Ongkos_Haji.py
```

## Hasil Prediksi

| Tahun | Prediksi Tarif Haji (Rp) |
|-------|--------------------------|
| 2026  | 65.244.699               |
| 2027  | 70.796.048               | 
| 2028  | 76.347.398               |

## Evaluasi Model

Nilai koefisien determinasi (R²) ≈ 0.9405.

Hal ini menunjukkan bahwa model Regresi Linear mampu menjelaskan sekitar 94% variasi data historis tarif haji yang digunakan.


## Kesimpulan

Berdasarkan hasil implementasi metode Regresi Linear menggunakan data tarif Ongkos Naik Haji Kota Palu tahun 2021–2025, diperoleh prediksi tarif haji sebesar Rp65.244.699 pada tahun 2026, Rp70.796.048 pada tahun 2027, dan Rp76.347.398 pada tahun 2028.

Hasil prediksi menunjukkan adanya tren peningkatan tarif haji dari tahun ke tahun. Dengan nilai R² yang tinggi, model dapat digunakan sebagai pendekatan sederhana untuk memproyeksikan tarif haji pada tahun-tahun berikutnya.