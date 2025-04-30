from pyspark.sql import SaparkSession

def read_postgres(spark):
    if = spark.read \
        .format("jdbc") \
        .option("url","jdbc:postgresql") \
        .option("dbtable","yourtable") \
        .option("user","etlreadonly") \
        .option("password","novadrive376a@") \
        .load()
    return df


"""
def read_csv(spark,file_path):
df = spark.read.csv(file_path, header=True, inferSchema=True)
return df
"""

def read_excel(spark,file_path):
    df = spark.read.format("com.crealytics.spark.excel") \
        .oprion("header", "true") \
        .load(file_path)
    return df

if __name__ == "__main__":
    spark = SparkSession.builder.appName("DataConnector").getOrCrate()
    
    postgres_df = read_postgres(spark)
#     ---csv_df = read_csv(spark, "data/yourfile.csv")
    excel_df = read_excel(spark, "data/dados.xlsx")
    
    # Save data to MinIO
    postgres_df.write.parquet("s3a://your-bucket/landing/postgress")
    # csv_df.write.parquet("sea://your-bucket/landing/csv")
    excel_df.write.parquet("s3a://your-bucket/landing/excel")    
    