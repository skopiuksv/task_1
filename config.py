from dotenv import load_dotenv, dotenv_values
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost/svyatoslavskopyuk')

load_dotenv()
credentials = dotenv_values(".env")
