"""训练入口（占位文件）。

这只是"仓库格式示例"，里面不放真实实现。
真实项目里这个文件负责：加载配置 → 构建数据 → 训练 → 评估 → 写 results/runs.csv。

用法示例：
    python -m src.train --config configs/base.json --epochs 60
"""
from __future__ import annotations

import argparse
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/base.json")
    ap.add_argument("--epochs", type=int, default=60)
    args = ap.parse_args()

    cfg = json.load(open(args.config, encoding="utf-8"))
    print("config loaded:", json.dumps(cfg, ensure_ascii=False))
    print(f"TODO: 在这里实现训练循环（{args.epochs} epochs）")


if __name__ == "__main__":
    main()
