pin_code = "2354"
entered_pin = ""
count = 0
while entered_pin != pin_code:
    entered_pin = input("enter pin code: ")
    count += 1
print(f"you are authorised. you took {count} attempts")