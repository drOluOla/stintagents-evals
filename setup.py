from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="stintagents-evals",
    version="0.1.0",
    author="Oluseyi",
    description="Multi-agent voice interaction system for employee onboarding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drOluOla/stintagents-evals",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.59.7",
        "openai-agents[voice]==0.5.0",
        "gradio==5.49.1",
        "numpy>=2.1.3",
        "torch>=2.5.1",
        "scipy>=1.14.1",
        "faster-whisper==1.2.1",
        "pydub>=0.25.1",
    ],
)
