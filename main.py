
while 1:
    try:
        m=int(input("四大名著：红楼梦，水浒传，三国演义，西游记编号为1-4，输入编号："))
        
    
        if 1<=m<=4:
            if m==1:
                with open('红楼梦.py','r',encoding="utf-8") as f:
                    exec(f.read())
                    break
            elif m==2:
                with open('水浒传.py','r',encoding="utf-8") as f:
                    exec(f.read())
                    break
            elif m==3:
                with open('三国演义.py','r',encoding="utf-8") as f:
                    exec(f.read())
                    break
            else:
                with open('西游记.py','r',encoding="utf-8") as f:
                    exec(f.read())
                    break
        else:
            continue
    except:
        print('数据有误,请重新输入')
        
