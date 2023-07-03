# To generate pickled file 'preprocessed_words.txt' - no need to run this code if you have this file.
import time
start = time.time()
import pickle

from nltk import edit_distance
reader= open('../data/word_data.txt', 'r')
all_words=dict()
word_list=[]
for words in reader:
    for word in words.split():
        word_list.append(word)
curr_len=4

for i in range(0,len(word_list)):
    all_words[word_list[i]]=[]
    word_len=len(word_list[i])
    if(word_len==curr_len): 
        print("All "+(curr_len-1)+"length words done preprocessing.")
        print(time.time()-start)
        curr_len=curr_len+1
    for j in range(i,len(word_list)):
        if(len(word_list[j])-word_len>1):
            break
        else:
            edit_dist=edit_distance(str(word_list[i]),str(word_list[j]))
            if(edit_dist==1):
                all_words[word_list[i]].append(word_list[j])


with open("../data/preprocessed_words.txt", "wb") as fp:   #Pickling
  pickle.dump(all_words, fp)