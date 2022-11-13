import pytest
from mysql_client import MySqlClient
from utils.builder import MySqlBuilder

class MyTest:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client:MySqlClient = mysql_client
        self.builder: MySqlBuilder = MySqlBuilder(self.client)

class TestMySql(MyTest):
    def test_count_request_by_type(self):
        self.builder.create_count_request_by_type()
        count_rows = self.client.execute_query('select count(*) from count_request_by_type;', fetch=True)[0][0]
        assert count_rows == 4

    def test_top_10_popular_request(self):
        count_top = 20
        self.builder.create_top_10_popular_request(count_top=count_top)
        count_rows = self.client.execute_query('select count(*) from top_10_popular_request;', fetch=True)[0][0]
        assert count_rows == count_top