'''
class Person():
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def show(self):
		print("%s %d"%(self.__name,self.__age))
	#@property
	def name(self):
		return self.__name
	def age(self):
		return self.__age

p1 = Person("123",10)
print(p1.name(),p1.age())
class Person2():
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def show(self):
		print("%s %d"%(self.__name,self.__age))
	@property
	def name(self):
		return self.__name
	def age(self):
		return self.__age
	@age.setter
	def age(self,age)
		self.__age = age
p2 = Person2("xx",156)
#print(p2.age())
print(p2.age)
p2.age = 100

class Person(object):
classmethod
@static
overload

class Person(object):
	#gouzaohanshu
	def __init__(self,name,age,height):
	#shilicansu
		self.__name = name
		self.__age = age
		self.height = height
	def show(self):
		print("%s %d"%(self.__name,self.__age))
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,name):
			self.__name = name

p1 = Person("aaa",12,25)
print(p1.height,p1.name)
p2=Person("bbb",15,85)
print(p2.name)
p2.name = "ddd"
print(p2.name)

class Person(object):
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def show(self):
		print("%s %d"%(self.__name,self.__age))
	@property
	def name(self):
		return self.__name
	def age(self):
		return self.__age
	@age.setter
	def age(self,age):
		self.__age = age
p1 = Person('kkk',12)
print(p1.age)
p1.age = 18
print(p1.age)
print(p1.name,p1.age)

super(student,self).__init__(name,age)
Person.__init__(self,name,age)
super().__init__(name,age)

class Person(object):
	def __init__(self,name,number,age,sex):
		self.name = name
		self.number = number
		self.age =age
		self.sex = sex

class PrimaryStudent(Person):
	def __init__(self):

	def study(self):
		print("studying")

	def fight(self):
		print("fighting")
		
	super().__init__(name,number,age,sex)
	
def __str__(self):
	return "%s %d"%(name,age)
	__str__ = __repr__

		
class Person(objice):
	def aaa(self):
		pass
	@classmethod
	def bbb(cls):
		pass
	@staricmethod
	def ccc()
		pass
d = Person()
d.aaa()
d.bbb()
d.ccc()
Person.bbb()
Person.ccc()

Singletion

singletion

class Person(object):
	def __init__(self)

__new__:


class Person(func):
		def inner():
			pass


def singletion(cls):
	def 

************
def singletion(cls)
	instance = {}
	def getInstance(*args,**kwargs):
		if cls not in instance
			instance[cls] = cls(*args,**kwargs)	
	return instance[cls]
return getInstance

@singletion

class Text(object)
	def __init__(self,name,age)
		self.name = name
		self.age  =age
*************

class Check(object):
		instance = None
		@classmethod
		def getInstance(cls,*args,**kwargs):
			if not cls.instance:
				cls.instance = cls(*args,**kwargs)
			return cls.instance

open(path,flag,encoding,errors)
path:daokailujing xiangduilujing
flag:dakaifangshi
	r:zhidu
	rb:yiserjinzhidu
	r+:duxie
encoding:bianmageshi [utf-8 gbk]

errors:cuowu  [try-excep]


zhuyi:wenjianduqudeshihou yidingshuyibianmafangshi,hewenjianbenshenbianmagehsi

f = open("zhixianhgshu.txt","r",encoding = "gbk")

duqumwnjianzhongdeneirong

result = f.read()
print(result)

1
guanbi zuoyong :wenjian duixiang zhanyong neicun kongjian
f.close()

f1 = open("xxx.txt","r+",encoding = "utf-8")
result1 = f1.read()
print(result1)

f1.close()


def singleton(cls):
	instance = {}
	def getinstance(cls,*args,**kwargs):
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)
		return instance[cls]
	return getinstance
@singleton
class Text(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
p1 = Text("sss",12)
p2 = Text("aaa",12)
print(id(p1) == id(p2))

def singletion(cls):
	instance = {}
	def getInstance(*args,**kwargs):
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)	
		return instance[cls]
	return getInstance

@singletion

class Text(object):
	def __init__(self,name,age):
		self.name = name
		self.age  =age

def singleton(cls):
	instance = {}
	def getinstance(*args,**kwargs):
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)
		return instance[cls]
	return getinstance
@singleton
class Text(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
p1 = Text("sss",12)
p2 = Text("aaa",12)
print(id(p1) == id(p2))


def singleton(cls):
	instance = {}
	def getIntance(*args,**kwargs):
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)
		return instance[cls]
	return getIntance
@singleton
class Text(object):
	def __init__(self,name):
		self.name = name
p1 = Text("ss")
p2 = Text("saa")
print(id(p1) == id(p2))

open(path,flag,encoding,errors)

f1 = open("filel.txt","r",encoding = "utf-8")
result = f1.read(2**10)
f1.close()

size = os.path.getsize("filel.txt")
print(size)

while size > 0:
		result1 = f1.read(16)
		print(result)
		size -= 16

result1 = f1.readline
print(result1)

result1 = f1.redline()

while result1
	print(result1)
	result1 = f1.redline()

result1 = f1.readline(5)
print(result1)

readlines

result1 = f1.readlines()
print(result1)

fanghuiyigelienbiao
neibuchongfudiaoyong readline()
read() read(1024) readline()

# # dakaiwnejian: open()
# # xieshushuju: write()
# w:xie fugai wb:erjinzhixei w+:duxie a:zhuijia
w = open("aaa.txt","w",encoding = "utf-8")

w.write("heheheheheh")

w.flush()

w.close()


with as 

with open("filel.text","r") as f:
	print(f.read())
#with shangxiawenguanli:tongguomouzhongfangshijianhuayichang
with open("xxx.txt","w",enconding = "utf-8") as w:
	w.write("sasdasdasd")
	f.flush()

class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def show(self):
		print("showing")
	@classmethod
	def text(cls):
		print("texting")
	@staticmethod
	def fun():
		print("funing")
p1 = Person("aaa",15)
p1.show()
p1.text()
p1.fun()
Person.fun()
Person.text()

def singleton(cls):
	instance = {}
	def getInstance(*args,**kwargs):
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)
		return instance[cls]
	return getInstance
@singleton
class Text():
	def __init__(self,name):
		self.name = name
p2 = Text("aaa")
p1 = Text("sss")

print(id(p1),id(p2))

def singleton(cls):
	instance = {}
	def getInstance(*args,**kwargs):
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)
		return instance[cls]
	return getInstance
@singleton
class Text(object):
	def __init__(self,name):
		self.name = name
p1 = Text("456")
p2 = Text("789")
print(id(p1) == id(p2))

class Check(object):
	def fun1(self):
		print('hhh')
	@classmethod
	def fun2(cls):
		print("456")
	@staticmethod
	def fun3():
		pass
p1 = Check()
p1.fun1()
p1.fun2()
p1.fun3()
Check.fun1("123")

class Person(object):
	instance = None
	def __new__(cls,*args,**kwargs):
		if not cls.instance:
			cls.instance = super(Person,cls).__new__(cls,*args,**keargs)
		return cls.instance
	def dance(self):
		print("dancing")
print("hello")

class Check(object):
	ff = 666
	def fun1(self):
		print(self.ff)
	@classmethod
	def fun2(cls):
		print("456")
	@staticmethod
	def fun3():
		pass
p1 = Check()
p1.fun1()
p1.fun2()
p1.fun3()
Check.fun1(p1)

mianxiangduixiang
kuapingtai
jiaohushi
jieshixing

age = 10
print(unm)
x = 3
y = 5
result = x*y
print(result)
  '''

