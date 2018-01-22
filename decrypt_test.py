import itertools
import rsa

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
    try:
        r=rsa.decrypt(rsa.enc_message,p,q)
        print(r)
        output.write(p+ ","+q+": "+r)
    except Exception:
        pass
output.close()