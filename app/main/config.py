#### Heroku Config
import os

class Config:
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True

config_by_name = dict(
    dev=DevelopmentConfig
)
