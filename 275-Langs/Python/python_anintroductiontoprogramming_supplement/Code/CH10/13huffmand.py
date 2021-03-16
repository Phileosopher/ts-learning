# Huffman decode
# This is the coded message
bitstring = "010001011100010110101111000101110011"+\
            "111101001111110100101110011111101001"+\
            "010101110110000110111110111011000011"+\
            "110101110100011001110010011100001100"+\
            "010101100000110101000111110101001111"+\
            "001000111000001011010010111001000010"+\
            "101011101100001110111111011011110001"+\
            "01101100"
table = {}              # This is the table of codes
table['00'] = " "
table["11111"] = "A"
table["011100"] = "D"
table["111100"] = "V"
table["101"] = "T"
table["11101"] = "M"
table["011101"] = "F"
table["100"] = "E"
table["01100"] = "U"
table["011110"] = "K"
table["010"] = 	"I"
table["111101"] = "O"
table["011111"] = "L"
table["1100"] = "H"
table["011010"] = "B"
table["111000"] = "Q"
table["1101"] = "N"
table["011011"] = "C"
table["111001"] = "S"

# Pull bits from the string making a substring
# until the substringis found in the dictionary.
# Then emit the character indexed.
while len(bitstring) > 0: # Until all bits are used
    code = ""              # Clear the current code
    while not (code in table):     # Is this in the dictionary?
        code = code + bitstring[0] # No. Add the next bit from the message
        bitstring = bitstring[1:] # Remove that bit from the message
    print (table[code], end="")   # When the code matches, print the character