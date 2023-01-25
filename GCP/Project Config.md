###### *Creating Virtual Environment*
	sudo apt-get update
	python3 -m pip install --user --upgrade pip
	python3 -m pip install --user virtualenv
	sudo apt install python3.8-venv
	python3 -m venv flax
	source flax/bin/activate
---
###### *Installing Jax*
	pip install --upgrade clu
	
	pip install "jax[tpu]>=0.2.26" \
	-f https://storage.googleapis.com/jax-releases/libtpu_releases.html
	
	export USE_TORCH=False

---
###### *Set up Transformers*
	pip install tensorflow-cpu
	git clone https://github.com/huggingface/transformers
	cd transformers
	pip install .
	pip install flax optax datasets	
	#You might need this if you are planning on streaming datasets
	git clone https://github.com/huggingface/datasets.git
	cd datasets
	pip install -e ".[streaming]"
	cd ~/
---