# b1 = True
# b2 = False
# print(b1,b2)
# name1 = "ssss"
# name2 = name1
# print(name1,name2)
# name2 = "aaa"
# print(name1)
# print(name2)
# num = 100
# print(type(num))
# str0 = "123"
# r0 = int(str0)
# print(type(str0),type(r0))
# f0 = 1.23
# r1 = int(f0)
# print(type(r1))
# print(int(13.58))
# print(float(15))
# print(float("12.68"))
# print(float("145"))
# n = 49
# m = str(n)
# print(type(m))
# print("hello")
# print(100)
# print(True)
# print(False)
# print("10+20=",10+20)
# %d zhengxing
# %s zifuchuang
# %f fudianshu
# print("%d + %d =%d"%(num1 + num2 = num3))
# print("hhh"*3,"ssss")
# print("\"aaa\"")
# print("\'aaa\'")
# print("sss"+"sss")
# print("sss","sss","sssdd",sep = "%")
# name = input("shuru:")
# print(name)
# n = 1.17
# m = 2
# print(n + m)
# print(5/3)
# num = 10
# num /= 2
# print(num)
# print(3 <= 5)
# num1 = int(input("rushu:"))
# num2 = 21
# if num1 == num2:
# 	print("nizhongjiangle") 
# a = 1
# while a <= 9:
# 	b = 1
# 	while b <= a:
# 		print("%dx%d=%d"%(b,a,b*a),end ="" )
# 		b += 1
# 	print("")
# 	a += 1
# a = 10
# b = 20
# temp = a
# a = b
# # b = temp
# # print(a,b)
# a = 10
# b = 20
# a,b = b,a
# print(a,b)
# def custon(src_path,des_path):
# 	with open(src.path,"rb") as f1:
# 		content = f1.read()
# 	with open(des_path,"wb") as f2:
# 		f2.write(comtent)
# 		f2.flush()
# def singleton(cls):
# 	linshibianliang
# 	dict = {}
# 	def currentInstance(*args,**kwargs):
# 		if cls not in dict:
# 			dict[cls] = cls(*args,**kwargs)
# 		return dict[cls]
# @singletion
# nonlocal xxxxx

# csv:Comma Separate Valuse,
# fedian zaishiyong de guochengzhong zhifuzhijianshiyongdoughaogekai
# zhuyaoyongyubutongchengxuzhiian shujuijiaohu
# zaiwindowsxiakeyishiyongwxceldakai
# import csv
# def readCsv1(path):
# 	csvFile = open(path,"r")
# 	csvReader = csv.reader(csvFile)
# 	print(csvReader)
# 	print(type(csvReader))

# if __name__=="__main__":
# 	path = r"file,"
# def readCsv2(path):
# 	infoList = []
# with open(path,"r") as csvFile:
# 	csvReader = csv.read(csvFile)
# 	for item in csvReader:
# 		infoList,append(item)
# 		return 
# inport csv
# def writeCsv1(path):
# 	pass
# if __name__ == "__main__":
# 	path = 
# enum de biaozhuanku
# enum tiugongsle enum
# enum lei:yongyuchongdangfulei
# meiijuchengyuan meihucgangliangff

# from enum import Enum,Intenum,iique
# class 
# @unique
# REd
# ytiuchangchulu pibbi cuo,
# num = 10 
# print(num)
# print(num/0)
# print("over")

# AttributeError:yigeduixiangshitufnagwenleyige
# IOError:shuru shuchuyichang
# importError:daorumokuaiyichang
# indexError:
# keyError:
# ValueError:
# for i in range(len(l1)):
# 	dict1[l1[i]] = l2[i]
# print(dict1)
# a="sss   ssdasda   sadasd  aaassssss"
# b = a.strip("s")
# print(b)
# try:
# 	path = r"a.text"
# 	f = open(path,"r",encoding="UTF-8")

# 	result = f. read()
# except FileNotFoundError as e:
# 	print("aaa")
# except LookupError as e:
# 	print("bbb")
# except ValueError as e:
# 	print("ccc")

# finally:

# 	if f:
# 		F.close()
# a = "aaaaassssssxxssaxxxaaaa"
# print(a.index("xxx"))
# print(a.strip("a"))
# print()
# class Aaa(Except):
# 	def __init__(self,message):
# 		super(MyException,self).__init__()
# 		self.message = message
# print(int(1.9))
# print(float(1))
# print(int("123"))
# print(float("12.3")
# print(int("123"))
# print(int(1.9))
# # print(float(1))
# # print(int("123"))
# # print(float("12.3"))
# # s1 = "46546456465"
# # print(int())
# # import sys 
# # um1 = 10
# # str1 = "abc"
# # print(num1,str1,end="")
# # print("num1=%d,str1=%s"%(num1,str1))
# # print("kkk","kkk","kkk","kkk",sep="%")
# # # sep "fengge"
# # print("")
# # print("hhh",file=sys.stdout)
# # num1 = 0
# # while num1 < 10:
# # 	print(num1,end="")
# # 	num1 += 1
# # print("")
# # print("heheh")
# # n = 0
# # a = 0
# # while n <= 100: 
# # 	if n%2 == 0:
# # 		a += n
# # 	n += 1
# # print(a)
# # a = 0
# # b = 0
# # while a <=100:
# # 	if a%3 == 0 and a%7 == 0:
# # 		b += a
# # 	a += 1
# # print(b)
# # while 1:
# # # pass
# # a = 5
# # while a < 3:
# # 	print("hello")
	
