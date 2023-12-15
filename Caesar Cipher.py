# Caesar Cipher

# Decoding (offset = 10)

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for character in message:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message += alphabet[(character_value + 10) % 26]
  else:
    translated_message += character

print(translated_message)

# Encoding 
message_for_v = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"

translated_message_for_v = ""

for character in message_for_v:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message_for_v += alphabet[(character_value - 10) % 26]
  else:
    translated_message_for_v += character
        
print(translated_message_for_v)

# Encoding function
def caesar_decode(message, offset):
  decoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      decoded_message += alphabet[(character_value + offset) % 26]
    else:
      decoded_message += character

  return decoded_message

# Decoding function
def caesar_encode(message, offset):
  encoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      encoded_message += alphabet[(character_value - offset) % 26]
    else:
      encoded_message += character

  return encoded_message

# Test
message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# Print the output of `caeser_decode()` for the first message with an offset of 10
print(caesar_decode(message_one, 10))

# Now we know what offset to use for the second message, so we use that to solve.
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(caesar_decode(message_two, 14))