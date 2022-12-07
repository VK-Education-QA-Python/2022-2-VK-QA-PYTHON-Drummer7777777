from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR


BaseTop5BigRequest = declarative_base()


class Top5BigRequest(BaseTop5BigRequest):
    __tablename__ = 'top_5_big_request'
    __table_arg__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_str_in_logs = Column(CHAR(30), nullable=False)
    # path_request = Column(CHAR(100), nullable=False)
    status_request = Column(Integer, nullable=False)
    size_request = Column(Integer, nullable=False)
    ip_request = Column(CHAR(30), nullable=False)