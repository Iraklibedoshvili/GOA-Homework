try:
    a = int(input("ricxvi: "))
    b = int(input("gamyofi: "))
    print(a/b)
except ZeroDivisionError:
    print("ver gayof nulze")
except ValueError:
    print("sheiyvane raime ricxvi")
else:
    print("sworad gaiyo")
finally:
    print("dasasruli")