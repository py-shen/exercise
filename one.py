
# 从1-n整数中取出m个整数，我的写法
def random_int(n, m):
	from random import randint
	result = ''
	for i in range(1, m+1):
		if m <= n:
			data = randint(1, n)
			result = (str(result) + ' ' + str(data))
		elif m > n:
			print('error')
			quit()
	print(result)

n = int(input('请输入n的参数：'))
m = int(input('请输入m的参数：'))
random_int(n, m)

# 从1-n整数中取出m个整数，超级简单的写法！！！！
# import random
# print(random.sample(range(1, 50), 30))

# 对random_int()的结果进行去除相同数字，并进行排序
