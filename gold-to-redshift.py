from awsglue.context import GlueContext
from pyspark.context import SparkContext

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

gold = spark.read.parquet(
"s3://retailsalesproj09/gold/sales/"
)

gold.write \
.format("jdbc") \
.option(
"url",
"jdbc:redshift://<cluster-endpoint>:5439/dev"
) \
.option("dbtable","fact_sales") \
.option("user","admin") \
.option("password","password") \
.mode("overwrite") \
.save()
