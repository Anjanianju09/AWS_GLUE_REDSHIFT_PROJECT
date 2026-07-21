from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import *

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

df = spark.read.option("header", True).csv(
"s3://retailsalesproj09/bronze/sales/"
)

df = df.dropDuplicates()

df = df.filter(col("SaleID").isNotNull())

df = df.withColumn(
    "Quantity",
    col("Quantity").cast("int")
)

df = df.withColumn(
    "Price",
    col("Price").cast("double")
)

df = df.withColumn(
    "Revenue",
    expr("Quantity * Price")
)

df.write.mode("overwrite").parquet(
"s3://retailsalesproj09/silver/sales/"
)
