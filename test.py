mine_linjer = ["Hei hei!\n", "Vi lærer python!\n"]

with open("min_fil.txt", mode="at") as f:
    print("Nå er filen åpen")
    f.writelines("Hadet")