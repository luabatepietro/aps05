from setuptools import setup, find_packages

setup(
    name="aps05",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        'setuptools',
        'numpy',
        'pandas'
    ],
    entry_points={
        "console_scripts": [
            "aps05=aps05.main:main",  # Apontando para a função demo no arquivo demo.py
        ],
    },
    author="Lucas Abatepietro",  # Seu nome
    author_email="luabatepietro@hotmail.com",  # Seu email
    description="APS05",
    long_description=open("README.md", encoding="utf-8").read(),  # Descrição longa com codificação correta
    long_description_content_type="text/markdown",
    url="https://github.com/luabatepietro/aps05.git",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)