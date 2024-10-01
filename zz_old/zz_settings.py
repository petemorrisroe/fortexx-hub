from pydantic import BaseSettings

class Settings(BaseSettings):
    cosmos_db_endpoint: str = 'https://fortexx.documents.azure.com:443/'
    cosmos_db_key: str = 'r0wiDynUSKZiOxWrSvC4RD4FNfQjG2mg1dFkgKAUtEHeM2id4tqhDQEMbZmFV0vWdsLqb2thrBDjACDblmvlRw=='
    database_name: str = 'fortexx'
    container_name: str = 'article'

    class Config:
        env_file = ".env"  # Load from a .env file, or set variables in Azure

settings = Settings()