# # else:
# # 	print("else")
# # b1 = 0
# # while b1 <= 3:
# # 	b2 = 0
# # 	while b2<5:
# # 		print("b1=%d,b2=%d"%(b1,b2))
# # 		b2 += 1
# # 	b1 += 1
# # a = 1
# # while a < 10:
# # 	b = 1
# # 	while b <= a:
# # 		print("%dx%d=%d"%(b,a,b*a),end="")
# # 		b += 1
# # 	a += 1
# # 	print("")
# # list1 = ["sss","bbb","aaaa","eee"]
# # n = 0
# # while n < len(list1):
# # 	print(list1[n])
# # 	n += 1
# def copy(src_path,des_path):
# 	srcFile = open(src_path,"r")
# 	desFile = open(des_path,"w")
# 	srcReader = csv.reader(srcFile)
# 	desWriter = csv.wirter(desFile)
# 	for item in srcReader:
# 		desWriter.wirterow(item)
# 	srcFile.close()
# 	desFIle.close()


# class MyException(Exception):
# 		def __init__(self,massage):
# 			super(MyException,self).__init__()
# 			self.massage = massage
# 		def __str__(self):
# 			return self.message
# # 		def handle(self):
# # 			pass 
# x = (y = z+1)
# x = y = z =1
# x = (y = 1)
# print(unm1)
# a=10
# isinstance(a)
# a = list(range(1,4))
# print (a)
# nonlocal
# import random
# 	random.choice(range(start,end,step))
# random.random()
# random.uniform()
# a='''a s s dddd     
# aas sddad s 
# aaaa'''
# print(a)
# def f(x,l=[]):
# 	for i in range(x):
# 		l.append(i*i)
# 	print(l)
# f(2)
# f(3,[3,2,1])
# f(3)
# a = range(5)
# for a in range(5):
# 	print(a)
# a = [1,2,3]
# b = [4,5,6]
# c = [a,b]
# print(c)
# d = copy.copy(c)
# print(id(d) == id(c))
# /t1 = ()
# dict1 = {"zhangshan":14,"lishi":45,"huawnag":50}
# # print(dict1["zhangshan"])
# # dict1["abc"] = 25
# # print(dict1)
# # result1 = dict1.get("zhanshan")
# # def age(dict1):
# # 	for i in dict1:
# # 		if i == "zhangshan":
# # 			print(dict1(i))
# a = int(input("shurugeshu"))
# for key,value in dict1.items():
# 	print(key,value)
# 	if value == 
# # import pickle
# class Person (object):
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def show(self):
# 		print("%s %d"%(self.name,self.age))
# p1 = Person("sss",19)
# p1.show()

# # pickle.dunp(obj,file)
# f1  = open("file1.text","wb")
# pickle.dump(p1,f1)
# # f2 = open("file1.text","rb")
# # reault = pickle.load(f2)
# # print(result)
# # print(type(result))
# # result.show()
# # f2.close()
# class Goods(object):
# 	def __init__(self,name,prick,balance):
# 		self.name = name
# 		self.price = price
# 		self.balance = balance
# 	def __str__(self):
# 	return"name:%s price:%d balance%d"%(self.name,self.prine,self.balance)






# class ShoppingCar(object):
# 	def __init__(self):
# 		self.shop_goodslist = {}
# 	def __str__(self):
# 	return"liebian:%s"%(self.shop_goodslist)







# class User(object):
# 	def __init__(self,username,uid,psw,Shoppingcar):
# 		self.username = username
# 		self.uid = uid
# 		self.psw = psw
# 		self.Shoppingcar = Shoppingcar
# 		self.islogin = False 

# def __srt__(self):
# 	return"%s %s %s %s %s"%(self.username,self.uid,self.psw,self.Shoppingcar,self.islogin) 




# import os

# def singletion(cls):
# 	instance = None
# 	def getInstance(*args,**kwargs)
# 		nonlocal instance
# 		if not instance;
# 			instance = cls(*args,**kwargs)
# 		return instance
# 	return getInstance
# 	instanceDict = {}
# 	def getInstance(*args,**keargs):
# 		if cls not in instanceDict:
# 		instanceDict[cls] = cls(*args,**keargs)
# 		return instanceDict[cls]
# 	return getInstance



# @singletion
# class Storage(object):
# 	def __init__(self):
# 		pass
# 	def init_goods(self):
# 		path = r"goods(path)"
# 		if not os.path.exists(path):
# 			self.goodsList = []
# 			named = ["mac","book","kindle","iphone"]
# 			prices = [20000,78,50,8888]
# 			balances = [100,80,65,89]

# 			for i in range(len(names)):
# 				goods = Goods(name[i],prices[i],balances[i])
# 				self.goodsList.append(goods)
# 			with open(path,"wb") as f:
# 				pickle.dump(self.goodsList,f)

# 		else:
# 			with open(path,"rb") as f:
# 				self.goodsList = pickle.load(f)
# def save_goods(self.goodsList,f)


# form 
# def user_login(self):
# 	uid = 
# if user.islogin:
# 	print("yijingdengluguo")
# 	return user
# psw = input("qingshurumumk")
# if name == user.username and psw == user.psw:
# 	print(dengluhenggong)
# 	user.islogin = True
# 	return user
# else:
# 	print(denglushibai,qiangshurizhengqiedemima)

# def add_goods(self):
# 	user = self.user_login()
# 	if user == None:
# 		print("qingxianjinxingdoeng,lu")
# 		return

