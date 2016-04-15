#python教程
  
2.4元组：不可编序列
   
   元组不能更改，
   
   列表用[]元组用（）
   
   tuple函数和list函数功能基本一样。


find可以在较长的字符串中查找字串。如果没有返回-1

可以通过replace（“替换前”，“替换后”）来改变字符串

split（“+”）去除+

“   abcd   ”.strip()

"abc"


通过dict可以用来创建字典

fromkeys给指定的键创建字典
dict.fromkeys(["name","age"],"unknow")


reversed用来反转字符串


一个字符串创建字典要求，首字母对尾字母

a=list("abcd")

b=list(reversed("abcd"))

c=dict(zip(a,b))


pop用来可以获得给定键的键值，并删除。




    peopel={
	  "A":{
	  "phone":"123",
	  "addr":"23hao"
	  },
	  "B":{
	  "phone":"456",
	  "addr":"45hao"
	  },
	  "C":{
	  "phone":"789",
	  "addr":"67hao"
	  }
     }

    labels={
	  "phone":"phone number",
	  "addr":"address"
	 }
    name=raw_input("name:")

    request=raw_input("phone number(p) or address(a)?")

    if request =="p":key="phone"
    if request =="a":key="addr"

    if name in people:print"%s's %s is %s."\
    (name,labels[key],people[name][key])

字典的copy创建一个新的字典，与之前的字典没有关系。





