#Manjiri Acharekar - msa530



import hashlib
import string

#open files

#dictionary for reading the given password.file
#yahoo_passwords.txt to retrieve the passwords

dictionary = open ('password.file','r')
password = open('yahoo_passwords.txt','w')

#password.write('cnt' + '\t\t' + 'Original text'.ljust(70) + '\t\t' + 'Password' + '\n')
#password.write('***************************************************************************************** \n')

#count for less than 1000 passwords
cnt = 1

array = []
var = False

#check where to start such that redundant data is ignored
check = "1:ac1@associatedcontent.com:@fl!pm0de@"

for line in dictionary:
        line = line.strip()
        if line == check:
                var = True
        if var == True and cnt <= 1000:
                #line = line.strip()
				# split line by ':'
                array = line.split(":")
                passwd = array[2]
				
				#print in the format informed in the question 
                password.write(line +' '+ passwd + '\n')
				
                #password.write(str(cnt) + '\t\t' + line.ljust(70) + '\t\t' + passwd + '\n')
                cnt = cnt + 1
                #print('\n')
				
dictionary.close()
password.close()				
				
				
				