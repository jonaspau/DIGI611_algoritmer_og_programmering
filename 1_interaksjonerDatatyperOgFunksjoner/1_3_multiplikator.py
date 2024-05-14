def multiplikator():
    tall_1 = float(input("Første tall: "))
    tall_2 = float(input("Andre tall: "))
    sum = tall_1 * tall_2

    return(f"{tall_1} * {tall_2} = {sum}")

sum = multiplikator()
print(sum)
