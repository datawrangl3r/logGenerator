import random
import logging
import time
import argparse
import ConfigParser
from datetime import datetime 

parser = argparse.ArgumentParser(description='Random Log Generator.')
parser.add_argument('-i', '--iterations', type=int, help='Number of iterations', required=True)
parser.add_argument('-f', '--framework', type=str, default='lumen', help='Name of framework')
parser.add_argument('-s', '--sleep', type=int, default=0, help='Delay for the log to be printed')
args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.readfp(open('loggenerator.conf'))
msg = config.get(args.framework,"msg").split(',')

logging.basicConfig(
		filename='%s.log'%(str(datetime.now().date())), \
		level=logging.DEBUG,\
		format='%(message)s')

for i in range (args.iterations):
	logging.info('[%s] '%(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))+msg[random.randint(0, len(msg)-1)])
	time.sleep(args.sleep)
