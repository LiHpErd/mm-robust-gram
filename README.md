# 面向鲁棒多模态学习的质量门控格拉姆表征对齐方法

> 毕业设计课题仓库 · **格式示例**（代码为占位，不含真实实现）

在多模态学习中，某一路输入质量下降（加噪、丢字、传感器掉线）时，模型常被坏数据带偏。
本工作提出**质量门控 + 格拉姆（二阶关系结构）对齐**：用无标注的质量信号动态调节各模态的
融合权重与对齐强度，只在对齐双方都可靠时才施加约束。

---

## 目录

- [方法概述](#方法概述)
- [快速开始](#快速开始)
- [实验结果](#实验结果)
- [仓库结构](#仓库结构)
- [引用](#引用)
- [License](#license)

## 方法概述

```
图像 ──► 冻结骨干 ──► F_img ──┬──► 质量头 ──► g_img ─┐
                              ├──► Gram G_img ───────┤
                              └──► 分类头 ──► logits ─┴──► 门控加权融合 ──► ŷ
文本 ──► 冻结骨干 ──► F_txt ──┬──► 质量头 ──► g_txt ─┘
                              ├──► Gram G_txt ───────┘
                              └──► 分类头 ──► logits

损失 = CE(fused) + λ1·Σ g_m·CE_m + λ2·Σ g_m·g_n·‖G_m − G_n‖²
```

三个模块：① 质量估计（置信度/扰动一致性/证据不确定性）；② 门控对齐；③ 门控融合。

## 快速开始

```bash
# 1. 环境
conda create -n mm python=3.10 -y && conda activate mm
pip install -r requirements.txt

# 2. 跑一次（占位脚本，仅验证环境）
python -m src.train --config configs/base.json
```

数据与权重（不进仓库，按需下载）：

| 数据/权重 | 用途 | 获取 |
|---|---|---|
| Food-101（UPMC） | 主数据集 | 见 OGM-GE 仓库 README |
| MM-IMDb | 第二数据集 | 见官方仓库 |
| CLIP ViT-B/32 | 图像骨干（冻结） | HuggingFace（设 `HF_ENDPOINT=https://hf-mirror.com`） |
| BERT-base-uncased | 文本骨干（冻结） | 同上 |

## 实验结果

> 占位表格，跑完实验后由 `results/runs.csv` 汇总生成。

| 方法 | 干净 | 文本加噪 σ=1.0 | 文本缺失 |
|---|---|---|---|
| Late Fusion | - | - | - |
| OGM-GE | - | - | - |
| **本文（Ours）** | - | - | - |

## 仓库结构

```
.
├─ README.md              ✅ 上传   项目说明（GitHub 首页展示的就是它）
├─ LICENSE                ✅ 上传   MIT 协议
├─ .gitignore             ✅ 上传   排除数据/权重/缓存
├─ requirements.txt       ✅ 上传   依赖清单
├─ configs/base.json      ✅ 上传   超参配置
├─ src/                   ✅ 上传   源码
│   ├─ __init__.py
│   └─ train.py
├─ results/               ✅ 上传   实验结果表（runs.csv / summary.md）
├─ docs/figures/          ✅ 上传   论文用图
├─ .github/workflows/     ✅ 上传   CI 配置
├─ data/                  ❌ 不上传 数据集（体积大、有版权）
├─ feats/                 ❌ 不上传 预计算特征
├─ checkpoints/           ❌ 不上传 模型权重（.pth/.npz）
└─ runs/                  ❌ 不上传 TensorBoard 日志
```

## 引用

```bibtex
@misc{yourname2026gram,
  title  = {质量门控格拉姆表征对齐},
  author = {你的名字},
  year   = {2026},
  note   = {本科毕业设计}
}
```

## License

本项目采用 [MIT License](LICENSE)。
