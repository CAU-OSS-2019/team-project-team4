from konlpy.tag import Okt
from gensim.models import Word2Vec
import gensim
import glob
import csv

# load data
okt = Okt()
nlp_dataList = []
path = 'nlp_train_data/*.txt'
files = glob.glob(path)
for name in files:
    f = open(name, 'r', encoding='utf-8-sig')
    # rdr = csv.reader(f)
    rdr = f.readlines()
    for line in rdr:
        tokens = okt.pos( line[line.find('> ') + 2:] )
        lineList = []
        for keyword, type in tokens:
            if type == 'Noun' or type == 'Verb' or type == 'Adjective' or type == 'Adverb':
                lineList.append(keyword)
        if lineList:
            nlp_dataList.append(lineList[:])
        lineList.clear()
    f.close()
print('-----------------------------------END-------------------------------------')

# make w2v model
w2v_model = gensim.models.Word2Vec()
w2v_model.build_vocab(nlp_dataList)
w2v_model = Word2Vec(nlp_dataList, size=100, window=3, min_count=5, workers=4, sg=1)
w2v_model.save('w2v_model')

# show examples
model = gensim.models.Word2Vec.load('w2v_model')
a = model.wv.most_similar("승리")
a = model.wv.get_vector("승리")
print(a)

