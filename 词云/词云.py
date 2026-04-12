import jieba
import wordcloud
w=open('.txt','r',encoding='utf-8')
F=w.read()
w.close()
words=jieba.lcut(F)
word=[word for word in words if len(word)>1]
t=' '.join(word)
T=wordcloud.WordCloud(font_path='msyh.ttc',width=1000,height=700,background_color='white',\
                      stopwords={'和','的'})
T.generate(t)
T.to_file('ciyun.png')
