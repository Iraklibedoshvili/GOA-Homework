dictionary=[
    "product1",20,
    "product2",101,
    "product3",99,
    "product5",100
]
filtered=list(filter(lambda item : item[1] < 100,dictionary))
print(filtered)