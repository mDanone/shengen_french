import os

import dotenv
dotenv.load_dotenv()


DATABASE = {
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", "5432"),
    "USERNAME": os.getenv("DB_USERNAME", "postgres"),
    "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
    "NAME": os.getenv("DB_NAME", "postgres")
}

URL_EXAMPLE = "psycopg2://{HOST}:{PORT}@{USERNAME}:{PASSWORD}/{NAME}"
DATABASE_URL = URL_EXAMPLE.format(**DATABASE)