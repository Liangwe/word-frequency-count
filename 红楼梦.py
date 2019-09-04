#红楼梦
print("红楼梦人物出场次数：")
import jieba                                #jieba库的应用
import time
import countname
start=time.perf_counter()
txt=open("红楼梦.txt","r",encoding="gb18030").read()
excludes={"他们","两个","知道","只见","如今","来到","一个","国王","我们",\
           "变成","你们","什么","一面","说道","那里","这个","出来","自己",\
            "这里","怎么","起来","不知","姑娘","没有","众人","不是","听见",\
          "就是","Page","就是","进来","咱们"}               #这些文字是多次程序运行所得
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="熙凤" :
        rword="凤姐"
    elif word=="老太太" :
        rword="贾母" #把意思相同的归为一个人
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
print("-----------------------------------")

