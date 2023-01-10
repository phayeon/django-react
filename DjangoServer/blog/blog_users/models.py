from django.db import models


# 유저
class BlogUser(models.Model):
    use_in_migration = True
    blog_userid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=20)

    class Meta:
        db_table = "blog_users"

