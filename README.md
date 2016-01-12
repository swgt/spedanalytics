# SPED Analytics

Sistema de Analise dos dados do SPED Fiscal.

[![Build Status](https://travis-ci.org/swgt/spedanalytics.svg?branch=master)](https://travis-ci.org/swgt/spedanalytics)
[![Code Health](https://landscape.io/github/swgt/spedanalytics/master/landscape.svg?style=flat)](https://landscape.io/github/swgt/spedanalytics/master)
[![Throughput Graph](https://graphs.waffle.io/swgt/spedanalytics/throughput.svg)](https://waffle.io/swgt/spedanalytics/metrics)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/swgt/spedanalytics.git swgt
cd swgt
python -m venv .swgt
source .swgt/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku master --force
```
