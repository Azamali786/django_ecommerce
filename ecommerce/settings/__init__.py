from decouple import config
env = config("ENVIRONMENT")

if env == "DEV":
    from .dev_settings import *
elif env == "PROD":
    from.prod_settings import*
