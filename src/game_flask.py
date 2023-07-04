import pickle
import random
import networkx as nx
from flask import Flask,request, render_template

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
x=[]
ll=[]
ll2=[]

app = Flask(__name__,template_folder='templates', static_folder='static')

@app.route("/")
def index():
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
    x=[]
    x.append(f1)
    x.append(f2)
    leng=len(ll)
    ll2=" ".join(ll)
    
    return render_template("index.html",x=x,leng=leng,ll=ll2)


@app.route('/result',methods = ['POST', 'GET'])
def result():
      result = request.form
      res=[]; res2=1
      w1=(result['startwrd'])
      w2=(result['endwrd'])
      if(w1 in word_list and w2 in word_list):
          try: res=nx.shortest_path(net, w1, w2)
          except nx.NetworkXNoPath: res2=-1
      else: res2=0
      res1=(res)
      
      return render_template("result.html",res1 = res1, res2=res2)

if __name__ == '__main__':
   app.run(port=8000,debug = True)
