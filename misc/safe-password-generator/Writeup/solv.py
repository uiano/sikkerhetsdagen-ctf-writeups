string_1 = "5051515854515155555256565151585750515158545151555552565651515857505151585451515555525656515158575051515854515155555256565151585750515158545151555552565651515857505151585451515555525656515158573b"
flag_enc = "3b4559585644564f4044586844595453426f514b506f5f5a516c43585f6f54575f494d"

parts = [string_1[i : i + 2] for i in range(0, len(string_1), 2)]
key = []

for x in range(len(parts) - 1):
    for i in range(10):
        # Find output of
        test = ord(str(i)) ^ int((parts[x]), 16)
        if (
            chr(test) == "a"
        ):  # since we just supplied all 'aaaaaa's expept the last one which is most likely a \n
            print("Found: ", i)
            key.append(str(i))

flag_parts = [flag_enc[i : i + 2] for i in range(0, len(flag_enc), 2)]
flag = ""
for x in range(len(flag_parts)):
    test = chr(ord(key[x]) ^ int((flag_parts[x]), 16))
    flag += str(test)

print(flag)