# 	print('''
# 		0.aaaa
# 		1.bbbb
# 		2.cccc
# 		3.dddd
# 		''')
# 	index = int(input("qingshurubianhaoa"))
# 	storage = Storage()
# 	goods = storage.goodList[index]
# 	num = int(input("qingshurishuliang"))
# 	if unm <0:
# 		print("shuruyouwu")
# 	else:
# 		while num > goods.balance:
# 			num = int(input("shangpiindeshengyuliang:%d qingchongxinshurushuliang:"%(goods,balance)))
# 		else:
# 			user_goods = Good(goods.name,goods.price,num)
# # 	def del_goods1
# l1 = ["aaa","bbb","ccc","ddd","eee"]
# for i in range(1,len(l1)):
# 	if i%2 == 0:
# 		print(l1[i])
# b =int(len(l1)) 
# for a in range(1,b,3):
# # 	print(l1[a])
# l1 = ["aaa","bbb","ccc","ddd","eee"]
# l2 = ["aaa","ccc","ddd"]
# # l3 = []
# for a in l1:
# 	for b in l2:
# 		if a != b:
# 			l3 = l3.extand(a)
# 			print(l3)
# for a in range(len(l1)): 
# 	if l1[a] != l2:
# 		print(l1[a]) 

# for a in l1:
# 	if a not in l2:
# 		l3.append(a)
# 		print(l3)
# for a in l2:
# 	if a in l1:
# 		l1.remove(a)
# 		l3 = l1
# print(l3)


# l1 = ["aaa","bbb","ccc","ddd","eee"]
# l2 = ["aaa","ccc","ddd"]

# a = "abbcccdddd"
# dict1 = {}
# # l1 = list(a)
# # count(a)
# for i in a:
# 	b = dict1.get(i)
# 	if b == None:
# 		dict1[i] = 1
# 	else:
# 		dict1[i] += 1
# print(dict1)
# a = "tody is a good day tody is a good day tody is a good day tody is a good day"
# dict1 = {}
# list1 = a.split(" ")
# for b in list1:
# 	c = dict1.get(b)
# 	if c == None:
# 		dict1[b] = 1
# 	else:
# 		dict1[b] += 1
# print(dict1)
# l1 = [0,1,2,3,4,5,6,7,8,9,10]
# l2 = ["a","b","c","d","e","f","g","h"]
# dict2 = {}
# # for i in range(len(l1)):
# # 	dict2[l1[i]] = l2[i]
# # print(dict2)
# a = 0
# if len(l1) == len(l2):
# 	while a < len(l1):
# 		dict2[l1[a]] = l2[a]
# 		a += 1
# elif len(l1) > len(l2):
# 	while a < len(l2):
# 		dict2[l1[a]] = l2[a]
# 		a += 1
# elif len(l1) < len(l2):
# 	while a < len(l1):
# 		dict2[l1[a]] = l2[a]
# 		a += 1
# print(dict2)
# s1 = {1,2,3,4,5,6,7,8,9,91,254}
# # print(type(s1))
# s2 = set([3,3,2,5,5,8,4,3,1,2,1,3,5,4,3,4,3])
# print(s2)
# l = list(s2)
# # print(type(s2))
# list1 = []
# for i in l:
# 	list1.append(i)
# print(list1)
# s2.add({1000,123})
# print(s2)
# abs()
# max()
# min()
# pow(m,n)
# round()
# a = abs(-1.368)
# a = max(3,5,2,4,5,6,4,6,4,6)
# a = min(1,3,0,5,4,6,5,1,3,2,4,6,8,7,4)
# a = pow(2,8)
# a = round(1.768854)
# print(a)
# import math
# from math inport*
# ceil()
# floor()
# sqrt()
# import math
# a = ceil(21.5487564)
# print(a)
# import random
# print(random.choice(range(10,101)))
# print(random.randint(10,100))
# import random
# # print(round(random.random()*6+4,2))
# list1 = [1,2,4,5,5,6,4,6,4,3,2,1,6,5]
# # list2 = list1
# # a = range(len(list2))
# # for i in list1:
# # 	if i > list2[a]:
# # # 		print(i)
# max1 = list1[0]
# for i in list1:   
# # 	if max1 > i: 
# # 		max1 = max1
# 	if max1 < i:
# 		max1 = i
# print(max1)
# 	# if i > max1:
# 	# 	max1 = i
# print(max1)
# # print(list1)
# mix2 = 0
# for i in range(1,len(list1)):
# 	if list1[i] > max1:
# 		max1 = list1[i]
# 		max2 = i
# print(max1,max2)
# for a in range(len(list1)):
# 	if list1[a] == max1:
# 		print(a)
# list1 = [4,6,7,3,2,1,6,,8,7,4,41,6,8,5]
# map(function,Iterable)
# duizhifingddehandhu
# function
# interableiterable
# interable = "ableavlellllloe"
# l1 = [5,6,5,0,6,9,0,,9,5,5,6,8,4,3]
# for i in list1:
# 	l3.append(i**2)

# newlist3 = ()
# def func(x):
# 	return x**2
# map(func,list1)
# print(result)
# def func():
# 	return x**2
# 	redult = map(func,list1)
# 	print(reult)
# newList = list
# l1 = [54,6,8,4,5,4,8,97,4,6]
# def tex(x):
# 	return str(x)
# a = map(tex,l1)
# l2 = list(a)
# print(l2)

# l3 = []
# for b in l1:
# 	l3.append(str(b))
# print(l3)
# from functools import reduce

# l1 = [5,4,5,4,5,4]
# def f(x,y):
# 	return x*y
# a = reduce(f,l1)
# print(a)

# b = 1
# for i in l1:
# 	b *= i
# print(b)
# l1 = [1,3,5,7,9]
# def tex(x,y):
# 	return "x"+"y"
# a = reduce(tex,l1)
# print(a)

# def tex1(x):
# 	return str(x)
# l2 = list(map(tex1,l1))
# print(l2)

