from setuptools import setup, find_packages

setup(
    name="intent-state-machine",
    version="0.1.0",
    packages=find_packages(),
    description="Intent State Machine (Proposal #78) - 追踪与治理 Agent 意图漂移的核心引擎",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Xiaoxue Security Team",
    url="https://github.com/senmud/intent-state-machine",
    install_requires=[
        "sentence-transformers>=2.2.2",
        "numpy>=1.21.0",
        "pydantic>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
)