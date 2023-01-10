import pymysql
from app.models.user import User
from app.env import conn
from sqlalchemy.orm import Session

pymysql.install_as_MySQLdb()


def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()


def find_users(db: Session):
    return db.query(User).all()
