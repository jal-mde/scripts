from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kafka_wordcount.py <zk> <topic>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingKafkaWordCount")
    ssc = StreamingContext(sc, 1)

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel( logger.Level.ERROR )
    logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

    zkQuorum, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
    lines = kvs.map(lambda x: x[1])
  #################################################################  
    grep = lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: word) \
        .filter(lambda x:(x == "AUDI"))
    grep.pprint()
#################################################################
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda x: (x, 1))\
                  .reduceByKey(lambda a, b: a + b)
    counts.pprint()
#################################################################
    ssc.start()
    ssc.awaitTermination()
