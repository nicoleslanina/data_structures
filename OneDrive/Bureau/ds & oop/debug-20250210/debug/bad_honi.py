'''
HONI block

Consider a series of four consecutive letters of some word that make up the 
subword HONI (case sensitive) is called the HONI-block. 

Given a string by the user, throw out as many letters as you want (it might be
none), so that in the end there are as many HONI-blocks as possible in the word.  

upgrade to: 
--> where HONI-block is not case sensitive.  
--> let user provide any sub-block
'''


word = input('enter string: ').lower()
sub_block = input('Enter the sub block we are looking for: ').lower()
block_count = 0 
i = j = 0  

while i < len(word) and j < len(sub_block):
    if word[i] == sub_block[j]:   
        if j!= len(sub_block)-1:    
            j = j + 1               
        else: 
            j = 0                
            block_count = block_count + 1   
    i = i + 1              
print(f'number of HONI-blocks: {block_count}')