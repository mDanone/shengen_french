import os

import dotenv
dotenv.load_dotenv()


DATABASE = {
    "HOST": os.getenv("HOST", "localhost"),
    "PORT": os.getenv("PORT", "5432"),
    "USERNAME": os.getenv("USERNAME", "postgres"),
    "PASSWORD": os.getenv("PASSWORD", "postgres"),
    "NAME": os.getenv("NAME", "postgres")
}

URL_EXAMPLE = "psycopg2://{HOST}:{PORT}@{USERNAME}:{PASSWORD}/{NAME}"
DATABASE_URL = URL_EXAMPLE.format(**DATABASE)

RU_CAPTCHA_KEY = os.getenv("RU_CAPTCHA_KEY")

RU_CAPTCHA_POST_URL = "https://rucaptcha.com/in.php"
RU_CAPTCHA_GET_URL = "https://rucaptcha.com/res.php"
