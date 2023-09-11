import re#正则表达式，用规则去匹配字符串

"""
match
匹配字符串开头是否有所需字符
"""
s = "dad is altertive from parent"
result = re.match("dad",s)
print(result.span())#(0, 3)
print(result.group())#dad
print(result)#<re.Match object; span=(0, 3), match='dad'>

"""
search
匹配字符串中第一次出现的所需字符
"""
result01 = re.search("from",s)
print(result01.span())#(17, 21)
print(result01.group())#from
print(result01)#<re.Match object; span=(17, 21), match='from'>

"""
findall
匹配字符串中出现的所需字符,返回值是一个列表
"""
result03 = re.findall("e",s)
print(result03)#['e', 'e', 'e']

"""
元字符匹配
"""
#   .  任意一个非（\n）字符
#   []  匹配[]中列举的字符
#   \d  匹配数字，即0——9
#   \D  匹配非数字
#   \s  匹配空白，即空格，tab键
#   \S  匹配非空白
#   \w  匹配单词字符，即a-zA-Z0-9
#   \W  匹配非单词字符

s = "itheima1 @@python2 !!666 ##itccast3"

#   \d  匹配数字，即0——9
fin01 = re.findall(r'\d', s)   # 字符串前面带上r的标记，表示字符串中转义字符无效，就是普通字符的意思
print(fin01)#['1', '2', '6', '6', '6', '3']

#   \W  匹配特殊字符
fin02 = re.findall(r'\W', s)
print(fin02)#[' ', '@', '@', ' ', '!', '!', ' ', '#', '#']

#找出所有英文字母
fin03 = re.findall(r'[a-zA-Z]',s)
print(fin03)#['i', 't', 'h', 'e', 'i', 'm', 'a', 'p', 'y', 't', 'h', 'o', 'n', 'i', 't', 'c', 'c', 'a', 's', 't']


#   *   匹配前一个规则的字符出现0到无数次
#   +   匹配前一个规则的字符出现1到无数次
#   ?   匹配前一个规则的字符出现0到1次
#   {m}   匹配前一个规则的字符出现m次
#   {m,}   匹配前一个规则的字符出现至少m次
#   {m,n}   匹配前一个规则的字符出现m到n次

#边界匹配
#   ^   匹配字符串开头
#   $   匹配字符串结尾
#   \b   匹配一个单词的边界
#   \B   匹配非单词边界

#分组匹配
#   |   匹配左右任意一个表达式
#   ()  将括号中字符作为一个分组

"""
案例
"""
# 匹配账号，只能由字母和数字组成，长度限制6到10位
r = '^[0-9a-zA-Z]{6,10}$'
s = '123456_'
print(re.findall(r, s))
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '123453678'
print(re.findall(r, s))
# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
# abc.efg.daw@qq.com.cn.eu.qq.aa.cc
# abc@qq.com
# {内容}{内容}{内容}.{内容}{内容}{内容}{内容}@{内容}.{内容}.{内容}
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
#[\w-]表示即a-zA-Z0-9和-
# s = 'a.b.c.d.e.f.g@qq.com.a.z.c.d.e'
s = 'a.b.c.d.e.f.g@126.com.a.z.c.d.e'
print(re.match(r, s))


