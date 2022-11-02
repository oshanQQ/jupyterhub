from jupyter_client.localinterfaces import public_ips
from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator

# 作成したdocker imageの名前
image_name = "jupyterhub"

# ログイン方式をNativeAuthentivatorにする
c.JupyterHub.authenticator_class = NativeAuthenticator

# 好きユーザに管理者権限を与える
c.Authenticator.admin_users = {"admin"}

# wslのIPアドレスを取得する　≠　WindowsのIPアドレス
ip = public_ips()[0]

# jupyterのhubへのルート
c.JupyterHub.hub_ip = ip
c.JupyterHub.hub_port = 8111

# JupyterhubにアクセスするためのIP
c.JupyterHub.ip= ip
c.JupyterHub.port = 8888

# DockerコンテナのSpawner設定
c.JupyterHub.spawner_class = DockerSpawner
c.Spawner.default_url = "/lab"
c.DockerSpawner.default_url = "/lab"
c.DockerSpawner.image = image_name
c.DockerSpawner.remove_containers = True
c.DockerSpawner.hub_ip = ip

# workspaceの設定、ノートブックの永続化
notebook_dir = "/root/workspace"
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"jupyterhub-user-{username}" : notebook_dir}

