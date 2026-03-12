# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pathlib import Path


root = Path(__file__).parent
readme_file = root / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""


setup(
    name="claw",
    version="0.1.1",
    author="YLX Studio",
    author_email="",
    description="用于管理 OpenClaw 配置（channels.telegram.allowFrom）的简单工具包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/web3toolsbox/claw",
    packages=find_packages(),
    license_files=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
    install_requires=[],
    entry_points={
        "console_scripts": [
            # 安装后可通过 `openclaw-config` 命令调用 main()
            "openclaw-config=claw.main:main",
        ],
    },
    keywords="openclaw, config, telegram",
    project_urls={
        "Source": "https://github.com/web3toolsbox/claw",
    },
)

