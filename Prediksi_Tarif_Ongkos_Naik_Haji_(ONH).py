import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("dataset_tarif_haji_palu.csv")

tahun = df["Tahun"].values.reshape(-1, 1)
tarif = df["Tarif_Haji_Rp"].values

model = LinearRegression()
model.fit(tahun, tarif)

prediksi_2026 = model.predict([[2026]])
prediksi_2027 = model.predict([[2027]])
prediksi_2028 = model.predict([[2028]])

r2 = model.score(tahun, tarif)

print("=" * 60)
print("PREDIKSI TARIF ONGKOS NAIK HAJI KOTA PALU")
print("=" * 60)

print("\nData Historis")

for t, b in zip(df["Tahun"], df["Tarif_Haji_Rp"]):
    print(f"Tahun {t} : Rp {b:,.0f}")

print("\nHasil Prediksi")

print(f"2026 : Rp {prediksi_2026[0]:,.0f}")
print(f"2027 : Rp {prediksi_2027[0]:,.0f}")
print(f"2028 : Rp {prediksi_2028[0]:,.0f}")

print(f"\nNilai R² : {r2:.4f}")

hasil_prediksi = pd.DataFrame({
    "Tahun": [2026, 2027, 2028],
    "Tarif_Haji_Prediksi_Rp": [
        int(prediksi_2026[0]),
        int(prediksi_2027[0]),
        int(prediksi_2028[0])
    ],
    "Metode": [
        "Regresi Linear",
        "Regresi Linear",
        "Regresi Linear"
    ]
})

hasil_prediksi.to_csv(
    "hasil_prediksi_haji_2026_2028.csv",
    index=False,
    encoding="utf-8-sig"
)

tahun_garis = np.array([
    2021, 2022, 2023, 2024,
    2025, 2026, 2027, 2028
]).reshape(-1, 1)

prediksi_garis = model.predict(tahun_garis)

plt.figure(figsize=(10, 6))

plt.scatter(
    tahun,
    tarif,
    s=100,
    label="Data Historis"
)

plt.plot(
    tahun_garis,
    prediksi_garis,
    linewidth=2,
    label="Model Regresi Linear"
)

plt.scatter(
    [2026, 2027, 2028],
    [
        prediksi_2026[0],
        prediksi_2027[0],
        prediksi_2028[0]
    ],
    s=120,
    label="Hasil Prediksi"
)

plt.annotate(
    f"2026\nRp {prediksi_2026[0]:,.0f}",
    xy=(2026, prediksi_2026[0]),
    xytext=(2026, prediksi_2026[0]-5000000),
    ha="center",
    va="top",
    bbox=dict(
        boxstyle="round,pad=0.4",
        fc="white",
        ec="black"
    )
)

plt.annotate(
    f"2027\nRp {prediksi_2027[0]:,.0f}",
    xy=(2027, prediksi_2027[0]),
    xytext=(2027, prediksi_2027[0]-5000000),
    ha="center",
    va="top",
    bbox=dict(
        boxstyle="round,pad=0.4",
        fc="white",
        ec="black"
    )
)

plt.annotate(
    f"2028\nRp {prediksi_2028[0]:,.0f}",
    xy=(2028, prediksi_2028[0]),
    xytext=(2028, prediksi_2028[0]-5000000),
    ha="center",
    va="top",
    bbox=dict(
        boxstyle="round,pad=0.4",
        fc="white",
        ec="black"
    )
)

plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, p: f"{x:,.0f}")
)

plt.title(
    "Prediksi Tarif Ongkos Naik Haji Kota Palu Tahun 2026-2028",
    fontweight="bold"
)

plt.xlabel("Tahun")
plt.ylabel("Tarif Haji (Rp)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()