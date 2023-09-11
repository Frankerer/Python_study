# 导包
#SparkContext类对象，是PySpark编程中一切功能的入口#选定人类
from pyspark import SparkConf, SparkContext

#让spark能连接到python.exe
import os
os.environ["PYSPARK_PYTHON"] = "D:/software/python/python.exe"

# 创建SparkConf类对象#选定程序员
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext对象#选定作为程序员的我本身
sc = SparkContext(conf=conf)

#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd1 = sc.parallelize([1,2,3,4,5,6])

"""
MAP
"""
#设计一个方法
def func(data):
    return data*10
# 通过map方法将全部数据都乘以10
#   对RDD内的数据逐个处理，并返回一个新的RDD
rdd1_2 = rdd1.map(func)#得到的是rdd对象
rdd1_3 = rdd1.map(lambda x:x*10).map(lambda y:y+5)#链式调用

print(rdd1_2.collect())
print(rdd1_3.collect())

""" 
flatmap
"""
#对rdd执行map操作，然后进行{解除嵌套}操作

#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd2 = sc.parallelize(["1234 abc eff","aff ewf fff"])
rdd2_1 = rdd2.map(lambda x:x.split(" "))#[['1234', 'abc', 'eff'], ['aff', 'ewf', 'fff']]
print(rdd2_1.collect())
rdd2_2 = rdd2.flatMap(lambda x:x.split(" "))
print(rdd2_2.collect())#['1234', 'abc', 'eff', 'aff', 'ewf', 'fff']

"""
reduceByKey算子
"""
#针对元组数据（a,b），认定a为key,进行key的聚合，并执行关于b的数据（自定义）操作
rdd3 = sc.parallelize([('a',1),('a',2),('b',9),('b',8),('b',7),('c',1)])
rdd3_1 = rdd3.reduceByKey(lambda a,b:a+b)
#进行关于（a，b）的元素key:a的聚合，执行关于b的操作，例如，对于key:'b'，操作为9+8=17，17+7=24，结果为(‘b’,24)
print(rdd3_1.collect())#[('c', 1), ('a', 3), ('b', 24)]

"""
filter数据过滤
"""
#通过某函数对数据进行判断，用函数结果的返回值True,Flase来决定该数据是否去留
rdd4 = sc.parallelize([1,2,3,4,5,6])
rdd4_1 = rdd4.filter(lambda a:a%2 == 0)
print(rdd4_1.collect())#[2, 4, 6]

"""
distinct
"""
#去重操作
rdd5 = sc.parallelize([1,2,2,4,6,6])
rdd5_1 = rdd5.distinct()
print(rdd5_1.collect())#[1, 2, 4, 6]

"""
sortBy
"""
#按照数据的指定元素大小进行排序
rdd6 = sc.parallelize([('a',1),('b',2),('c',9),('d',8),('e',7),('f',1)])
rdd6_1 = rdd6.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print(rdd6_1.collect())#[('c', 9), ('d', 8), ('e', 7), ('b', 2), ('a', 1), ('f', 1)]

"""
pyspark输出操作
"""
rdd7 = sc.parallelize([1,1,3,4,5,3])

#collect算子
rdd7.collect()
#内容转化成list

#reduce算子,对RDD两两聚合
num = rdd7.reduce(lambda a,b:a+b)
print(num)#17
#((((((1+1)+3)+4)+5)+3)

#take算子
#取出前面指定数量个元素，组成list返回
rdd7.take(5)#【1，1，3，4，5】

#count,统计rdd内元素个数，返回值是数字
rdd7.count()

"""
pyspark输出到文件操作
"""



sc.stop()
