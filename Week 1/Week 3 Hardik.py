print("How many bars should be charged")
charge_bars = int(input())

bars_charged = 0

while bars_charged < charge_bars:
    #print(("Charging ...", end="")
    bars_charged = bars_charged + 1
    print(f"Charging : {'█ '* bars_charged}")

print("\nThe battery is fully charged.")