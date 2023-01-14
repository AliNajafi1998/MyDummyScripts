from credentials import *
from twarc import Twarc
import os
import sys
import json

if len(sys.argv) < 2:
    print("tweet_ids file is missing!!")
    sys.exit(1)

tweet_ids_fpath = sys.argv[1]

fname = os.path.basename(tweet_ids_fpath)


client = Twarc(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,)


BASEDIR = os.path.abspath(os.path.dirname(__file__))

downloaded_dir = os.path.join(BASEDIR, "TOBEFILLED", fname) + "_ids.txt"
ouput_dir = os.path.join(BASEDIR, "TOBEFILLED", fname) + ".jsonl"
 
fh = open(ouput_dir, 'w')
fs = open(downloaded_dir, 'w')
 
num_tweets=0
for tweet in client.hydrate(open(tweet_ids_fpath)):
    fh.write(json.dumps(tweet))
    fh.write("\n")
    fs.write(tweet["id_str"])
    fs.write("\n")
    num_tweets += 1
    if num_tweets % 10 == 0:
        print('Number of tweets added into database:{}'.format(num_tweets))