Linux Commands 

##### *Running Scripts in Parallel*
	cat turkish_tweets_all_fnames.txt | parallel -P 10 python scripts/basic_clean_up.py {}

##### *Change Owner of file*
	sudo chown $(whoami) ~/TurkishTwitterRobertaLarge/.git/config
