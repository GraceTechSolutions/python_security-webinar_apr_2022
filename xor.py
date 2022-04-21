# chr
# ord

# number = ord('a')
# print(number)
# string = chr(97)
# print(string)

def xor(word):
    key = input('Enter key: ')
    final_res = ''
    for alpha in word:
        number = ord(alpha)
        key_xor = ord(key)
        res = number ^ key_xor
        final_res = final_res + chr(res)
    
    return final_res


enc = xor('Hello World')
print(enc)

dec = xor(enc)
print(dec)


# Complete Project

# Step 1
# Encrypt data and save to file

# Step 2
# Read data from file and decrypt
