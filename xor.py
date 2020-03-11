hex_s1 = input("enter first hex string: \n")
hex_s2 = input("enter second hex string: \n")
hex_s3 = ""

for i in range (0, len(hex_s1), 2):
	hex1 = hex_s1[i:i+2]
	hex2 = hex_s2[i:i+2]
	
	dec1 = int(hex1, 16)
	dec2 = int(hex2, 16)

	dec3 = dec1 ^ dec2
	hex3 = hex(dec3)
	hex_s3 += hex3[2:4]

print(hex_s3)
