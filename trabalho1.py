import pandas as pd

dados = pd.read_csv('items.csv')

itens = dados[["asin", "brand", "title" , "url", "image", "rating", "reviewUrl", "totalReviews", "prices"]]

print(itens)
