from abc import ABC, abstractmethod

class DBManger(ABC):
    """
    abstractmethod 데코레이터를 활용하여 추상 메소드 선언
    """
    @abstractmethod
    def connection(self):
        pass

class SqlServer(DBManger):

    def connection(self):
        return ('Microsoft Database Connected.')

class OracleServer(DBManger):

    def connection(self):
        return ('Oracle Database Connected.')

class MariaServer(DBManger):

    def connection(self):
        return ('Maria Database Connected.')

class DBConnFactory(DBManger):
    """
    DBConnFactory 클래스 인스턴스 생성
    """

    def get_db_connection(self, db):
        return db.connection()


db_factory = DBConnFactory()

print(db_factory.get_db_connection(SqlServer))
print(db_factory.get_db_connection(MariaServer))
print(db_factory.get_db_connection(OracleServer))