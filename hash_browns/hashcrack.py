import sys
from Crypto.Hash import SHA256
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def main():
  dic = sys.argv[1]
  hsh = sys.argv[2]

  f = open(dic, "r")

  i = 0
  for x in f:
    if i == 1000:
      break
    wrd = x[:-1]

    v = bytes(wrd, "utf-8")
    hash_obj = SHA256.new(data=v)
    hsh_str = str(hash_obj.hexdigest())

    if hsh_str == hsh:
      print("key found:", wrd)
      break
    elif wrd == "pineapple":
      print("broke")
      return -1

    i = i + 1

  return 0

main()
