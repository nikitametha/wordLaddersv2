# Run this on terminal 'python3 game_terminal.py' to play the game on the terminal ONLY.
import pickle
import random
import networkx as nx

reader= open('../data/word_data.txt', 'r')
with open("../data/preprocessed_words.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)


word_list=[]

net = nx.Graph()
for words in reader:
    for word in words.split():
        word_list.append(word)
        net.add_node(word)


for k,v in b.items():
    for v_i in v:
        net.add_edge(k,v_i)
x=0
ll=[]


print("WELCOME\nSELECT DIFFICULTY\nLEVEL: 1 (HARD)\nLEVEL: 2 (EASY)\n")
inp=input("TYPE 1 OR 2: ")
if(inp=="1"): inp=1
elif(inp=="2"): inp=2
else:
    input("Wrong input, type 1 or 2: ")

#DIFFICULTY LEVEL MAX--any length
if(inp==1):
    while True:
        try:
            f1=random.choice(word_list)
            f2=random.choice(word_list)
            ll=nx.shortest_path(net, f1, f2)
            print("Start Word: ",f1)
            print("End Word: ",f2)
        except nx.NetworkXNoPath:
            continue
        break


#DIFFICULTY LEVEL EASY-- SELECT THE LENGTH OF WORD LIST TO BE USED
if(inp==2):
    print("TODO\n")

g=[]
g.append(f1)
rr=1
print("Type 1 to give up the next word!")
print("Make the bridge!")
t=(input()).lower()


while(g!=ll):
    if(t=="1"):
        print(ll[rr])
        g.append(ll[rr])
        rr=rr+1
        print(g)
        if(rr==len(ll)):
            print("You won!\n")
            break
    elif (t.lower()==ll[rr] and t.lower() not in g):
        g.append(t)
        rr=rr+1
        print(g)
        if(rr==len(ll)):
            print("You won!\n")
            break
        else:
            print("Correct!")
    else:
        if(len(ll[rr-1])<len(ll[rr])):
            print("Try again! Add a letter!")
        elif(len(ll[rr-1])>len(ll[rr])):
            print("Try again! Delete a letter")
        else:
            print("Try again! Change a letter!")
    t=input()
     
