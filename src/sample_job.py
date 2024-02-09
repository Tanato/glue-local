from pyspark.conf import SparkConf
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.types import StructType, StructField, StringType


def initSpark():
    conf = SparkConf().setAll([("spark.eventLog.enabled", False)])
    sc = SparkContext(conf=conf)
    glueContext = GlueContext(sc)
    return glueContext.spark_session


spark = initSpark()

order_list = [
                ['1005', '623', 'YES', '1418901234', '75091'],
                ['1006', '547', 'NO', '1418901256', '75034'],
                ['1007', '823', 'YES', '1418901300', '75023'],
                ['1008', '912', 'NO', '1418901400', '82091'],
                ['1009', '321', 'YES', '1418902000', '90093']
            ]

# Define schema for the order_list
order_schema = StructType([
                        StructField("order_id", StringType()),
                        StructField("customer_id", StringType()),
                        StructField("essential_item", StringType()),
                        StructField("timestamp", StringType()),
                        StructField("zipcode", StringType())
                    ])

# Create a Spark Dataframe from the python list and the schema
df_orders = spark.createDataFrame(order_list, schema=order_schema)

df_orders.show()
