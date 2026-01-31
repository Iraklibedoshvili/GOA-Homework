S = str(input("Enter sentance:"))
S_reversed = (S[-100:])
if S == S_reversed:
    print("Palindorem")
else:
    print("this sentance is normal")