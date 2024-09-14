

import os
import path
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

class Config(object):

    CLUSTER_NAME = os.getenv("CLUSTER_NAME")
    CLUTER_PASSWORD = os.getenv("CLUTER_PASSWORD")
    GCP_API_KEY = os.getenv("GCP_API_KEY")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
