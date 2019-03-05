# titli

## Dependencies
```bash
$ sudo apt update --yes && sudo apt upgrade --yes

$ arch_ver=$(uname -a | grep -o "x86.") # arch_ver=$(arch)
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-$arch_ver.sh -O miniconda.sh
$ sudo apt-get install bzip2
$ bash miniconda.sh -b -p miniconda && rm miniconda.sh
$ echo "export PATH=\$PATH:\$HOME/setups/miniconda/bin" >> ~/.bashrc
$ source ~/.bashrc
$ conda update -n base -c defaults conda # conda update conda
```

## Setup and Installation
```bash
$ conda create -n titli python==3.5 keras tensorflow firebase-admin scikit-learn flask flask_uploads && source activate titli
$ # conda list --explicit > titli.txt

$ # or
$ conda env create --file titli.txt && source activate titli

$ # or
$ conda create -n titli && source activate titli
$ pip install keras tensorflow firebase-admin scikit-learn flask flask_uploads
$ # pip freeze > requirements.txt

$ # or
$ conda create -n titli && source activate titli
$ pip install -r requirements.txt


$ sudo apt-get install python-pip # sudo pip install --upgrade pip
```

## Build
```bash
$ python train.py -d "../dataset/flood" -m "../output/trained_model" -l "../output/bin" -p "../output/plot"
$ python server.py

```
## API Reference
|Method|Request|Response|
|:-:|-|-|
|POST|```curl -F "photo=@<path>" http://127.0.0.1:4000/upload/<uid>```|```"<uid>":{"img_label":"","img_url":""}}```|
