#Manjiri Acharekar - msa530


import hashlib

#open files

#frm_sprng for reading the given formspring.txt
#formspring_passwords.txt to retrieve the passwords output file
#dictionary reads the customized generated password list by script password_customlist.py

frm_sprng = open('formspring.txt', 'r')
dictionary = open('password_custom.txt', 'r')
password = open('formspring_passwords.txt', 'a')

#Initialise Variables
#salt values to be appended with the passwords ...random values
#count for less than 1000 passwords
cnt = 0
salt1 = 0x30
salt2 = 0x30

#Create set to store sha1 hashed values
hash_sha256 = set()
for line in frm_sprng:
  hash_sha256.add(line.strip()) 

cnt = 0

#salt values less than 99
while (salt2 <= 99):
    while (salt1 <= 99):
        for line in dictionary:
            #Append Salt values to custom passwords and then hashed
            custom_hashed = hashlib.sha256(chr(salt1) + chr(salt2) + line.strip().upper())
			#upper can be changed to lower or title to get more combinations
			
            #compare if any hash value matches with the formspring.txt values
            if custom_hashed.hexdigest() in hash_sha256:
                cnt = cnt + 1
                if cnt < 1001:
                    #password found and print to output file
                    password.write(custom_hashed.hexdigest()+ " " + line.strip() + "\n")
					#alternateprint
                    print str(cnt) + "\t" + custom_hashed.hexdigest()+ "\t" + line.strip().ljust(100) + "\n"
                else:
                    #exit if more than 1000 passwords
                    exit()
        dictionary.seek(0,0)
        salt1 = salt1 + 1
    salt2 = salt2 + 1
    salt1 = 0x30
	
	#adjusting salt values

frm_sprng.close()	
dictionary.close()
password.close()