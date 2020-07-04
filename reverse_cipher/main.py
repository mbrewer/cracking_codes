# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = '.ti esrever dna ,ti pilf ,nwod gniht ym tuP'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
