
try:
    my_list = [5, 10, 15]
    print (my_list.pop(input("ampirchie elementis indexi: ")))
except TypeError:
    print("ar aris es ardebuli indexi")
finally:
    print("dasasruli")