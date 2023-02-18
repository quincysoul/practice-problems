class CaesarCipher:
    def __init__(self, k=1):
        self.k = k

    def encode(self):

        pass


def encrypt(text, s):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) + s - ord("A")) % 26 + ord("A"))
        else:
            result += chr((ord(ch) + s - 97) % 26 + 97)
    return result


# check the above function
# text = "CEASER CIPHER DEMO"
# s = 400

# print("Plain Text : " + text)
# print("Shift pattern : " + str(s))
# print("Cipher: " + encrypt(text, s))

# text = "MOKCOBxMSZROBxNOWY"
# s = -400

# print("Plain Text : " + text)
# print("Shift pattern : " + str(s))
# print("Cipher: " + encrypt(text, s))

# print("character A", ord("A"))
# print("character Z", ord("Z"))

# res = 100 - 65
# print(res)
# res = res % -26
# print(res)

# print(-13 % 3)

print(ord("a"))
