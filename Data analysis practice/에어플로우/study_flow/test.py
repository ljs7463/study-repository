# 슬랙 알림설정
alert = SlackAlert("airflow-notification")

default_args = {
    "owner": "SSSEOK",
    "email": ["SSSEOK@naver.com"],
    "on_success_callback": alert.slack_success_alert,
    "on_failure_cllback": alert.slack_failuer_alert,
    "provied_context": True,
}

# DAG 정의
dag = DAG(
    dag_id="정기_크롤링1",  # DAG의 식별자용 아이디
    description="oo사이트 업데이트 정보를 크롤링하는 DAG",  # DAG에 대해 설명한다.
    default_args=default_args,  # 모든작업에 적용되는 기본값을 설정하기
    start_date=datetime.datetime(2023, 1, 1, tzinfo=KST),  # DAG 실행 날짜
    schedule_interval="0 5 7 * * ",  # 스케쥴링 주기설정
)

# Task 정의

# 데이터 삭제 Task
pre_task = (
    BigQueryExecuteQueryOperator(  # Apache Airflow에서 BigQuery 쿼리를 실행하기 위한 오퍼레이터 중 하나
        task_id="데이터_삭제",  # Airflow내에서 해당 작업을 식별하는 데 사용되는 고유한 식별자
        sql="TRUNCATE TABLE `test_page.test_1.test_table",  # 실행할 쿼리
        use_legacy_sql=False,  # False -> StandardSQL, True -> Legacy SQL
        dag=dag,
    )
)

# 테이블 복사 Task
post_task = BigQueryExecuteQueryOperator(
    task_id="데이터_복사",
    sql="""
    SELECT * FROM `test_page.test.test_1`
    """,
    destination_dataset_table=f"test_page.using.test_1",  # 쿼리결과를 저장할 BigQuery테이블 지정
    write_disposition="WRITE_TRUNCATE",  # 쿼리결과를 저장할때 대상 테이블 처리방식 지정
    use_legacy_sql=False,
    dag=dag,
)
# Write_disposition -> 실행결과 데이터가 대상 테이블에 어떻게 저장될지 제어하는 parameter
## WRITE_TRUNCATE : 대상 테이블에 이미 데이터가 있는 경우, 기존 데이터를 삭제하고 실행 결과 데이터를 쓴다는 의미이다. 즉, 대상 테이블의 내용을 새롭게 덮어쓴다.
## WRITE_APPEND : 대상 테이블에 이미 데이터가 있는 경우, 새로운 데이터를 기존 데이터 뒤에 추가합니다. 즉, 데이터를 테이블에 추가한다.
## WRITE_EMPTY : 대상 테이블에 이미 데이터가 있는 경우 아무 작업도 수행하지 않는다. 대상 테이블이 비어있을때만 새로운 데이터를 쓸 수 있다.