# def tex2(y,z):
# 	return y + z
# q = int(reduce(tex2,l2))
# print(q)
# print(type(q))
# l1 = [35,49,8,5,1,8,41,5,6,4,46,164]
# for i in range(len(l1)-1):
# 	for a in range(len(l1)-i-1):
# 		if l1[a] > l1[a + 1]:
# 			l1[a],l1[a + 1] = l1[a + 1 ],l1[a]
# print(l1)
# fileter (functiom, iterable)

# l1 = [1, 4, 5, 5, 6, 8, 8, 35, 41, 46, 49, 164]
# def tex(x):
# 	if x%2  == 0:
# 		return True
# 	return False
# a = list(filter(tex,l1))
# print(a)
# newList2 = list1.copy()
# for unm in newList2:
# 	if num%2 == 1:
# 		newList2.remove(num)
# print(newList2)
# newlist3 = [num for unm in list1 if num%2 == 0]
# print(newList3)

# l1 = [54,7,6,8,4,6,6,4]
# l2 = sorted(l1)
# print(l1)
# print(l2)
# l3 = sorted (l1,reverse = True)
# print(l3)

# list4 = [23,-54,-582,418,-21] 
# list5 = sorted(list4,key=abs)
# print(list5)

# list7 = sorted(list6,key = len,reverse = True)
# iterable
# b = "name"
# if b == "name":
# 	print(p1.name)
# __dict__(meiyeduixiangdouyougaishxing miaoshuzhidongduixiangde suoyouxinxi)

# print(P1.__dict__)
# print(p1.__dict__["name"])

# getattr(obj,name,default)
# value = getattr(p1,"name","xxx")
# value2 = getattr(p1,"age",23)
# print(value)


# @classmethod
# @staticmethod
# getaterr
# print(reflect 02.a.name)
# getattr(reflect02.a,"name")
# f = getattr(reflect02.a,"showing")
# c  = print

# a =input("hahahaah")
# res = hasattr(reflect03,news,op)
# 	if res:
# 		getattr(reflext03.news,op)
# 		print(f())
# 	else:
# 		print("hahahaah")
l1 = [65,7,1,3,2,419,87,6,46,8,7,3,1,8]
for i in range(len(l1)-1):
	for a in range(0,len(l1) - i - 1):
		if l1[a] > l1[a+1]:
			l1[a],l1[a+1] = l1[a+1],l1[a]
print(l1)
# l1 = [6,87,4,6,8,7,6,4,321,65,7]
# l2 = []
# a = range(len(l1))
# for i in l1:
# 	if l1[a] < i:
# 		print(i)
# 		l2.append(l1[a])
# 		l1.remove(l1[a])
# print(l1)
# print(l2)
# max1 = l1[0]
# for i in l1:
# 	if max1<i:
# 		max1 = i
# print(max1)


# list1 = [1,2,4,5,5,6,4,6,4,3,2,1,6,5]
# list2 = list1
# a = range(len(list2))
# for i in list1:
# 	if i > list2[a]:
# # 		print(i)
# import turtle
 
# turtle.color("red")
# turtle.pensize(6)
# turtle.speed(1)
# # turtle.shape("turtle")
# for i in range(len(list1)-1):
# 	for a in range(len(list1)-i-1):
# 		if list1[a]
# list1 = [5,4,6,43,13,4,1,3,54,6,14,54]
# newList = list1.copy()
# max1 = newList[0]
# for i in range(len(newList)):
# 	if newList[i] > max1:
# 		max1 = newList[i] 
# newList.remove(max1)
# print(newList) 
# list1 = [85,74,4,6]
# for i in range(len(list1)-1):
# 	for j in range(len(list1)-i-1):
# 		if list1[j] > list1[j+1]:
# 			list1[j],list1[j+1] = list1[j+1],list1[j]
# print(list1)


# left = 0 
# right = len(list1) - 1
# key = 20
# while left  <= right:
# 	middle = (left + right) // 2
# 	if list1[middle] > key:
# 		right = middle -1
# 	elif list1[middle] < key:
# 		left = middle + 1
# 	else:
# 		print(middle)
# key = 4
# for i in range(len(list1)):
# 	if list1[i] == key:
# 		pass
# 		# print(i)
# print(i)	
# l1 = [85,74,4,6,8,4,6,5,4,6,8,4,68]
# l2 = l1.copy()
# l3 = []
# while l2 != []:
# 	max1 = l2[0]
# 	for i in range(len(l2)):
# 		if l2[i] > max1:
# 			max1 = l2[i]
# 	l3.append(max1)
# 	l2.remove(max1)
# print(l3)
# print(l2)

# a = "sssss"
# b = "fffff"
# c = a + b
# print(c)

# print(r"dd$d%d/ddd\tddd\dd/dd")
# a = "sssadasdasdasdasdasdasd"
# print(len(a))
# print("heHHKKLlloasdasda".upper())
# print("aklsjdhasSDLKFHSDIFSkughui".lower())

# a = "sadsdasdasd sas"
# b = ""
# for i in a:
# 	num = ord(i)
# 	num -= 32

# 	b += chr(num)
# print(b)
# index("afafa")
# print(a.strip("s"))
# print(a.index("g"))

# a = "ssdasdsaasasdasdas"
# b = a.split("d")
# print(b)
 
# c = ""
# a = c.join(b)
# print(a)

# b = a.replace("s","h",5)
# print(b)
# if a.isdigit() == False:
# 	print("aaaaa")
# str = "this IS a Test"
# print(len(str))
# num = 0
# for i in range(len(str)):
# 	if str[i] == "a":
# 		num +=1
# print(num)
# a = "abc"
# if str[0] == a[0]:
# 	if str[1] == a[1]:
# 		if str[2] == a[2]:
# 			print("shi")
# else:
# 	print("bushi")
# # str1 = ""
# # for j in range(len(str)):
# # 	if ord(str[i]) > 125:
# # 		str1 += str[i]
# # 		if ord(str[i]) < 125:
# # 			ord(str[i])
# str2 = str.replace(i,a)
# print(str2)
# str1 = "this IS a Test"
# print(len(str1))
# print(str1.count("a"))
# print(str1.startswith("abc"))
# print(str1.lower())
# print(str1.replace("this","that"))
# print(str1.find("c"))

# time = "23:59:49"
# list1 = time.split(":")
# print(list1)
# hour = int(list1[0])
# minute = int(list1[1])
# seconds = int(list1[2])

