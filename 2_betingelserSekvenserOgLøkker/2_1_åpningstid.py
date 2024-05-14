# Flytdiagram:
#  Få tid fra brukeren
#  Sjekk om tallet er mer enn 8 og mindre enn 18
#    print stengt
#    returner False
#  Sjekk om tallet er mer enn 18
#    print stengt
#    returner False
#  Returner åpen


def sjekk_åpningstid(tid):
    if tid < 8:
        print("Stengt")
        return False
    elif tid > 18:
        print("Stengt")
        return False
    else:
        print("Åpen")
        return True


tid = int(input("Skriv inn tid i hele timer for å sjekke åpningstid: "))
sjekk_åpningstid(tid)

# Tester:
# sjekk_åpningstid(2)
# sjekk_åpningstid(8)
# sjekk_åpningstid(14)
# sjekk_åpningstid(18)
# sjekk_åpningstid(20)