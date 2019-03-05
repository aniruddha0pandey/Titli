# titli

```bash
$ sudo apt update --yes
$ sudo apt upgrade --yes

$ uname -a # get sys arch
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
$ sudo apt-get install bzip2
$ bash miniconda.sh -b -p miniconda && rm miniconda.sh
$ echo "export PATH=\$PATH:\$HOME/setups/miniconda/bin" >> ~/.bashrc
$ source ~/.bashrc
$ conda update -n base -c defaults conda # update conda

$ conda create -n titli python==3.5 keras firebase-admin scikit-learn flask && source activate titli

$ ## OR
$ conda env create --file titli.txt && source activate titli
$ # conda list --explicit > titli.txt

$ ## OR
$ conda create -n titli && source activate titli
$ pip install -r requirements.txt
$ # pip freeze > requirements.txt

$ sudo apt-get install python-pip # sudo pip install --upgrade pip

$ python train.py -d "../dataset/flood" -m "../output/trained_model" -l "../output/bin" -p "../output/plot"
$ python predict.py --image "../tests"

```
