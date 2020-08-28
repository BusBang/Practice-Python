alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text) :
    ciphertext = ""
    for ch in text :
        if ch in alph :
            i = (alph.index(ch) + 3) % 26
            ciphertext += alph[i]
        else :
            ciphertext += ch
    return ciphertext

def decrypt(text) :
    ciphertext = ""
    for ch in text :
        if ch in alph :
            # if alph.index(ch)<3 :
            #     i = (alph.index(ch)+23)
            # else :
            #     i = (alph.index(ch)-3)
            i = (alph.index(ch)+23) % 26
            ciphertext += alph[i]
        else :
            ciphertext += ch
    return ciphertext

print(encrypt("I'm a ironman"))
print(decrypt("I'p d lurqpdq"))
print(encrypt("abcd wxyz"))
print(decrypt("defg zabc"))