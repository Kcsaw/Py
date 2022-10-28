class LPR:
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
# 建立3隻寵物並儲存在 序列 之中這可以用白癡寫法而這是用迴圈 
cats=[]
    
for times in range(5):
    cats.append(LPR(input("請輸入寵物名="), eval(input("請輸入年紀=")), input("請輸入毛髮顏色="))) 

"""
for x in cats:
    print(x.name)
    print(x.age)
    print(x.color)
"""    

#找出年紀最大與最年輕者
maxcats=0
mincats=20

for x in cats:
    
    if(x.age>maxcats):
        maxname=x.name
        maxcats=x.age
    if(x.age<mincats):
        minname=x.name
        mincats=x.age
        
# 找出最大的年紀數字看懂沒LPR
print("{} 年紀最大者 {} 歲".format(maxname,maxcats))
print("{} 是年輕者為 {} 歲".format(minname,mincats))