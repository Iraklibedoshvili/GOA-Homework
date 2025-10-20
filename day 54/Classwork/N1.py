products = {
    "Jeans":125,
    "T-Shirt":65,
    "shoes":200,
    "shorts":95

}
filtered = dict(filter(lambda i: i[1] < 100 , products.items()))
print(filtered)