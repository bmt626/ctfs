#!/usr/bin/python3

encrypted_text = [0x58,0x6e,0x60,0x6b,0x7b,0x56,0x66,0x75]
decrypted_text = ''

for i in range(8):
    text_int = ((encrypted_text[i] - 13) & 0x7F)
    text_char = chr((text_int) ^ (i + 7))
    decrypted_text = decrypted_text + text_char

print(decrypted_text)