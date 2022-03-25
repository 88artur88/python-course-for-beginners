def calculate_brutto(netto, vat=0.23):
    return netto + netto * vat


total = calculate_brutto(100)
total += calculate_brutto(200)
print(total)


