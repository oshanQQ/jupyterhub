FROM python:3.8.13-buster

# rootユーザでないとノートブックが新規作成できないらしい
USER root

# お好みでワークスペースを作成
WORKDIR /root/workspace 

RUN apt update

# timezoneの設定
RUN apt install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV TZ=Asia/Tokyo

# 無駄なキャッシュを削除してなるべくイメージ容量を小さくする
RUN apt autoremove
RUN apt clean
RUN rm -r /var/lib/apt/lists/*

#  計算機関連のライブラリをインストールする
RUN pip install --no-cache-dir numpy pandas scipy opencv-python matplotlib Pillow scikit-learn optuna keras

# jupyterlabの拡張関係をインストールする
RUN pip install --no-cache-dir jupyterhub jupyterlab_code_formatter jupyterlab-git lckr-jupyterlab-variableinspector jupyterlab_widgets ipywidgets import-ipynb jupyterlab-language-pack-ja-JP

# jupyterhubの起動時設定 dockerspawnerを使うときは原則これ
CMD ["jupyterhub-singleuser", "--allow-root"]

