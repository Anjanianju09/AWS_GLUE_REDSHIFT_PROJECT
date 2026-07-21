from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="retail_sales_pipeline",
    schedule="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:

    crawler = GlueCrawlerOperator(
        task_id="run_crawler",
        crawler_name="RetailSalesCrawler"
    )

    bronze = GlueJobOperator(
        task_id="bronze_to_silver",
        job_name="Bronze_To_Silver"
    )

    silver = GlueJobOperator(
        task_id="silver_to_gold",
        job_name="Silver_To_Gold"
    )

    redshift = GlueJobOperator(
        task_id="gold_to_redshift",
        job_name="Gold_To_Redshift"
    )

    crawler >> bronze >> silver >> redshift
