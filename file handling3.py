#write() method
#  1. r+ mode
'''earlier in file " akansha saxena was written '''
a=open('aak.txt','r+')    #CODE 
a.write("second Dove")  #writes something in file in r+ mode it overwrites the characters
a.close()

'''
output
second Doveena
'''
# 2. w+ mode
#earlier in file " akansha saxena was written.

#CODE
b=open('code.txt','w+') # overwrite the complete file
b.write("coding is future")
b.close()
'''
output
coding is future
'''

