from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL') #mysql+aiomysql://username:password@host:port/dataname



class DataBase:

    def __init__(self, database_url=DATABASE_URL):
        self.__engine = create_async_engine(database_url, pool_pre_ping=True)
        self.__session = sessionmaker(self.__engine, class_=AsyncSession)
    
    async def on_shutdown(self) -> None:
        await self.__engine.dispose()
        print("Database connection closed.")
    
    async def view_statistics(self) -> dict | None:
        result = {"user count": None}
        try:
            async with self.__session() as session:
                stmt = text("""SELECT COUNT(*) FROM User""")
                query_result = await session.execute(stmt)
                users_count = query_result.fetchone()

                result["user count"] = users_count[0]

            return result
        except OperationalError as ex:  
            print("Connection failed.")
            print(ex)
            return None