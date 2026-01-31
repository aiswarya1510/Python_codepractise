def nonrepeat(word):
   if word=="":
      print("empty string")
   track=""
   word_2=sorted(word)
   i=0
   if len(word)==1:
      print(word[0])
   while(i<len(word_2)-1):
      if word_2[i]==word_2[i+1]:
         track=word_2[i]
      elif(word_2[i]!=word_2[i+1] and word_2[i]!=track):
         print(word_2[i])
      i=i+1

   if len(word_2)-1==i:
         print(word_2[i])

    
     

         
         

    
        


# nonrepeat("a b c d")



def nonrepeat2(word):
   ret=""
   my_dict={}
   for c in word:
      if c in my_dict:
         my_dict[c]=my_dict[c]+1
      else:
         my_dict[c]=1


   for key,val in my_dict.items():
      if val==1:
         ret=ret + str(key)
   return ret


print(nonrepeat2("aabbcge"))



'''
dictionary is ordered from 3.7,
use len function to fimd the lenght
values can be of any type  eg: "val" : ["red","blue"],
thisdict = dict(name = "John", age = 36, country = "Norway")
x = thisdict["model"]
x = thisdict.keys() -- gets a list of keys,
x = thisdict.values() --Get a list of the values
x = thisdict.items() --method will return each item in a dictionary, as tuples in a list.
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary"),
thisdict.update({"year": 2020}),
thisdict.pop("model") -- will remove the specified key,
thisdict.popitem() -- remove last inserted item,
del thisdict["model"] -- specified key
thisdict.clear() -- empties
del this_dict --> deletes entire dictionary,
for x in thisdict:
  print(x)  --- prints key
for x in thisdict:
  print(thisdict[x])  -- prints value
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
for x, y in thisdict.items():
  print(x, y)
mydict = thisdict.copy()
print(mydict)  -- to make copy wihtout referencing
mydict = dict(thisdict)
print(mydict) -- also to make copy
print(myfamily["child2"]["name"])  -- for nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])



'''


      
         
      

