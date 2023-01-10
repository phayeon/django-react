import pymysql
from app.models.post import Post
from app.env import conn
from sqlalchemy.orm import Session

pymysql.install_as_MySQLdb()


def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from posts"
    cursor.execute(sql)
    return cursor.fetchall()


def find_posts(db: Session):
    return db.query(Post).all()
