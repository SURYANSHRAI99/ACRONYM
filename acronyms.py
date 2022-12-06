def fxn(stng):
   
    # get all words
    lst = stng.split()
    oupt = ""
     
    # iterate over words
    for word in lst:
       
        # get first letter of each word
        oupt += word[0]
         
    # uppercase oupt
    oupt = oupt.upper()
    return oupt
 
 
# input string
inpt1 = "COMPUTER SCIENCE ENGINEERING"
 
# output acronym
print(fxn(inpt1))
 
# input string
inpt1 = "GEEKS FOR GEEKS"
 
# output acronym
print(fxn(inpt1))
 
# input string
inpt1 = "LOVELY PROFESSIONAL UNIVERSITY"
 
# output acronym
print(fxn(inpt1))
