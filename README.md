# nvidia-optimize

Simple python module that when imported, sets Nvidia GPU's to optimal settings for Deep Learning 


| GPU  | Optimization               |
|------|----------------------------|
| M60  | `nvidia-smi -ac 2505,1177` |
| K80  | `nvidia-smi -ac 2505,875`  |
| V100 | `nvidia-smi -ac 877,1530`  |