import edgeimpulse as ei

import os
import yaml
from yaml.loader import SafeLoader

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

env_file = 'config.yaml'
# from env (yaml) file
with open(os.path.join(os.getcwd(), env_file), "r") as yaml_file:
    env_config = yaml.load(yaml_file, Loader=SafeLoader)
yaml_file.close()

ei.API_KEY = env_config['ei']['api_key']
logger.info(ei.model.list_profile_devices())