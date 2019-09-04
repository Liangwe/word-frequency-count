#水浒传
print("水浒传人物出场次数：")   
import jieba
import time
import countname
start=time.perf_counter()
txt=open("水浒传.txt","r",encoding="gb18030").read()
excludes={"二人","一个","来到","人马","你们","我们","好汉",
          "知府","什么","他们","银子","梁山","两个","只见",
          "如何","那里","说道","众人","这里","出来","小人","今日","兄弟"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="哥哥":
        rword="宋江"
    elif word=="头领":
        rword="林冲"
    else:
        rword=word
        counts[word]=counts.get(word,0)+1
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
print("-----------------------------")
