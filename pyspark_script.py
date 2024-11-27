from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


jar_files = [
    "clickhouse-jdbc-0.4.6.jar", 
    "postgresql-42.2.23.jar"]

spark = SparkSession.builder.appName("PySpark PostgreSQL Connection").config("spark.jars", ",".join(jar_files)).getOrCreate()

url = "jdbc:postgresql://localhost:5434/test_db"
properties = {
    "user": "zms",
    "password": "123456",
    "driver": "org.postgresql.Driver"
}

df = spark.read.jdbc(url=url, table="test_table", properties=properties)


url_ch = "jdbc:clickhouse://localhost:8123"
user_ch = "default" 
password_ch = ""  
query_ch = "select * from test_table"
driver_ch = "com.clickhouse.jdbc.ClickHouseDriver"

df_ch = (spark.read
      .format('jdbc')
      .option('driver', driver_ch)
      .option('url', url_ch)
      .option('user', user_ch)
      .option('password', password_ch).option(
    'query', query_ch).load())


print('clickhouse')
df_ch.show()
print('postgresql')
df.show()

spark.stop()
