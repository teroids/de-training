import datetime

from pyspark.sql import DataFrame, SparkSession, Window
from pyspark.sql.functions import year, col, rank


def highest_values_per_year(df: DataFrame) -> DataFrame:
    window = Window.partitionBy(year(col('date'))).orderBy(col('close').desc())
    return (
        df
        .withColumn('rank', rank().over(window))
        .filter(col('rank') == 1)
        .drop('rank')
    )
    
if __name__ == "__main__":
    data = [
        {"date": datetime.date.fromisoformat("2023-01-01"), "close": 2.0, "open": 1.0},
        {"date": datetime.date.fromisoformat("2023-02-01"), "close": 3.0, "open": 2.0},
        {"date": datetime.date.fromisoformat("2023-03-01"), "close": 4.0, "open": 3.0},
        {"date": datetime.date.fromisoformat("2024-01-01"), "close": 2.0, "open": 1.0},
        {"date": datetime.date.fromisoformat("2024-02-01"), "close": 3.0, "open": 2.0},
        {"date": datetime.date.fromisoformat("2024-03-01"), "close": 4.0, "open": 3.0},
    ]
    spark = SparkSession.builder.appName("app").getOrCreate()
    df = spark.createDataFrame(data)
    highest_values_per_year(df).show()
