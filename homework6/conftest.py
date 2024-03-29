import pytest
from mysql_client import MySqlClient


def pytest_configure(config):
    mysql_client = MySqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table_count_request_by_type()
        mysql_client.create_table_top_10_popular_request()
        mysql_client.create_top_5_big_request()
    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MySqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()