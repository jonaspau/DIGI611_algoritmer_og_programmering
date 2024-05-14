def rabatt(medlem, alder):
    if medlem:
        print("Du får 50 prosent rabatt")
    else:
        if alder < 5:
            print("Det er gratis")
        elif alder < 25:
            print("Du får 10 prosent rabatt")
        else:
            if alder > 65:
                print("Du får 25 prosent rabatt")
            else:
                print("Du får ingen rabatt")

rabatt(True, 2)
rabatt(False, 32)
rabatt(True, 72)
rabatt(False, 16)
rabatt(False, 65)
