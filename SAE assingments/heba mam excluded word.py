exclude_list=['is','are','am','of','as','on','a']
sent=input('enter a sentence')
sent_list=sent.lower().split()
new_list=[]
for each in sent_list:
    if each not in exclude_list:
        new_list.append(each)
print(" ".join(new_list))