# seconds += 1
# if seconds == 60:
# 	seconds = 0
# 	minute += 1
# 	if minute == 60:
# 		minute = 0
# 		hour += 1
# 		if hour == 24:
# 			hour = 0

# print("%.2d:%.2d:%.2d"%(hour,minute,seconds))
# # tcp : Transmission control protocol                                                         
# def trx(a,b):
# 	return a + b
# print(trx(1,2))
# trx(1,2)
# def myPrint():
# 	print("ssss")
# print(myPrint())
# def show1():
# 	print("111")
# 	show3()
# 	print("aaa")
# def show2():
# 	print("222")
# 	show1()
# 	print("bbb")
# def show3():
# 	print("333")
# 	print("ccc")
# show2()

# a = trx(1,2)
# print(a)

# 222
# 111
# 333
# ccc
# aaa
# # bbb
# def func(a):
# 	a = 1
# temp = 20
# func(temp)
# print(temp)

# def fun2(x):
# 	x[2] = 100
# 	print(x)
# x = [10,20,30,14]
# fun2(x)
# print(x)

# def num(a,b,c):
# 	print(a,b,c)
# num(1,2,3)
# num(a=1,c = 2,b = 3)
# import __hello__
# import socket
# sercerSocket = socket.socket()
# sercerSocket.bind(("10.12.152.104",6666))
# sercerSocket.listen(7)
# print("hehehehe")
# clientSocket,clientAddress = sercerSocket.accept()
# print("%s--%s"%(str(clientSocket),str(clientSocket)))
# while True:
# 	clientData =clientSocket.recv(1024)
# 	print("hhhh:"+ clientData.decode("utf8"))
# 	sendData = input("ssdsadasda")
# 	clientSocket.send(sendData.encode("utf8"))
# 	clientData = clientSocket.recv(1024)



# import socket
# clientSocket = socket.socket()
# clientSocket.connect(("10.12.152.104",6666))
# while True:
# 	data = input("ssasdasdasdasdas")
# 	clientSocket.send(data.encode("utf8"))
# return

# def num(a,b):
# 	return a + b
# num(10,20)
# print(num(10,20))show1
# def func(a):
# 	if a < 0:
# 		print("aaa")
# 	elif a>10:
# 		print("bbb")
# 	else:
# 		print("ccc")
# a = func(4)
# print(a)
# def add(a,b):
# 	return a+b

# sum = lambda num1,num2:num1 +num2
# print(sum(1,2))





# def num1(a,b):
# 	if a > b:
# 		print(a)
# 	elif a < b:
# 		print(b)
# 	else:
# 		print("%d=%d"%(a,b))
# a = num1(1,2)
# print(a)

# def year(a):
# 	if a%4 == 0:
# 		if a%100 != 0:
# 			print("yes")
# 		elif a%400 == 0:
# 			print("yes")
# 		else:
# 			return "no"
# 	elif a%400 == 0:
# 		print("yes")
# 	else:
# 		return "no"

# a = year(1600)
# print(a)


# def isleapyear(year):
#  	if (year%4 == 0 and year%100 !=0) or year % 400 == 0:
#  		print("yes")
#  	else:
#  		print("no")
# a = isleapyear(1900)
# print(a)



# def unm2(c):
# 	d = 0
# 	for i in range(1,c + 1):
# 		if i%3 == 0:
# 			d += 1
# 	print(d)
# 	return d	
# e = unm2(10)
# print(e)

# def mun1(i):
# 	c = 0
# 	for a in range(1,i + 1):
# 		if a%1 == 0 and a%a == 0:
# 			c += 1
# 	return c
# 	print(c)
# mun1(10)

# def unm(a):
# 	if a > 1:
# 		result = True
# 		for i in range(2,a): 
# 			if a % i == 0:
# 				result = False
# 				break
# 		return result
# 	else:
# 		return True
# def getnum(n):
# 	c = 0
# 	for i in range(1,n+1):
# 		if unm(i):
# 			c += 1
# 	return c
# print(getnum(1000))

# def zhishu(a):
# 	if a > 0:
# 		result = True
# 		for i in range(2,a):
# 			if a%i == 0:
# 				result = False
# 				break
# 		return result
# 	else:
# 		return False
# def geshu(n):
# 	c = 0
# 	for i in range(1,n+1):
# 		if zhishu(i):
# 			c += 1
# 	return c
# geshu(1000)
# print(gesh`u(1000))
# def test(a,b,fun):
# 	return fun(a) + fun(b)
# print(test(43,-27,abs))
# def fun1():
# 	def fun2(a,b):
# 		s = a + b
# 		print(s)
# 	return fun2
# f = fun1()
# print(f(1,2))

# num1 = 4
# def func1():
# 	global num1
# 	print(num1)

# 	num1 = 20
# func1()
# a = 10
# def test():
# 	global a
# 	a = a +1
# 	print(a)
# test()
# x = 0
# def outer():
# 	x = 1
# 	def inner(): 
# 		nonlocal x
# 		x = 2
# 		print("inner:",x)
# 	inner()
# 	print("outer",x)
# outer()
# print("global",x)



# nonlocal
# global

# import time
# def test():
# 	print("hello")

# def outer(func):
# 	def inner():
# 		t1 = time.time()
# 		func()
# 		time.sleep(2)
# 		t2 = time.time()
# 		print(t2-t1)
# 	return inner
# f1 = outer(test)
# f1()



# def outer(person):
# 	def inner(a):
# 		a = abs(a)
# 		person(a)
# 	return inner
# @outer
# def person(age):
# 	print(age)
# # f = outer(person)
# # f(36)
# # f(-58)
# person(-86)

# def outer(func): 
# 	def inner(*args,**kwargs):
# 		func(*args,**kwargs)
# 		print("hahahaha")
# 	return inner
# @outer

# def test(a,b,c):
# 	print(a+b+c)
# test(1,48,1)

