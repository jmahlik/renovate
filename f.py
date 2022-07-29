import configparser
from pprint import pprint

config = configparser.ConfigParser()

config.read("./lib/modules/manager/tox/__fixtures__/tox-ini-1.txt")

pprint({s: dict(config[s]) for s in config.sections()})
