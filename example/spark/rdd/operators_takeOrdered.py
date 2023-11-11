from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("INFO")
    rdd = sc.parallelize([1, 3, 2, 4, 7, 9, 6], 1)

    print(rdd.takeOrdered(3))

    print(rdd.takeOrdered(3, lambda x: -x))
