with open ('poem.txt','r') as f:
   dict={}

   for line in f:
      tokens=line.split(' ')
      for token in tokens:
         if(token in dict):
            dict[token]+=1

         else :
            dict[token]=1
      

   print(dict)
   print(2+dict['Two'])