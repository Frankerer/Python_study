"""
演示获取PySpark的执行环境入库对象：SparkContext
并通过SparkContext对象获取当前PySpark的版本
"""

# 导包
#SparkContext类对象，是PySpark编程中一切功能的入口#选定人类
from pyspark import SparkConf, SparkContext
# 创建SparkConf类对象#选定程序员
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext对象#选定作为程序员的我本身
sc = SparkContext(conf=conf)


#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# RDD对象称之为分布式弹性数据集，是PySpark中数据计算的载体，它可以:
# 提供数据存储
# 提供数据计算的各类方法
# 数据计算的方法，返回值依旧是RDD（RDD迭代计算)
# 后续对数据进行各类计算，都是基于RDD对象进行

rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1":"value1","key2":"value2","key3":"value3"})

#如果要查看RDD里面有什么内容，需要用collect()方法
print(rdd1.collect())#[1, 2, 3, 4, 5]
print(rdd2.collect())#[1, 2, 3, 4, 5]
print(rdd3.collect())#['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(rdd4.collect())#[1, 2, 3, 4, 5]
print(rdd5.collect())#['key1', 'key2', 'key3']


# 用过textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd = sc.textFile("D:\software\pycharm\code\数据\shoping.txt")

print(rdd.collect())
#列表方式，每行是一个字符串元素


# 打印PySpark的运行版本
print(sc.version)
# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()