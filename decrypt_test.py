import itertools
import rsa
import enchant
import nltk

#english words
dict_words=enchant.Dict("en-US")
file_primes=open("export.txt",'r')
primes_string=file_primes.readlines()
primes_list=[]
for i in range (0,len(primes_string)):
    line_no_n=primes_string[i][:len(primes_string[i])-1]
    #print(line_no_n)
    primes_list.extend(line_no_n.split("\t"))
#primes_list=primes_string.split("\t")
#print(primes_list)
file_primes.close()

combinations=itertools.combinations(primes_list, 2)
combinations=list(combinations)
#print(list(combinations))
#print(rsa.enc_message)
output=open("output.txt","w")
for comb in combinations:
    p=int(comb[0])
    q=int(comb[1])
    print(p)
    print(q)
    #if p>71 and q>73:
    #    break
    #elif p>71 or q>73:
    #    continue
    try:
        if p*q == rsa.public_key:
            r=rsa.decrypt(rsa.enc_message,p,q)
            words = r.split(" ")
            suspect_word=False
            for word in words:
                if dict_words.check(word):
                    suspect_word=True
                    break
            #print(r)
            output.write(str(p)+ ","+str(q)+": "+r+"\n")
            if (suspect_word):
                print("suspect")
                output.write("suspect\n")
                break

    except Exception, e:
        #print(str(e))
        pass
output.close()