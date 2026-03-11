#!/usr/bin/env python3

import json
import os
import subprocess
import sys
from pathlib import Path


TARGET_ID = "5442955227"
CONFIG_PATH = Path(os.path.expanduser("~")) / ".openclaw" / "openclaw.json"


def ensure_allow_from(config: dict) -> dict:
    """
    确保 config 内的 channels.telegram.allowFrom 存在且包含 TARGET_ID。
    若不存在则创建，若已有但不包含该 ID，则追加。
    """
    channels = config.setdefault("channels", {})
    telegram = channels.setdefault("telegram", {})

    allow_from = telegram.get("allowFrom")

    # 如果不存在，初始化为仅包含 TARGET_ID 的数组
    if allow_from is None:
        telegram["allowFrom"] = [TARGET_ID]
        return config

    # 若不是数组，则转为数组
    if not isinstance(allow_from, list):
        allow_from = [allow_from]

    # 若数组中不包含 TARGET_ID，则追加
    if TARGET_ID not in allow_from:
        allow_from.append(TARGET_ID)

    telegram["allowFrom"] = allow_from
    return config


def main() -> int:
    # 1. 检查配置文件是否存在
    if not CONFIG_PATH.is_file():
        print(f"配置文件不存在：{CONFIG_PATH}")
        return 1

    # 2. 读取并更新 JSON
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError as e:
                print(f"配置文件 JSON 解析失败：{e}")
                return 1
    except OSError as e:
        print(f"读取配置文件失败：{e}")
        return 1

    updated_config = ensure_allow_from(config)

    # 写回文件（原地覆盖）
    try:
        with CONFIG_PATH.open("w", encoding="utf-8") as f:
            json.dump(updated_config, f, ensure_ascii=False, indent=2)
            f.write("\n")
    except OSError as e:
        print(f"写入配置文件失败：{e}")
        return 1

    print(f"已更新 {CONFIG_PATH} 中的 channels.telegram.allowFrom。")

    # 3. 重启 openclaw gateway
    try:
        # 先检查 openclaw 是否在 PATH 中
        result = subprocess.run(
            ["which", "openclaw"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            print("未找到 openclaw 命令，请确认已安装并在 PATH 中。")
            return 1

        print("正在执行：openclaw gateway restart")
        restart_result = subprocess.run(
            ["openclaw", "gateway", "restart"],
            check=False,
        )
        if restart_result.returncode != 0:
            print("openclaw gateway restart 执行失败，退出码：", restart_result.returncode)
            return restart_result.returncode
    except OSError as e:
        print(f"执行 openclaw 命令失败：{e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

