import os

installs = "curl -o app-linux-amd64.tar.gz https://assets.coreservice.io/public/package/29/gaganode/1.0.4/gaganode-1_0_4.tar.gz && tar -zxf app-linux-amd64.tar.gz && cd gaganode-linux-amd64 && sudo ./gaganode config set --token=gxavoumrohkpgzcirfphxsto"

os.system(installs)
