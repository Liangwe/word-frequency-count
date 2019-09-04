#西游记
print("西游记人物出场次数：")
import jieba
import time
import countname
start=time.perf_counter()
txt=open("西游记.txt","r",encoding="gb18030").read()
excludes={"一个","那里","怎么","我们","不知","两个","甚么","只见","不是",
          "原来","不敢","闻言","如何"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="行者" or word=="大圣" or word=="老孙":
        rword="悟空"
    elif word=="师父" or word=="三藏" or word=="长老":
        rword="唐僧"
    elif word=="和尚" or word=="呆子":
        rword="沙僧"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

a=[]
b=[]
for i in range(100):
    word,count=items[i]
    if (i<11):
        print("{0:<10}{1:>5}次".format(word,count))
        a.append(word)
        b.append(count)
    else:
        a.append(word)
        b.append(count)
        
countname.showNameBar(a[0:10],b[0:10])
countname.Ciyun(' '.join(a))

dur=time.perf_counter()-start
print("运行时间为{:.2f}s".format(dur))

