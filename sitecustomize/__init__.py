import dotenv
import sys
import os

dotenvpath = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), ".env")
if os.path.exists(dotenvpath):
    dotenv.read_dotenv(dotenvpath)
