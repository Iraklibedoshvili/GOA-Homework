number = input("Enter any  number: ")
try:
    books = int(number)
except:
    books = input("Add second  number")
if number < 0 :
    raise number("number must not be negative")

#raise keywords viyenebs shecdomis gamosasworeblad