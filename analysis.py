import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs("charts", exist_ok=True)
df = pd.read_csv("bestsellers.csv")
print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())
print(df.isnull().sum())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print("Unique Books")

print(df["Name"].nunique())
print("Unique Authors")

print(df["Author"].nunique())
print(df["Author"].value_counts().head(10))
plt.figure(figsize=(10,6))

df["Author"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Authors")

plt.xlabel("Author")

plt.ylabel("Books")

plt.tight_layout()

plt.savefig("charts/top_authors.png")

plt.show()
print(df["Genre"].value_counts())
plt.figure(figsize=(6,6))

df["Genre"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.savefig("charts/genre.png")

plt.show()
print(df.nlargest(10, "User Rating"))
print(df.nlargest(10, "Reviews"))
print(df.nsmallest(10, "Price"))
print(df.nlargest(10, "Price"))
print(df["Price"].mean())
print(df["User Rating"].mean())
plt.figure(figsize=(8,5))

plt.hist(df["Price"], bins=20)

plt.title("Price Distribution")

plt.xlabel("Price")

plt.ylabel("Frequency")

plt.savefig("charts/price_distribution.png")

plt.show()
year_price = df.groupby("Year")["Price"].mean()

print(year_price)
plt.figure(figsize=(8,5))

year_price.plot(marker="o")

plt.title("Average Price by Year")

plt.ylabel("Average Price")

plt.savefig("charts/year_price.png")

plt.show()
genre_rating = df.groupby("Genre")["User Rating"].mean()

print(genre_rating)
plt.figure(figsize=(6,5))

genre_rating.plot(kind="bar")

plt.title("Average Rating by Genre")

plt.savefig("charts/genre_rating.png")

plt.show()
plt.figure(figsize=(8,5))

plt.scatter(df["Reviews"], df["User Rating"])

plt.xlabel("Reviews")

plt.ylabel("Rating")

plt.title("Reviews vs Rating")

plt.savefig("charts/reviews_rating.png")

plt.show()
print("Analysis Completed Successfully!")
