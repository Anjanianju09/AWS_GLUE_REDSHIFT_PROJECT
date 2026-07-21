from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import sum

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

silver = spark.read.parquet(
"s3://retailsalesproj09/silver/sales/"
)

gold = silver.groupBy("ProductID").agg(
sum("Revenue").alias("TotalRevenue")
)

gold.write.mode("overwrite").parquet(
"s3://retailsalesproj09/gold/sales/"
)
