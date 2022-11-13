from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR


BaseCountRequestByType = declarative_base()


class CountRequestByType(BaseCountRequestByType):
    __tablename__ = 'count_request_by_type'
    __table_arg__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_request = Column(CHAR(50), nullable=False)
    count_request = Column(Integer, nullable=False)

