from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("INFO")
    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)

    print(rdd.glom().flatMap(lambda x: x).collect())
