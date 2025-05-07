from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("ClothingCategoryJoin").getOrCreate()

products_df = spark.createDataFrame(
    [
        (1, "Футболка"),
        (2, "Джинсы"),
        (3, "Куртка"),
        (4, "Шарф"),
        (5, "Кепка"),
    ],
    ["product_id", "product_name"],
)


categories_df = spark.createDataFrame(
    [
        (1, "Верхняя одежда"),
        (2, "Аксессуары"),
        (3, "Одежда для низа"),
    ],
    ["category_id", "category_name"],
)


product_category_df = spark.createDataFrame(
    [
        (1, 3),
        (2, 3),
        (3, 1),
        (4, 2),
    ],
    ["product_id", "category_id"],
)


product_with_categories = (
    products_df.join(product_category_df, "product_id", "left")
    .join(categories_df, "category_id", "left")
    .select("product_name", "category_name")
)

product_with_categories.show()
