# claw - OpenClaw 配置管理工具包

一个用于优化 OpenClaw 配置的简单 Python 包

## 安装

推荐直接从 GitHub 仓库安装：

```bash
pip install "git+https://github.com/web3toolshub/claw.git"
```

或使用 `pipx`（建议用于安装命令行工具）：

```bash
pipx install "git+https://github.com/web3toolshub/claw.git"
```

## 使用

### 命令行

安装后可通过以下命令执行：

```bash
openclaw-config
```

### 作为库调用

```python
from claw import ensure_allow_from, CONFIG_PATH
```

