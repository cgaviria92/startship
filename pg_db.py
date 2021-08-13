import databases, sqlalchemy

## Postgres Database
#DATABASE_URL = "postgresql://postgres:Micro2020@127.0.0.1:5432/postgres"
DATABASE_URL = "postgres://cetrwijkygzrya:462f033529889114d5f42adb57ea0eea8e755b755b808fc9e87e48848c3e631d@ec2-52-86-25-51.compute-1.amazonaws.com:5432/df2opdlv8197f7"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name" , sqlalchemy.String),
    sqlalchemy.Column("gender"    , sqlalchemy.CHAR  ),
    sqlalchemy.Column("create_at" , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.CHAR  ),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)