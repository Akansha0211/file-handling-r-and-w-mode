#write() method
#  1. r+ mode
'''earlier in file " akansha saxena was written '''
a=open('aak.txt','r+')
a.write("second love")  #writes something in file in r+ mode it overwrites the characters
a.close()

'''
output
second loveena
'''
# 2. w+ mode
#earlier in file " akansha saxena was written.

b=open('code.txt','w+') # overwrite the complete file
b.write("coding is future")
b.close()
'''
output
coding is future
''''

