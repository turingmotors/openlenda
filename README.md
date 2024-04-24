<div align="center">
<img height="200px" src="assets/OpenLendaLogo.png">  

# OpenLenda
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

<a href="docs/README_ja.md">
    <img height="20px" src="https://img.shields.io/badge/JA-flag.svg?color=555555&style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj4NCjxwYXRoIGZpbGw9IiNmZmYiIGQ9Im0wLDBoOTAwdjYwMGgtOTAweiIvPg0KPGNpcmNsZSBmaWxsPSIjYmUwMDI2IiBjeD0iNDUwIiBjeT0iMzAwIiByPSIxODAiLz4NCjwvc3ZnPg0K">
</a>

**OpenLenda** is a Japanese traffic light detection and recognition model.

![sample](assets/sample.gif)

</div>

# 🚥Introduction
**OpenLenda** is a Japanese traffic light recognition model based on [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX). This model not only detects traffic lights but can also recognize their colors and specific arrow indications in an end-to-end manner.
For more information about the development, please visit [https://zenn.dev/turing_motors/articles/traffic-light](https://zenn.dev/turing_motors/articles/traffic-light) (Japanese article). This repository is for model publication. 

# 🚙Getting Started

## Installation

1. Clone this repository.
    ```bash
    git clone https://github.com/turingmotors/openlenda.git
    cd openlenda
    ```

2. Install python dependencies. We strongly recommend using [pyenv](https://github.com/pyenv/pyenv) and [poetry](https://python-poetry.org/) to manage python versions and dependencies.
    ```bash
    pyenv install 3.8.10
    pyenv local 3.8.10
    poetry install
    ```

3. Download the pretrained weights.
    ```bash
    wget https://github.com/turingmotors/openlenda/releases/download/v0.1.0/openlenda_s.pth -P models
    ```
    
## Demo
If you don't have a GPU, please remove `--device gpu` from the following commands.
```bash
python tools/demo.py video -f exps/openlenda_s.py\
    -c models/openlenda_s.pth\
    --path assets/tokyo_day.mp4\
    --conf 0.5 --nms 0.01 --tsize 640 --save_result --device gpu
```

## Export ONNX
```bash
python tools/export_onnx.py --output-name openlenda_s.onnx\
    -f exps/openlenda_s.py\
    -c models/openlenda_s.pth\
```

# 📈Performance
AP and AR are evaluated on the private validation set. The results are shown below.
| Model | size | AP50 | AR50 | Download |
|:---:|:---:|:---:|:---:|:---:|
| OpenLenda-nano | 416x416 | 0.941 |0.830 | [link](https://github.com/turingmotors/openlenda/releases/latest/download/openlenda_nano.pth) |
| OpenLenda-tiny | 416x416 | 0.944 | 0.807 | [link](https://github.com/turingmotors/openlenda/releases/latest/download/openlenda_tiny.pth) |
| OpenLenda-s | 640x640 | 0.964 | 0.946 | [link](https://github.com/turingmotors/openlenda/releases/latest/download/openlenda_s.pth) |
| OpenLenda-x | 640x640 | 0.950 | 0.961 | [link](https://github.com/turingmotors/openlenda/releases/latest/download/openlenda_x.pth)|

# 📚Documentation
Please see YOLOX's [README](https://github.com/Megvii-BaseDetection/YOLOX/blob/main/README.md) or [docs](docs) (almost same as YOLOX's).

# 🤔Q & A
<details>
<summary> Check Q and A. </summary>

## About Datasets
### Is the dataset publicly available?
Sorry, but the dataset is private.

### How many images are there in the dataset?
About 44,000 images.

## About Training and Evaluation
### Can I use this repository for learning and evaluation?
This is possible under the Apache 2.0 license. However, at this time, it is not possible to use the code in this repository as-is for training and evaluation, so you will need to modify the code yourself.
</details>

# Orginization
<a href="https://www.turing-motors.com/en">Turing Inc.

<image height="100px" src ="assets/TuringLogo.png">
</a> 

# 📝License
This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for more details.

# 🙏Acknowledgement
This project is based on [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX).
