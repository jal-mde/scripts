from __future__ import print_function

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
# $example on$
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.clustering import StreamingKMeans
from pyspark.mllib.clustering import StreamingKMeansModel
# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="StreamingKMeansExample")  # SparkContext
    #ssc = StreamingContext(sc, 1)

    model2 = StreamingKMeansModel.load(sc, "K_Means.model")
    result = model2.predict(01/05/2010 12:00:00 AM,150,34.1016,-118.3295,)
    print("/"*80)
    print(result)

    #ssc.start()
    #ssc.stop(stopSparkContext=True, stopGraceFully=True)
    # $example off$

    #print("Final centers: " + str(model.centers))
    print("Final centers Model 2: " + str(model2.centers))
