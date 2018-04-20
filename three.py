text = 'aAsmr3idd4bgs7Dlsf9eAF'
# 从字符串中取出数字，重新组成字符串

#第一种做法，常规写法
num = ''
for i in text:
	if i.isdigit():
		num += i
print(num)

#第二种，简化写法
list = ''.join([i for i in text if i.isdigit()])
print((list))

# 第三种，正则表达式
import re
L = ''.join( re.findall(r'[\d|.]+', text))
print(L)

