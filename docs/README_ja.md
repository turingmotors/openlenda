<div align="center">
<img height="200px" src="../assets/OpenLendaLogo.png">  

# OpenLenda
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](../LICENSE)

<a href="../README.md">
    <img src="https://img.shields.io/badge/-EN-555555.svg?logo=&style=flat-square">
</a>

**OpenLenda** は日本の交通信号機を検出・認識するモデルです。

![sample](../assets/sample.gif)

</div>

# 🚥Introduction

**OpenLenda**はYOLOXベースの日本の交通信号機認識モデルです。このモデルは交通信号機を検出するだけでなく、色や矢印の認識もEnd-to-Endで行います。詳細は[こちら](https://zenn.dev/turing_motors/articles/traffic-light)をご覧ください。このリポジトリはモデル公開用です。

# 🚙Getting Started

## Installation

1. リポジトリをクローンします。
    ```bash
    git clone https://github.com/turingmotors/openlenda.git
    cd openlenda
    ```

2. Pythonの依存関係をインストールします。[pyenv](https://github.com/pyenv/pyenv)及び[poetry](https://python-poetry.org/)を使用してPythonのバージョンと依存関係を管理することを強くお勧めします。
    ```bash
    pyenv install 3.8.10
    pyenv local 3.8.10
    poetry install
    ```

3. 学習済みの重みをダウンロードします。
    ```bash
    wget https://github.com/... models/
    ```
    
## Demo
GPUを使用しない場合は、以下のコマンドから`--gpu`を削除してください。
```bash
python tools/demo.py video -f exps/openlenda_s.py\
    -c models/openlenda_s.pth\
    --path assets/tokyo_day.mp4\
    --conf 0.5 --nms 0.01 --tsize 640 ---save_result --gpu
```

## Export ONNX
```bash
python tools/export_onnx.py --output-name openlenda_s.onnx\
    -f exps/openlenda_s.py\
    -c models/openlenda_s.pth\
```

# 📈Performance
APやARは非公開の検証セットで評価されています。結果は以下の通りです。(score threshold: 0.45)
| Model | size | AP50 | AR50 | Download |
|:---:|:---:|:---:|:---:|:---:|
| OpenLenda-nano | 416x416 | 0.941 |0.830 | |
| OpenLenda-tiny | 416x416 | 0.944 | 0.807 | |
| OpenLenda-s | 640x640 | 0.964 | 0.946 | |
| OpenLenda-x | 640x640 | 0.950 | 0.961 | |


# 📚Documentation
YOLOXの [documentation](https://github.com/Megvii-BaseDetection/YOLOX/blob/main/README.md) をご覧ください。

# 🤔Q & A
<details>
<summary> Q and Aを見る </summary>

## データセットについて
### データセットは公開されていますか？
申し訳ありませんが、データセットは非公開です。

### データセットには何枚の画像が含まれていますか？
約4.4万枚の画像が含まれています。

## 学習及び評価について
### このリポジトリを使用して学習や評価を行うことはできますか？
Apache 2.0ライセンスの下で可能です。ただし、現時点では、学習や評価にこのリポジトリのコードをそのまま使用することはできないため、自分でコードを変更する必要があります。
</details>

# Orginization
<a href="https://www.turing-motors.com/">Turing Inc.

<image height="100px" src ="../assets/TuringLogo.png">
</a> 

# 📝License
このプロジェクトはApache License 2.0の下で公開されています。詳細は[LICENSE](../LICENSE)をご覧ください。

# 🙏Acknowledgement
このプロジェクトは[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)をベースにしています。
