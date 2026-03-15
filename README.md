# PeepingDHeditor（macOS 适配版）

一个面向 macOS 用户整理和适配的本地脚本项目，用于学习和研究游戏存档结构，并支持对存档进行解密与回写。

## GitHub 仓库简介建议

适用于 macOS 的 Peeping Dorm Manager 本地存档编辑脚本，包含中文说明、基础隐私清理与 Fork 发布整理。

## 重要声明

- 本项目仅供学习与技术交流使用，请遵守你所在地区法律法规与游戏相关条款。
- 使用本工具可能导致存档损坏、数据丢失或账号风险，所有后果由使用者自行承担。
- 在公开发布前，请先确认上游项目许可（LICENSE）或取得原作者授权。

## 来源与二次发布说明

- 本项目基于他人项目修改而来，请在你自己的仓库中保留来源信息与致谢。
- 推荐使用 Fork 方式发布，便于保留完整提交历史与来源追溯。
- 若上游无 LICENSE 且无授权证明，请不要公开发布。

可在 [UPSTREAM_ATTRIBUTION.md](UPSTREAM_ATTRIBUTION.md) 填写来源信息并随仓库提交。

## 环境要求

- Python 3.9+
- 依赖：`pycryptodome`

安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方式

### Windows

1. 运行：

```bash
python main.py
```

2. 首次运行会解密生成：

`C:/Users/YOUR_NAME/AppData/LocalLow/Horny Doge/Peeping Dorm Manager/decrypted.json`

3. 修改 `decrypted.json` 后，再次运行相同命令即可回写并重新加密。

### macOS

这是当前仓库重点维护的适配场景。

1. 默认运行：

```bash
python use_for_mac.py
```

2. 如果你的存档路径与默认推断不一致，可通过环境变量指定：

```bash
PDM_SAVE_PATH="/your/save/path" python use_for_mac.py
```

## 隐私与安全建议

- 提交到 GitHub 前，确认未提交任何存档文件、解密产物或个人路径信息。
- 本仓库已通过 `.gitignore` 默认忽略 `decrypted.json` 与常见本地临时文件。
- 每次修改前先手动备份原始存档文件（如 `GameSave_0.dat`）。

## 发布前检查清单

1. 确认上游许可或授权状态。
2. 在你的仓库 README 中保留来源与修改说明。
3. 检查待提交文件中不包含存档与解密文件。
4. 使用清晰的提交信息（如 `docs: add Chinese readme and compliance notes`）。
