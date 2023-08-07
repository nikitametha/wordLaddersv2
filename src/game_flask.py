# Main file for game hosted on localhost - run this to run flask server
import pickle
import random
import networkx as nx
from flask import Flask,request, render_template


st_en_words=[0,0] # holds start and end word
curr_ladder=[]
won_flag=0
helpguess=""

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


app = Flask(__name__,template_folder='templates', static_folder='static')


@app.route("/", methods=['GET', 'POST'])
def index():
    while True:
        try:
            start_word=random.choice(word_list)
            end_word=random.choice(word_list)
            global ll
            ll=nx.shortest_path(net, start_word, end_word)
            print("Start Word: ",start_word)
            print("End Word: ",end_word)
        except nx.NetworkXNoPath:
            continue
        break
    st_en_words[0]=start_word
    st_en_words[1]=end_word
    # print(ll)
    global curr_word_index, won_flag, curr_ladder
    curr_word_index=1
    won_flag=0
    curr_ladder=[]
    curr_ladder.append(start_word)
    print("Current Word Ladder: ",curr_ladder)
    return render_template("index.html",st_en_words=st_en_words,ll=ll)


@app.route('/result', methods = ['POST', 'GET'])
def result():
      result = request.form
      res=[]; res2=1
      w1=(result['startwrd']).lower()
      w2=(result['endwrd']).lower()
      if(w1 in word_list and w2 in word_list):
          try: res=nx.shortest_path(net, w1, w2)
          except nx.NetworkXNoPath: res2=-1 # there's no path between the words
      else: res2=0 #either or both words not in our wordlist data
      res1=(res)
      

      return render_template("result.html",res1 = res1, res2=res2)

@app.route('/playgame',methods = ['POST', 'GET'])
def playgame():
    # print("in playgame the words are = ",st_en_words[0])
    print("Current Word Ladder: ",curr_ladder)

    return render_template("playgame.html",st_en_words=st_en_words,ll=ll,curr_ladder=curr_ladder)


@app.route('/calculate',methods = ['POST', 'GET'])
def calculate():
    global won_flag 
    global curr_word_index
    if request.method == 'POST':
        if request.form['submitbutton'] == 'Show me the next word':
            #hintt =ll[curr_word_index] - not necessary since it word be added show up on word list anyway
            curr_ladder.append(ll[curr_word_index])
            curr_word_index+=1
            if(curr_word_index==len(ll)):  
                won_flag=1
                return render_template("win_game.html")
            else:
                
                return render_template("playgame.html",st_en_words=st_en_words,ll=ll,won_flag=won_flag,curr_ladder=curr_ladder)
        if request.form['submitbutton'] == 'Check Word!':
            result = request.form
            t=result['guesswrd']
            global helpguess
            if (t.lower()==ll[curr_word_index] and t.lower() not in curr_ladder):
                curr_ladder.append(t.lower())
                curr_word_index=curr_word_index+1
                # print(curr_ladder)
                if(curr_word_index==len(ll)):
                    won_flag=1
                    return render_template("win_game.html")
                else:
                    helpguess="Correct Guess!"
            else:
                # print("incorrect word, give hint")
                if(len(ll[curr_word_index-1])<len(ll[curr_word_index])):
                    helpguess="Try again! Add a letter to '"+ str(ll[curr_word_index-1]) +"'"
                elif(len(ll[curr_word_index-1])>len(ll[curr_word_index])):
                    helpguess="Try again! Delete a letter from '"+ str(ll[curr_word_index-1]) +"'"
                else:
                    helpguess="Try again! Change a letter in '"+ str(ll[curr_word_index-1]) +"'"
            return render_template("playgame.html",st_en_words=st_en_words,ll=ll,won_flag=won_flag,helpguess=helpguess,curr_ladder=curr_ladder)




if __name__ == '__main__':
   app.run(port=8000,debug = True)
