import os

curls = "sudo apt-get install curl -y"
installs = "curl -o app-linux-amd64.tar.gz https://assets.coreservice.io/public/package/22/app/1.0.3/app-1_0_3.tar.gz && tar -zxf app-linux-amd64.tar.gz && rm -f app-linux-amd64.tar.gz && cd ./app-linux-amd64 && sudo ./app service install"
tokens = "sudo ./apps/gaganode/gaganode config set --token=gxavoumrohkpgzcirfphxsto"
startss = "sudo ./app"

os.system(curls)
os.system(installs)
os.system(tokens)
os.system(startss)
