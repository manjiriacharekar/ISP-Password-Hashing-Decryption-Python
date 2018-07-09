#Manjiri Acharekar - msa530



import hashlib

#open files

#linkd for reading the given SHA1.txt
#linkedin_passwords.txt to retrieve the passwords output file
#dictionary reads the customized generated password list by script password_customlist.py

linkd = open('SHA1.txt', 'r')
dictionary = open('password_custom.txt', 'r')
password = open('linkedin_passwords.txt', 'a')

#count for less than 1000 passwords
cnt = 0

#Create set to store sha1 hashed values
hash_sha1 = set()
for line in linkd:
  hash_sha1.add(line.strip()) 

for line in dictionary:
  # Convert password from custom list to hash value 
  custom_hashed = hashlib.sha1(line.strip().upper())		
  #upper can be changed to lower or title to get more combinations
  
  #compare if any hash value matches with the SHA1.txt values
  if custom_hashed.hexdigest() in hash_sha1 and cnt < 1000:
    cnt = cnt + 1
	#if it matches add to output file
    password.write(custom_hashed.hexdigest() + " " + line + "\n")
    print str(cnt) + "\t" + custom_hashed.hexdigest().ljust(70) + line + "\n"

#alternate printing
if cnt != 0:
  print 'Cracking Completed...' + '\n' + str(cnt) + " " + 'Passwords Found'
else: 
  print 'No Passwords Found'

linkd.close()
dictionary.close()
password.close()  
  
  