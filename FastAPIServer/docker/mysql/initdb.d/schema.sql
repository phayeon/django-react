create table posts(
        post_id varchar(20) primary key,
        title varchar(100),
        content varchar(1000),
        create_at datetime,
        updated_at datetime
)charset = utf8;