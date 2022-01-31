"""look through the first 100 digits of pi and print the numbers as letters"""

pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
alphabet = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

for i in pi:
    print(alphabet[int(i) - 1], end="")