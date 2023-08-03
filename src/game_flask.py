import pickle
import random
import networkx as nx
from flask import Flask,request, render_template


x=[0,0]
g=[]
hintt=0
won=0
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


@app.route("/")
def index():
    while True:
        try:
            f1=random.choice(word_list)
            f2=random.choice(word_list)
            global ll
            ll=nx.shortest_path(net, f1, f2)
            print("Start Word: ",f1)
            print("End Word: ",f2)
        except nx.NetworkXNoPath:
            continue
        break
    x[0]=f1
    x[1]=f2
    global leng
    leng=len(ll)
    print(ll)
    global rr, won, g
    rr=1
    won=0
    g=[]
    return render_template("index.html",x=x,leng=leng,ll=ll)


@app.route('/result',methods = ['POST', 'GET'])
def result():
      result = request.form
      res=[]; res2=1
      w1=(result['startwrd'])
      w2=(result['endwrd'])
      if(w1 in word_list and w2 in word_list):
          try: res=nx.shortest_path(net, w1, w2)
          except nx.NetworkXNoPath: res2=-1 # there's no path between the words
      else: res2=0 #either or both words not in our wordlist data
      res1=(res)

      return render_template("result.html",res1 = res1, res2=res2)

@app.route('/playgame',methods = ['POST', 'GET'])
def playgame():
    print("in playgame the words are = ",x[0])
    print("the ladder is  = ", ll)
    return render_template("playgame.html",x=x,ll=ll)


@app.route('/calculate',methods = ['POST', 'GET'])
def calculate():
    global won
    global rr
    if request.method == 'POST':
        #hint next word button is pressed
        if request.form['submitbutton'] == 'Show me the next word':
            hintt =ll[rr]
            g.append(ll[rr])
            rr+=1
            if(rr==len(ll)):  
                print("won in hints!")
                won=1
                return render_template("index.html",x=x,ll=ll)
            else:
                print("didn't win just yet")
                return render_template("playgame.html",x=x,ll=ll,hintt=hintt,won=won,g=g)
        if request.form['submitbutton'] == 'Check Word!':
            print("entered to check word")
            result = request.form
            t=result['guesswrd']
            global helpguess
            if (t in ll and t not in g):
                print("new guess")
                g.append(t)
                rr=rr+1
                print(g)
                if(rr==len(ll)):
                    print("won!")
                    won=1
                    return render_template("index.html",x=x,ll=ll)
                else:
                    print("correct guess")
                    helpguess="Correct Guess!"
            else:
                print("incorrect word, give hint")
                if(len(ll[rr-1])<len(ll[rr])):
                    helpguess="Try again! Add a letter!"
                elif(len(ll[rr-1])>len(ll[rr])):
                    helpguess="Try again! Delete a letter"
                else:
                    helpguess="Try again! Change a letter!"
            print("rendering template")
            return render_template("playgame.html",x=x,ll=ll,won=won,helpguess=helpguess,g=g)




if __name__ == '__main__':
   app.run(port=8000,debug = True)
