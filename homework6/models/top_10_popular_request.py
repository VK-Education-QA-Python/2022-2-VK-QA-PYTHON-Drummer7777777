from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR


BaseTop10PopularRequest = declarative_base()


class Top10PopularRequest(BaseTop10PopularRequest):
    __tablename__ = 'top_10_popular_request'
    __table_arg__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    path_request = Column(CHAR(100), nullable=False)
    count_request = Column(Integer, nullable=False)