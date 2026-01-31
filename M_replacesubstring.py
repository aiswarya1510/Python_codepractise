# def replacesubstring(word, substring, toplace):
#     newword=word
#     i=0
#     while(i<len(word)):
#         if word[i]==substring[0]:
#             j=1
#             k=i
#             while(j<len(substring)):
#                 if word[k+1]==substring[j]:
#                     k=k+1
#                     if j==len(substring)-1:
#                         flag=True
#                         i=k
#                     continue
#                 else:
#                     break
#             if flag==True:
#                 newword=newword[:k]

#         else:
#             i=i+1





# replacesubstring("abc", "abc", "a")







def replacesubstring2(word,substring,toplace):

    if substring in word:
        word=word.replace(substring,toplace)   #we are allocating it back to word because string is immutable
        return word
    return f"{word} does not have {substring} in to replace with {toplace}"

print(replacesubstring2("abc", "abc", "a"))


