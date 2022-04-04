# 1-list comprehension\列表的元素可以在一行中循环遍历
% % time
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_Numbers = [number for number in numbers if number % 2 == 0]
print(even_Numbers)

# 同样可以使用字典、几何和生成器来完成推动是
dictionary = {'first_num': 1, 'second_num': 2,
              'third_num': 3, 'fourth_num': 4}
oddvalues = {key: value for (key, value) in dictionary.items() if value % 2 != 0}
print(oddvalues)

# 2-Enumerate枚举函数
sentence = 'Just do it'
length = len(sentence)
for index, element in enumerate(sentence):
    print('{}:{}'.format(index, element))
    if index == 0:
        print('The first element!')
    elif index == length - 1:
        print('The last element!')


# 3-通过函数返回多个值
# 方法一：返回元组
def get_student(id_num):
    if id_num == 0:
        return '君', '云朵'
    elif id_num == 1:
        return '猴子', '小'
    else:
        raise Exception('没有雪深的id是：{}'.format(id_num))


student = get_student(0)
print('名字：{}，姓氏：{}'.format(student[0], student[1]))


# 方法二
def get_data(id_num):
    if id_num == 0:
        return {'first_name': '君',
                'last_name': '云朵',
                'title': '数据STUDIO',
                'department': 'A',
                'date_joined': '20201001'}
    elif id_num == 1:
        return {'first_name': '猴子',
                'last_name': '小',
                'tile': '机器学习研习院',
                'department': 'B',
                'date_joined': '20201019'}
    else:
        raise Exception('没有员工的id是：{}'.format(id_num))


employee = get_data(0)
print('first_name:{}, \nlast_name:{}, \ntitle:{}, \ndepartment:{}, \ndata_joined:{}'.format(
    employee['first_name'], employee['last_name'],
    employee['title'], employee['department'],
    employee['date_joined']
))

# 4-像在数学中一样比较多个数字
x = 5
print(1 < x < 30)

# 5将字符串转换为字符串列表

import ast


def string_to_list(string):
    return ast.literal_eval
    (string)


string = '[[1,2,3],[4,5,6]]'
my_List = string_to_list(string)
print(my_List)

# 6 For-Else方法 检查是否存在偶数
number_List = [1, 3, 7, 9, 8]

for number in number_List:
    if number % 2 == 0:
        print(number)
        break
    else:
        print('No even numbers!')

number_List = [1, 3, 7, 9, 8]

number_List1 = [number for number in number_List if number % 2 == 0]
print(number)

# 07 从列表中找到N个最大/最小的元素

import heapq

numbers = [80, 25, 68, 77, 95, 88, 30, 55, 40, 50]
print(heapq.nlargest(5, numbers))
print(heapq.nsmallest(5, numbers))


