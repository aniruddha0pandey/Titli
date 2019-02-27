# titli

```bash
$ sudo apt update --yes
$ sudo apt upgrade --yes

$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
$ sudo apt-get install bzip2
$ bash miniconda.sh -b -p miniconda
$ echo "export PATH=\$PATH:\$HOME/setups/miniconda/bin" >> ~/.bashrc
$ source ~/.bashrc

$ conda create -n sih python==3.5 keras
$ source activate sih

$ python train.py -d "../dataset/flood" -m "../output/trained_model" -l "../output/bin" -p "../output/plot"
$ python predict.py --image "../tests"
```
