import os
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)


class GetEnv:
    def __init__(self):
        self.CURRENT_ENV: str = os.environ.get("ENV")


class Debug:
    def __init__(self):
        self.debug: bool = os.environ.get("DEBUG")


class MySQL:
    def __init__(self):
        MY_SQL_ADDRESS: str = os.environ.get("MY_SQL_ADDRESS")
        MY_SQL_LOGIN: str = os.environ.get("MY_SQL_LOGIN")
        MY_SQL_PASSWORD: str = os.environ.get("MY_SQL_PASSWORD")
        MY_SQL_DB_NAME: str = os.environ.get("MY_SQL_DB_NAME")
        self.SQLALCHEMY_DATABASE_URL = f"mysql://{MY_SQL_LOGIN}:{MY_SQL_PASSWORD}@{MY_SQL_ADDRESS}/{MY_SQL_DB_NAME}"
        # self.database = databases.Database(SQLALCHEMY_DATABASE_URL)


class Config(GetEnv, Debug, MySQL):
    pass


config = Config()