# list1 = [i**2 for i in range(2,20,2)]
# print(list1)
# list2 = [x**2 for x in range(1,20) if x%2 == 0]
# print(list2)
# l1 = ["heai","KLJId","JUINd","SDIJ",587]
# l2 = [i.lower() for i in l1 if isinstance(i,str)]
# print(l2)
# l2 = []
# for i in l1: bbbbb
# 	i.lower()
# 	l2.append(i.lower())
# print(l2) 
# i = "ssHHHH"
# r = i.lower()
# print(r)
# def test(n):
# 	for i in range(1,n + 1):
# 		print(i)
# 	return "end"
# t = test(5)
# print(t)
# def a():
# 	print("ssss")
# 	a()
# a()

# import itertools
# list1 = [1,2,3,4]
# itertools.permutation(list1,3)
# print(result)
# print(list(result))

# t=10**10
# print(t)
# def checkQQ(qq):
# 	result = True
# 	try:
# 		mum = int(qq)
# 		if len(qq) > 5 and len(qq) <= 11:
# 			if qq[0] == "0":
# 				result = False
# 	except BaseException as e:
# 		result = False

# 		result = re.match(r"",qq)
# import re
# re.(r"[1][3-9]{10}")
# def qinhua(a):
# 	result = True
# 	if a.isdigit():
# 		if len(a) == 11:
# 			if a[0] == "1":
# 				if a[1] in ["0","1","2","9"]:
# 					result = False
# 			else:
# 				result = False
# 		else:
# 			result = False
# 	else:
# 		result = False
# 	return result	

# re.match(r"[1][3-8]%d{9}",phone)

# def aaa(n):
#    if n ==1 or n ==2:
#    	return 1
#    else:
# 		result = aaa(n-1) + aaa(n-2)
# 		return result
# print(re.search(r""))
# print(re.search(r"day","tody is a good day"))
# print(re.search(r"day$","tody is a good day"))
# print(re.findall(r"\Atody","tody is a good day\ntody is a good day\ntody is a good day",re.M))
# print(re.findall(r"tody","tody is a good day\ntody is a good day\ntody is a good day",re.M))
# print(re.findall(r"day","tody is a good day\ntody is a good day\ntody is a good day",re.M))
# print(re.findall(r"tody","tody is a good day\ntody is a good day\ntody is a good day",re.M))
# c = 0
# def num(b):
# 	c = 0
# 	for a in range(1,b+1):
# 		c += a
# 	print(c)
# 	return c
# print(num(3))

# a = 3
# b = 0
# # c = range(1,a + 1)
# for c in range(1,a+1):
# 	b += c
# print(b)

# def xxx(i):
# 	n = 1
# 	x = 0
# 	while n <= i:
# 		x += n
# 		n += 1
# 	return x
# print(xxx(10))

# print(type(c))
# def num1(a):
# 	if a >= 1:
# 		result = a + num1(a -1)
# 	else:
# 		return 0
# 	return result
# print(num1(89))

# def num2(b):
# 	if b == 1:
# 		return 1
# 	else:
# 		return b + num2(b-1)
# print(num2(-3))

# import os
# dirPath = 
# fileList =  os.listdir(dirPath)

# if __name__ == "__main__":
# 	print(6676)
# class Person(object):
# 	age = "aaa"
# 	__slots__ = ("name")
# 	def show(self):
# 		print("ssssss")

# p1 = Person()
# print(p1.age)
# p1.abc = "heheheeh"
# print(p1.abc)

# class Student():
# 	name = ""
# 	age = 0
# 	hobby = ""
# 	def show(a):
# 		print("a")
# p1 = Student()
# name = "xiaohua"
# age = 12
# haihao = "tiqiu"
# print(p1.name,p1.age,p1.hobby,p1.show())

# class Teacher():
# 	name = ""
# 	def let(self,a):
# 		print(name +"rang" + a + "ziwojieshao")


# class Student():
# 	name = "111"
# 	age = 20
# 	hobby = "ssss"
# 	def show():
# 		print("showing")
# 	def	inturduce():
# 		print("hehehehe")

# name = ""
# def func(a):
# 	print(a.name)
# p1 = func(1)
# print(p1)
# def run(self):
# 	print(id(self))
# 	print("running")
# a = 10
# s = 2*3.14*a
# print(s)
# a = 20
# b = 20
# if a > b:
# 	print(a)
# elif a < b:
# 	print(b)
# else:
# 	print("%d=%d"%(a,b))
# a = 40
# b = 30
# max = a
# if a < b:
# 	max = b
# else:
# 	max = a
# print(max)
# import random
# a = random.choice(range(1,4))
# print(a)
# print("1.aaa 2.bbb 3.ccc")
# b = 30
# i = 0
# while  b >= 5:
# 	b = b//2
# 	i += 1
# 	print(i)
# 	print(b)
# print(i)
# a = 3.4
# b = 2.8
# c = 1

# print(a + b + c)
# 18
# 10010011
# 11101100
# 11101101
# 00010010
# import random
# num = 4
# n = 0
# x = random.randint(1,2)
# while n >= 5:
# 	if num > x:
# 		print("dale")
# 	elif num < x:
# 		print("xiaole")
# 	else:
# 		print("ok")
# 	n += 1

    # *
#    ***
#   *****
#  *******

# for i in range(1,5):
# 	for j in 
# list1 = [5,34,6,8,4,6,34,63]
# # min = list1[0]
# # for i in list1:
# # 	if i < min:
# # 		min = i
# # 	else:
# # 		min = min
# # print(min)
# # a = set(list1)num = int(input("shuru"))
# # print(a)
# for i in range(0,len(list1)-1):
# 	for j in range(len(list1)-i-1):
# 		if list1[j] < list1[j+1]:
# 			list1[j],list1[j+1] = list1[j+1],list1[j]
# print(list1)
# def getInstance(*args,**kwargs): 
# 	instance = {}
# 	if cls not in instance:
# 		instance[cls] = cls(*args,**kwargs)
# 	return instance[cls]
# return getInstance 
# class Person(object):
# 	def __init__(self,name,age):
# 		self.__name = name
# 		self.__age = age
# 	def myperson(self):
# 		print("%s %s"%(self.__name,self.__age))
# 	@property
# 	def name(self):
# 		return self.__name
# 	@name.setter
# 	def name(self):
# 		self.__name = name
# 	@property
# 	def age(self):
# 		return self._age
# 	@age.setter
# 	def age(self):
# 		self.__age =age
	
