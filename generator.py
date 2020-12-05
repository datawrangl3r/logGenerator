import random
import logging
import time
import argparse
from configparser import ConfigParser
from datetime import datetime

parser = argparse.ArgumentParser(description='Random Log Generator.')
parser.add_argument('-i', '--iterations',
                    type=int,
                    help='Number of iterations',
                    required=True)
parser.add_argument('-f', '--framework',
                    type=str,
                    default='lumen',
                    help='Name of framework')
parser.add_argument('-s', '--sleep',
                    type=int,
                    default=0,
                    help='Delay for the log to be printed')
args = parser.parse_args()
config = ConfigParser()
config.read('logging.cnf')
msg = config.get(args.framework, "msg").split(",")
logging.basicConfig(filename=f'{str(datetime.now().date())}.log',
                    level=logging.DEBUG,
                    format='%(message)s')

for i in range(args.iterations):
    datestimetamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info(f'{datestimetamp}'+msg[random.randint(0, len(msg)-1)])
    time.sleep(args.sleep)
