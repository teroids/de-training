import datetime

import pytest
from pyspark.sql import SparkSession
from pyspark.testing.utils import assertDataFrameEqual


from spark_examples.app import highest_values_per_year


@pytest.fixture
def spark_fixture():
    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    yield spark
    spark.stop()

def test_highest_values_per_year(spark_fixture):
    spark = spark_fixture
    
    data = [
        {"date": datetime.date.fromisoformat("2023-01-01"), "close": 2.0, "open": 1.0},
        {"date": datetime.date.fromisoformat("2023-02-01"), "close": 3.0, "open": 2.0},
        {"date": datetime.date.fromisoformat("2023-03-01"), "close": 4.0, "open": 3.0},
        {"date": datetime.date.fromisoformat("2024-01-01"), "close": 2.0, "open": 1.0},
        {"date": datetime.date.fromisoformat("2024-02-01"), "close": 3.0, "open": 2.0},
        {"date": datetime.date.fromisoformat("2024-03-01"), "close": 4.0, "open": 3.0},
    ]
    
    original_df = spark.createDataFrame(data)
    
    transformed_df = highest_values_per_year(original_df)
    
    expected_data = [
        {"date": datetime.date.fromisoformat("2023-03-01"), "close": 4.0, "open": 3.0},
        {"date": datetime.date.fromisoformat("2024-03-01"), "close": 4.0, "open": 3.0},
    ]

    expected_df = spark.createDataFrame(expected_data)

    assertDataFrameEqual(transformed_df, expected_df)
