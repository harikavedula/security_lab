alphabets = "abcdefghijklmnopqrstuvwxyz"
alpha_order = dict()
inv_alpha = dict()
for i,ch in enumerate(alphabets):
    alpha_order[ch] = i
    inv_alpha[i] = ch
  

print("NOTE:- Keys should be Relative prime i.e. gcd(a,b) = 1.")   
key = list(map(int, input("Enter key values a and b for key(a,b) :").split()))
plain_text = input("Enter plain text (only letters): ").lower().replace(" ", "")



encrypted = dict()
for char in set(plain_text):
  encrypted[char] = ''

a,b = key[0], key[1]
for ch in encrypted.keys():
  val = ( a * alpha_order[ch] + b )  % 26    # Ci = ( a * Pi + b ) mod 26
  encrypted[ch] = inv_alpha[val]

cipher_text=''
for ch in plain_text:
  if ch not in encrypted:
    cipher_text += ch
  else:
    cipher_text += encrypted[ch]

print("Plain text is  :", plain_text)
print("Cipher text is :", cipher_text)




def gcd(a, b): 
    if a == 0 : 
        return b  
    return gcd(b%a, a) 


def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

print("Cipher text is:",cipher_text)
my_keys = []
print("Hacked Keys might be:(See at the end,found key)")
for a in range(1,26,1):
  for b in range(26):
    if gcd(a,b)==1:   
      temp = ''

      a_inv = modInverse(a,26)
      for ch in cipher_text:
        if ch in alphabets:
          num = (alphabets.find(ch) - b ) *  a_inv     
          num = num % 26
          if num < 0:
            num = num + 26
          temp = temp + alphabets[num]
        else:
          temp = temp + ch
      if temp == plain_text:  
        my_keys = [a,b]
      print("key(%d,%d) ::  %s " %(a,b,temp))

print("\n Key has found:- keys(%d,%d)"% (my_keys[0],my_keys[1]))
