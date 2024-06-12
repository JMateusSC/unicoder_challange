from dotenv import dotenv_values

secrets = dotenv_values(".env")

DATABASE_URL = secrets['DATABASE_URL']
JWT_SECRET_KEY = secrets['JWT_SECRET_KEY']
JWT_REFRESH_SECRET_KEY = secrets['JWT_REFRESH_SECRET_KEY']
ALGORITHM = secrets['ALGORITHM']

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days