# 08 函数参数以列值传递
def Summation(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum


result = Summation(*[8, 5, 10, 7])

print(result)

# 09 重复整个字符串
value = '数据STUDIO'
print(value * 3)
print('_' * 31)

# 10 从列表中找到元素的索引
cities = ['Vienna', 'Amsterdam', 'Paris', 'Berlin']
print(cities.index('Berlin'))

# 11 在同一行打印多个元素
print('数据', end='')
print('STUDIO')
print('数据', end=' ')
print('STUDIO')
print('Data', 'science', 'Machine', 'Learning', sep=',')

# 12 分割大数字以易于阅读
print(5_000_000_000_000)
print(7_543_291_635)

# 13反转列表的切片
sentence = '数据STUDIO 云朵君'
print(sentence[21:0:-1])

# 14 'is'和'=='的区别
list1 = [7, 9, 4]
list2 = [7, 9, 4]
print(list1 == list2)
print(list1 is list2)
list3 = list1
print(list3 is list1)

# 15在一行代码中合并2个字典
first_dct = {'London': 1, 'Paris': 2}
second_dct = {'Tokyo': 3, 'Seol': 4}
merged = {**first_dct, **second_dct}
print(merged)

# 16 识别字符串是否以特定字母开头
sentence = 'Data Studio'
print(sentence.startswith('d'))
print(sentence.endswith('o'))

# 17 获取字符的Unicode
print(ord('T'))
print(ord('A'))
print(ord('h'))
print(ord('a'))

# 18 获取字典的键值
cities = {'London': 1, 'Paris': 2, 'Tokyo': 3, 'Seol': 4}
for key, value in cities.items():
    print(f'key:{key} and Value:{value}')

# 19在数学运算中使用布尔值
x = 9
y = 3
outcome = (x - False) / (y * True)
print(outcome)

# 20在列表的特定位置添加值
# list_name.insert(position, value)

cities = ['London', 'Vienna', 'Rome']
cities.append('Seoul')
print('After append:', cities)
cities.insert(0, 'Berlin')
print('After insert:', cities)
cities.insert(1, ['Beijing', 'Shanghai'])
# ['Berlin', 'London', ['Beijing', 'Shanghai'], 'Beijing', 'Vienna', 'Rome', 'Seoul']

# 21过滤器filter()函数
# filter(function,iterator)
mixed_number = [8, 15, 25, 30, 34, 67, 90, 5, 12]
filtered_value = filter(lambda x: x > 20, mixed_number)
print(f'After filter: {list(filtered_value)}')


# 22创建没有参数边界的函数,简单的说这就是不定长参数的应用
def multiplication(*arguments):
    mul = 1
    for i in arguments:
        mul = mul * i
    return mul


print(multiplication(3, 4, 5))
print(multiplication(5, 8, 10, 3))
print(multiplication(8, 6, 15, 20, 5))

# 23 一次迭代两个或多个列表
# 使用enumerate函数迭代两个列表，但是可以用zip（）函数迭代两个或多个列表；解压用*。zipped zip（*zipped）
capital = ['Vienna', 'Paris', 'Seoul', 'Rome']
countries = ['澳大利亚', '法国', '韩国', '意大利']
con_countries = ['中国', '英国', '朝鲜', '法国']
for cap, country in zip(capital, countries, con_countries):
    print(f'{cap}是{country}的首都,竞争国家是{con_countries}')

# 24 zip函数的反解压，其实还是zip，只是对已经zip过的一种标识
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # 打包为元组的列表
print(zipped)
# <zip object at 0x000001B32B1D39C0>  zip对象

print(zip(a, c))
# <zip at 0x1b32b1e1dc0>

zip(*zipped)

# 25 改变句子中的字母的大小写
sentence = "Data STUDIO"
changed_sen = sentence.swapcase()
print(changed_sen)

# 26 检查对象使用内存的大小
import sys

mul = 5 * 6
print(sys.getsizeof(mul))

# 27 map()函数
values_list = [8, 10, 6, 50]
quotient = map(lambda x: x / 2, values_list)
print(f'Before division:{values_list}')
print(f'After division:{list(quotient)}')

# 28 反转整个字符串,字符串为什么没有reverse函数
value = 'OIDUTS ataD'
print('Reverse is:', value[::-1])

# 29 代码块的执行实践 只可以在jupyter中运行，在pycharm中没法运行
% % time
sentence = 'Data STUDIO'
changed_sen = sentence.swapcase()

# 30删除字符串的左侧和右侧的字符，默认是删除空格，也可以传递特定的字符
sentence1 = 'Data StUDIO           '
print(f'After removeing the right space:{sentence1.rstrip()}')
sentence2 = '          Data STUDIO'
print(f'After removing the the left space:{sentence2.lstrip()}')
sentence3 = 'Dsta STUDIO .,bbblllg'
print('After applying rstrip:', sentence3.rstrip('.,blg'))

# 31在元组或列表中查找元素的索引
cities_tuple = ('Berlin', 'Paris', 5, 'Vienna', 10)
print(cities_tuple.index('Paris'))
cities_list = ['Vienna', 'Paris', 'Seoul', 'Amsterdam']
print(cities_list.index('A'))

# 32 清空列表或集合中的元素
cities_list = ['Vienna', 'Paris', 'Seoul', 'Amsterdam']
print(f'Before removing from the list:{cities_list}')
cities_list.clear()
print(f'After removing from the list:{cities_list}')
cities_set = {'Vienna', 'Paris', 'Seoul', 'Amsterdam'}
print(f'Before removing from the set :{cities_set}')
cities_set.clear()
print(f'After removing from the set:{cities_set}')

# 33 连接两个集合
set1 = {'Vienna', 'Paris', 'Seoul'}
set2 = {'Tokyo', 'Rome', 'Amsterdam'}
print(set1.union(set2))

# 34根据频率对列表的值排序
from collections import Counter

count = Counter([7, 6, 5, 6, 8, 6, 6, 6])
print(count)
print('根据频率对值排序：', count.most_common())

# 35从列表中删除重复值
cities_list = ['Vienna', 'Paris', 'Seoul', 'Amsterdam', 'Paris', 'Amsterdam', 'Paris']
cities_list = set(cities_list)
print('从列表中删除重复值后：', list(cities_list))

# 36 列表中元素连接为句子
words_list = ['数据', 'STUDIO', "云朵君"]
print(" ".join(words_list))


# 37 一次从函数返回多少个值
def calculation(number):
    mul = number * 2
    div = number / 2
    summation = number + 2
    subtract = number - 2
    return mul, div, summation, subtract


mul, div, summation, subtract = calculation(10)
print('乘法：', mul)
print('除法：', div)
print('加法：', summation)
print('减法：', subtract)

# 38 找出两个列表之间的差异
cities_list1 = ['Vienna', 'Paris', 'Seoul', 'Amsterdam', 'Berlin', 'Londom']
cities_list2 = ['Vienna', 'Paris', 'Seoul', 'Amsterdam']
cities_set1 = set(cities_list1)
cities_set2 = set(cities_list2)
difference = list(cities_set1.symmetric_difference(cities_set2))
print(difference)

# 39将两个列表合并成为一个字典
number = [1, 2, 3]
cities = ['维也纳', '巴黎', '首尔']
result = dict(zip(number, cities))
print(result)

# 40 字符串格式化
print('i am {0},age{1}'.format('tom', 18))

