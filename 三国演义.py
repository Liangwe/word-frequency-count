#三国演义
print("三国演义人物出场次数：")
import jieba                                #jieba库的应用
import time
import countname
start=time.perf_counter()
txt=open("三国演义.txt","r",encoding="gb18030").read()
excludes={"将军","却说","二人","后主","上马","不知","天子","大叫","众将","不可",
          "主公","蜀兵","只见","如何","商议","都督","一人","汉中","不敢","人马",
          "陛下","魏兵","天下","今日","左右","东吴","于是","荆州","不能","如此",
          "大喜","引兵","次日","军士","军马"}                #这些文字是多次程序运行所得
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孟德" or word=="丞相":
        rword="曹操"                             #把意思相同的归为一个人
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