# p1 = Person("bbb",14)
# p1.name = "hhh"
# p1.myperson()

# def outer(b):
# 	def inner(a):
# 		a = abs(a)
# 		print(a)
# 	return inner
# p1 = outer(b)
# p1(-15)

# def outer(person):
# 	def inner(a):
# 		a = abs(a)
# 		person(a)
# 	return inner
# f1 = other(person)
# f1(16)

# @outer
# def person(age):
# 	print(age)
# # f = outer(person)
# # f(36)
# # f(-58)
# person(-86)
# l1 = [2,546,73,28,65,235,73,5,89]
# def zhushu():
# 	l2 = []
# 	for i in l1:
# 		for j in range(2,i):
# 			if i%j == 0:
# 				False
# 			else:
# 				l2.append(i)
# 	return l2


# def shuchu():
# 	a = set(l1)
# 	l3 = list(a)
# 	return l3



# l4 = []
# def oushu():
# 	for i in l1:
# 		if i%2 == 0:
# 			l4.append(i)
# 	return l4




# for i in range(len(l1)-1):
# 	for j in range(len(l1)-i-1):
# 		if l1[j] > l1[j+1]:
# 			l1[j],l1[j+1] = l1[j+1],l1[j]

# str1 = "absdsd"
# num1 = 0
# for i in str1:
# 	if i == "o":
# 		num1 += 1
# str2 = str1[::-1]
# for j in range(len(str1)):
# 	if str1[j] == str2[j]:
# 		result = True
# 	else:
# 		result = False
# 		# break
# print(result)

# str3 = str1.split()
# print(str3)
# str4 = ""
# for i in str3:
# 	j = i.capitalize()
# 	str4 += (" "+j)
# with open("text","wb",encoding = csv)

# with open("file.source.text","r") as:
# 	a = source.read()
# with open("source_copy.text","w",encoding = "utf8")
# 	source-copy.wirter(a)
# class DictClass(object):
# 	def __init__(self,dict1,key):
# 		self.dict1 = dict1
# 		self.key = key
# 	def chaxun(self):
# 		for key in self.dict1.keys():
# 			if self.key == key:
# 				return self.dict1[key]
# 			else:
# 				return "not find"
# 	def shanchu(self):
# 		self.dict1.pop(self.dict1[self.key])
# 	def liebiao(self):
# 		list1 = []
# 		for key in self.dict1.keys():
# 			list1.append(self.dict1[key])
# dict = DictClass({"aaa":1,"bbb":2,"ccc":3},"ccc")
# dict.chaxun()
# dict.liebiao()
# def search
# time1 = "23:39:59"
# timelist = time1.split(":")
# h = int(timelist[0])
# m = int(timelist[1])
# s = int(timelist[2])
# s += 1
# if s == 60:
# 	s = 0
# 	m += 1
# 	if m == 60:
# 		m = 0
# 		h +=1
# 		if h == 24:
# 			h = 0
# print("%.2d:%.2d:%.2d"%(h,m,s))
# s1 = set({1,2,3,4,56,6,66})
# s1.add(555)
# s1.add(11)
# print(s1)
# def myPrint(str,age = 18):
# 	print(str,age)
# myPrint("kaige")

# def a():
# 	a() += 1
# 	return a()
# def fun1():
# 	print("hello world")
# def outer():
# def func1():
# 	print("hello")
# def func2():
# 	print("*************")
# 	func1()
# func2()	
# def outer(func):
# 	print("*******")
# 	func()
# func1 = outer(func1)
# def say(age):
# 	print("%s hello"%(age))
# say(-10)

# def outer(a):
# 	def inner(age):
# 		if age > 0:
# 			pass
# 		else:
# 			age = 0
# def outer(func):
# 	def inner(age):

# def outer(a):
# 	def inner(age):
# 		if age < 0:
# 			age = 0
# 		a(age)
# 	return inner
# say = outer(say)
# say(-10)
# def outer(func):
# 	def inner(*args,**kwargs):
# 		print("########")
# 		func(*args,**kwargs)
# 	return inner
# @outer
# def func1(a,b):
# 	print("%s = %s"%(a,b))
# func1(1,3)
# print(int("1111",base = 2))

# def int2(num,base = 2):
# 	return int(num,base)
# print(int2("11111"))
# try except else
# try:
# 	pass
# except Exception as e:
# 	raise
# else:
# 	pass
# finally:
# 	pass

# f= open(path,"w")
# f.write("")
# f.close()
# encode()
# decode()
# def sum1():
	# sun() += sum()+1

# def main():
# 	pass

# a = eval("1+1")
# print(a)

# import tkinter
# win = tkinter.Tk()

# win.mainloop()
# list1 = [1,23,4,5,8,2]
# print(sorted(list1))
# print(sorted(list1,reverse = True))
# list1 = [0,1,2,3,4]
# list2 = []
# str1 = ""
# str2 = "01234"
# for i in range(len(str2)):
# 	a = 0
# 	i = 0
# 	if a < 5 i < 5:
# 		a = str1[i]
# 		a += 1

# print(str1)
# list1 = [0,1,2,3,4]
# a = range(len(list1))
# print()

# a = range(0,5,1)
# print(a)
# str1 = ""
# str2[i] = 
# str1 = "00000"
# a = range(0,5,1)
# str1[1] = a
# print(str1)
# list1 = [0,1,2,3,4]
# str1 = ""
# if i < 5:
# 	str2 = str1+str(i)
# 	print(str2)
# 	i += 1
# i = 0
# while i < 5:
# 	str1 = i
# import itertools
# mylist = list(itertools.permutations([1,2,3,4]),3)
# print(mylist)
# list1 = [0,1,2,3,4]
# list2 = [0,0,0,0,0]
# i = range(len(list1))
# m = 0
# for i in range(len(list1)):
# 	list2[m] = list1[i]
# 	m += 1
# print(lsit2)
# list3 = ["s","a","r"]
# list2 = []
# for a in list3:
# 	for b in list3:
# 		for c in list3:
# 			list1 = [a,b,c]
# 			list2 += list1
# print(list2)
a = 30*200/5
print(a)