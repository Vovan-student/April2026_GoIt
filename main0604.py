sentence = "The quick brown fox jumps over the lazy dog"
length = 0
gaps = 0

for i in sentence:
   if i!=" ":
       length = length + 1
   else:
       gaps = gaps + 1
       
print("The length of the sentence is:", length)
print("The number of gaps in the sentence is:", gaps)
