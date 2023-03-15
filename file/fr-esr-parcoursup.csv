from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql.functions import col,struct,when, desc

spark = SparkSession \
    .builder \
    .appName("Read Parcoursup csv files") \
    .getOrCreate()

df = spark.read.load("fr-esr-parcoursup.csv", format="csv", sep=";", inferSchema="true", header="true")

result_df = df.select(col("fili"),col("form_lib_voe_acc"),col("fil_lib_voe_acc"),col("voe_tot").astype(IntegerType()))\
    .groupBy(["fili","form_lib_voe_acc", "fil_lib_voe_acc"])\
    .sum()\
    .sort(desc("sum(voe_tot)"))\
    .limit(10)
   
result_df.show(10, 100, True)
result_df.write.mode("overwrite").csv("result-parcoursup.csv", header=True)

