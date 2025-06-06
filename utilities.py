import hashlib

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def append_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)

def create_file(filename, content=""):
    with open(filename, "x") as file:
        file.write(content)

def hashing(text):
    hashed = hashlib.new("SHA256")
    hashed.update(text.encode())
    return hashed 

#caesar cypher algorithm    
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)
