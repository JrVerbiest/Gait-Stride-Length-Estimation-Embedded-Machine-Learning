
import os
from pathlib import Path
import argparse
import time

import yaml
from yaml.loader import SafeLoader

import requests

from tensorflow import keras
import wandb

import edgeimpulse as ei

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

env_file = 'config.yaml'

# from env (yaml) file
with open(os.path.join(os.getcwd(), env_file), "r") as yaml_file:
    env_config = yaml.load(yaml_file, Loader=SafeLoader)
yaml_file.close()

ei.API_KEY = env_config['ei']['api_key']
model_file = 'model.h5'

def profile(args):

    # Download model from wandb project
    url = "https://api.wandb.ai/files/"+os.path.join(args.wandb_run_path, model_file)
    logger.info(url)

    r = requests.get(url, allow_redirects=True)
    open(model_file, "wb").write(r.content)

    model = keras.models.load_model(model_file)
    logger.info(model.summary())

    # Create C++ library with trained model
    model_output_type = ei.model.output_type.Regression()
    try:
        ei.model.deploy(model=model,
                        deploy_target=args.deploy_target,
                        model_output_type=model_output_type,
                        output_directory="./lib")

    except Exception as e:
        logger.info("Could not profile %s:" %e)

if __name__ == "__main__":

    my_file = Path(model_file)
    if my_file.is_file():
        logger.info('remove %s' %model_file)
        os.remove(model_file)

    parser = argparse.ArgumentParser(description="ei deploy - create ccp lib.")

    parser.add_argument("--wandb_run_path", type=str, help="wandb run path", required=True)
    parser.add_argument("--deploy_target", type=str, help="deploy target device", required=True)
    args = parser.parse_args()

    logger.info(args.wandb_run_path)
    logger.info(args.deploy_target)

    profile(args)
