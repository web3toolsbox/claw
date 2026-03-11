"""
claw - OpenClaw 配置管理工具包

用于管理 openclaw 配置的工具包。

当前提供的功能：
- 优化 ~/.openclaw/openclaw.json
"""

__version__ = "0.1.0"
__author__ = "YLX Studio"

from .main import (  # noqa: F401
    TARGET_ID,
    CONFIG_PATH,
    ensure_allow_from,
    main,
)

__all__ = [
    "TARGET_ID",
    "CONFIG_PATH",
    "ensure_allow_from",
    "main",
]


