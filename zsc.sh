#!/bin/sh

ROOT_DIR="zsc-app"

ZSC_API_SRC="https://github.com/iqbal-haz/zsc_api.git"
LOCAL="zsc_api"

LOCAL_VC_DIR=$LOCAL/.git

# Install python if Windows hasn't had python installed
if [[ $OSTYPE == "msys" ]];
then
    if ! type python > /dev/null
    then
        cd ~/Downloads
        curl https://www.python.org/ftp/python/3.9.12/python-3.9.12-amd64.exe --output python-3.9.12.exe
        python-3.9.12.exe /quiet PrependPath=1
    fi
fi

if [ ! -d $ROOT_DIR ]
then
    mkdir $ROOT_DIR && cd $ROOT_DIR
else
    cd $ROOT_DIR
fi

if [ ! -d $LOCAL_VC_DIR ]
then
    git clone $ZSC_API_SRC $LOCAL
    python3 -m venv env
    source env/bin/activate
    cd $LOCAL
else
    source env/bin/activate
    cd $LOCAL
    git pull $ZSC_API_SRC
fi

pip install -r requirements.txt
python3 app.py