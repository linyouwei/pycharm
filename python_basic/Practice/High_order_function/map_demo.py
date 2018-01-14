#encoding=utf8
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(n):
    return n[:1].upper()+n[1:].lower()
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

