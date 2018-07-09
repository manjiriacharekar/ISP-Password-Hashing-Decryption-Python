#Manjiri Acharekar - msa530


import random
 
#names.txt is the combined file of 'Commonly used English words' and 'Common First Names' 
#open the file to save the generated passwords 
 
r = random.SystemRandom()
password = open('password_custom.txt','a')
 
 
# define all functions
# created 23 functions with different combinations 
#1W 1C 2N FC
def gen_passwd1(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    charstr = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if chars:
        charstr.insert(r.randint(1,9), r.choice(chars))

    return ''.join(commonwords+charstr+numstr1+numstr2).title()
 
#2W 1C 1N FIRST CAPS
def gen_passwd2(words, max=50000, k=2, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    charstr = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if chars:
        charstr.insert(r.randint(1,9), r.choice(chars))

    return ''.join(commonwords+charstr+numstr1).title()

#1W 1C 3N FIRST CAPS
def gen_passwd3(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    numstr3 = []
    charstr = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr3.insert(r.randint(1,9), r.choice(numbs))
    if chars:
        charstr.insert(r.randint(1,9), r.choice(chars))

    return ''.join(commonwords+charstr+numstr1+numstr2+numstr3).title()
 
#1W 1C 2N ALL CAPS
def gen_passwd4(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    charstr = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if chars:
        charstr.insert(r.randint(1,9), r.choice(chars))

    return ''.join(commonwords+charstr+numstr1+numstr2).upper()
 
#1W  ALL CAPS
def gen_passwd5(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    return ''.join(commonwords).upper()

#1W 0C 3N ALL CAPS
def gen_passwd6(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    numstr3 = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr3.insert(r.randint(1,9), r.choice(numbs))

    return ''.join(commonwords+numstr1+numstr2+numstr3).upper()

#3N 1W 3N LOWER
def gen_passwd7(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    numstr3 = []
    numstr4 = []
    numstr5 = []
    numstr6 = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr3.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr4.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr5.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr6.insert(r.randint(1,9), r.choice(numbs))

    return ''.join(numstr1+numstr2+numstr3+commonwords+numstr4+numstr5+numstr6).lower()

#3N 1W LOWER
def gen_passwd8(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    numstr3 = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr3.insert(r.randint(1,9), r.choice(numbs))

    return ''.join(numstr1+numstr2+numstr3+commonwords).lower()

#1W 4N LOWER
def gen_passwd9(words, max=50000, k=1, numbs=None, chars=None, first_upper=True):
    commonwords = r.sample(words[:max], k)
    
    numstr1 = []
    numstr2 = []
    numstr3 = []
    numstr4 = []
    
    if numbs:
        numstr1.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr2.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr3.insert(r.randint(1,9), r.choice(numbs))
    if numbs:
        numstr4.insert(r.randint(1,9), r.choice(numbs))

    return ''.join(commonwords+numstr1+numstr2+numstr3+numstr4).lower()

# 2 words 2 numbs 1 character LOWER
def gen_passwd10(words, max=500000, k=2, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))    
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))

    return ''.join(elems)

# 1 words 2 numbs 1 character lower
def gen_passwd11(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))    
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))

    return ''.join(elems)

# 2 words 1 numbs 1 character lower
def gen_passwd12(words, max=500000, k=2, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))    
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))

    return ''.join(elems)


# 1 words 1 numbs  first caps
def gen_passwd13(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))
    if first_upper:
            elems[0] = elems[0].title()

    return ''.join(elems)


#1 word, 1 number lowercase
def gen_passwd14(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))

    return ''.join(elems)

# 2 words 2 numbs  lower
def gen_passwd15(words, max=500000, k=2, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))
    if numbs:        
            elems.insert(r.randint(1, len(elems)), r.choice(numbs)) 

    return ''.join(elems)

#1 word 1 number 1 character lower
def gen_passwd16(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))			
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))

    return ''.join(elems)

#1 word 3 number 1 character lower
def gen_passwd17(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))            
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))

    return ''.join(elems)


#2 word 1 number  lower
def gen_passwd18(words, max=500000, k=2, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))  
			
    return ''.join(elems)

#1 word upper
def gen_passwd19(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)

    return ''.join(elems).upper()

#1 word 3 number  lower
def gen_passwd20(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))  

    return ''.join(elems)

#1 word 3 number  upper
def gen_passwd21(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))  

    return ''.join(elems).upper()

#1 word 1 number 1 character first caps
def gen_passwd22(words, max=500000, k=1, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))
    if first_upper:
        elems = elems[0].title()

    return ''.join(elems)

#2 word 2 number 1 character first caps
def gen_passwd23(words, max=500000, k=2, numbs=None, chars=None,
                      first_upper=True):
    #generates random password
    elems = r.sample(words[:max], k)
  
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if numbs:
            elems.insert(r.randint(1, len(elems)), r.choice(numbs))           
    if chars:
            elems.insert(r.randint(1, len(elems)), r.choice(chars))
    if first_upper:
        elems = elems[0].title()

    return ''.join(elems)


if __name__ == '__main__':
    with open('names.txt') as f:
        words = [w.strip() for w in f]
    cnt= 0  

#call all the functions	and print the number of passwords generated
    for i in range(1,1000000):
        password.write(gen_passwd1(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd2(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd3(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd4(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd5(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd6(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd7(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd8(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd9(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd10(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd11(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd12(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd13(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd14(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd15(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd16(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd17(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd18(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd19(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd20(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd21(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd22(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		password.write(gen_passwd23(words, numbs='0123456789', chars='!@#$%')+"\n")
		cnt = cnt + 1
        print cnt
		
    
       
 #close the file       
    password.close()