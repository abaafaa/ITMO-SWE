import polars as pl
import matplotlib.pyplot as plt

path = r"C:\Users\user\Desktop\ЛР5.xlsx"

df = pl.read_excel(path, raise_if_empty=False)

print("Исходные данные из Excel:")
print(df)

df = df.rename({
    df.columns[0]: "X",
    df.columns[1]: "Value",
    df.columns[2]: "Binary"
})

df = df.filter(pl.col("X").cast(pl.Utf8).str.starts_with("X"))

df = df.with_columns(pl.col("Value").cast(pl.Int32))

print("\nОчищенные данные:")
print(df)

out_path = r"C:\Users\user\Desktop\ЛР5_очищено.xlsx"
df.write_excel(out_path)

print(f"\nФайл сохранён: {out_path}")

values = df["Value"].to_list()

plt.figure()
plt.boxplot(values)
plt.title("Диаграмма «Ящик с усами» (ЛР5)")
plt.ylabel("Значения")
plt.xticks([1], ["X1–X12"])
plt.grid(True)

plt.show()
