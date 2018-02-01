# rsa python example
# following tutorial https://www.docdroid.net/Hb50yD1/criptografia-criptografia-rsa.pdf#page=2
import ascii
import math_op as mo
import codify as cd
import printer as pr

def encrypt(string, _p, _q):
    # define two prime numbers
    p = _p
    q = _q
    # n is the product between p and q, the public key
    n = p * q
    #get totient function
    tn=mo.totient_function(p,q)
    #choose an 'e' value, that cannot be common divisor with tn
    e = mo.choose_e(tn)
    #convert the message into asc characters
    string_to_asc = ascii.convert_to_asc(string)
    #encrypt message
    encrypted_chars=cd.codify(string_to_asc, e, n)
    #pr.parameters("ENCRYPTED PARAMETERS", p,q,n,tn,e)
    return encrypted_chars
    # prev_string=ascii.convert_to_string(string_to_asc)

def decrypt(enc_chars, _p, _q):
    # define two prime numbers
    p = _p
    q = _q
    # n is the product between p and q, the public key
    n = p * q
    # get totient function
    tn = mo.totient_function(p, q)
    # choose an 'e' value, that cannot be common divisor with tn
    e = mo.choose_e(tn)
    # find d, the modular multiplicative inverse
    d = mo.modinv(e, tn)
    #decrypts message
    decr_chars=cd.codify(enc_chars,d,n)
    decr_message=ascii.convert_to_string(decr_chars)
    #pr.parameters("DECRYPTED parameters", p,q,n,tn,e,d)
    return decr_message

p=601
q=653
#x=encrypt("I'm sexy and I know it",17,23)
enc_message=encrypt("Lili is a nickname for Lisandra", p, q)
print(enc_message)
public_key=p*q

#decr_message=decrypt(enc_message, p, q)
#print(decr_message)



