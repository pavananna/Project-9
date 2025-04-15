{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPW6VpPhWj+mK8ee0Q3E3TE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/pavananna/Project-9/blob/main/Streamlit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "STmv65eSzcZ3",
        "outputId": "b26a45e1-dc13-478b-eaac-b549c906068b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.44.1-py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.4)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.13.1)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.34.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.24.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.44.1-py3-none-any.whl (9.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.8/9.8 MB\u001b[0m \u001b[31m64.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m98.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.44.1 watchdog-6.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain-cli"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UzQ8qof2zyp5",
        "outputId": "adcb455b-e0a1-43bd-b517-603d76a1cc45"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain-cli\n",
            "  Downloading langchain_cli-0.0.36-py3-none-any.whl.metadata (956 bytes)\n",
            "Requirement already satisfied: typer<1.0.0,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from typer[all]<1.0.0,>=0.9.0->langchain-cli) (0.15.2)\n",
            "Requirement already satisfied: gitpython<4,>=3 in /usr/local/lib/python3.11/dist-packages (from langchain-cli) (3.1.44)\n",
            "Collecting langserve>=0.0.51 (from langserve[all]>=0.0.51->langchain-cli)\n",
            "  Downloading langserve-0.3.1-py3-none-any.whl.metadata (40 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m40.3/40.3 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting uvicorn<1.0,>=0.23 (from langchain-cli)\n",
            "  Downloading uvicorn-0.34.1-py3-none-any.whl.metadata (6.5 kB)\n",
            "Collecting tomlkit>=0.12 (from langchain-cli)\n",
            "  Downloading tomlkit-0.13.2-py3-none-any.whl.metadata (2.7 kB)\n",
            "Collecting gritql<1.0.0,>=0.2.0 (from langchain-cli)\n",
            "  Downloading gritql-0.2.0-py2.py3-none-any.whl.metadata (1.7 kB)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython<4,>=3->langchain-cli) (4.0.12)\n",
            "Requirement already satisfied: httpx<1.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (0.28.1)\n",
            "Requirement already satisfied: langchain-core<0.4,>=0.3 in /usr/local/lib/python3.11/dist-packages (from langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (0.3.51)\n",
            "Requirement already satisfied: orjson<4,>=2 in /usr/local/lib/python3.11/dist-packages (from langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (3.10.16)\n",
            "Requirement already satisfied: pydantic<3.0,>=2.7 in /usr/local/lib/python3.11/dist-packages (from langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (2.11.3)\n",
            "Collecting fastapi<1,>=0.90.1 (from langserve[all]>=0.0.51->langchain-cli)\n",
            "  Downloading fastapi-0.115.12-py3-none-any.whl.metadata (27 kB)\n",
            "Collecting sse-starlette<2.0.0,>=1.3.0 (from langserve[all]>=0.0.51->langchain-cli)\n",
            "  Downloading sse_starlette-1.8.2-py3-none-any.whl.metadata (5.4 kB)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (8.1.8)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (4.13.1)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (13.9.4)\n",
            "\u001b[33mWARNING: typer 0.15.2 does not provide the extra 'all'\u001b[0m\u001b[33m\n",
            "\u001b[0mRequirement already satisfied: h11>=0.8 in /usr/local/lib/python3.11/dist-packages (from uvicorn<1.0,>=0.23->langchain-cli) (0.14.0)\n",
            "Collecting starlette<0.47.0,>=0.40.0 (from fastapi<1,>=0.90.1->langserve[all]>=0.0.51->langchain-cli)\n",
            "  Downloading starlette-0.46.2-py3-none-any.whl.metadata (6.2 kB)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython<4,>=3->langchain-cli) (5.0.2)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<1.0,>=0.23.0->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (4.9.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1.0,>=0.23.0->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1.0,>=0.23.0->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx<1.0,>=0.23.0->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (3.10)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (0.3.28)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (9.1.2)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (1.33)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (6.0.2)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (24.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0,>=2.7->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.1 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0,>=2.7->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (2.33.1)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0,>=2.7->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (0.4.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (2.18.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (3.0.0)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (2.32.3)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (0.23.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.9.0->typer[all]<1.0.0,>=0.9.0->langchain-cli) (0.1.2)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<1.0,>=0.23.0->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (1.3.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langsmith<0.4,>=0.1.125->langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langsmith<0.4,>=0.1.125->langchain-core<0.4,>=0.3->langserve>=0.0.51->langserve[all]>=0.0.51->langchain-cli) (2.3.0)\n",
            "Downloading langchain_cli-0.0.36-py3-none-any.whl (120 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m120.2/120.2 kB\u001b[0m \u001b[31m5.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gritql-0.2.0-py2.py3-none-any.whl (5.2 kB)\n",
            "Downloading langserve-0.3.1-py3-none-any.whl (1.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m24.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tomlkit-0.13.2-py3-none-any.whl (37 kB)\n",
            "Downloading uvicorn-0.34.1-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.4/62.4 kB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading fastapi-0.115.12-py3-none-any.whl (95 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m95.2/95.2 kB\u001b[0m \u001b[31m7.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading sse_starlette-1.8.2-py3-none-any.whl (8.9 kB)\n",
            "Downloading starlette-0.46.2-py3-none-any.whl (72 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m72.0/72.0 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: gritql, uvicorn, tomlkit, starlette, fastapi, sse-starlette, langserve, langchain-cli\n",
            "Successfully installed fastapi-0.115.12 gritql-0.2.0 langchain-cli-0.0.36 langserve-0.3.1 sse-starlette-1.8.2 starlette-0.46.2 tomlkit-0.13.2 uvicorn-0.34.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from langchain.chains.llm import LLMChain\n",
        "from langchain.chains.summarize import load_summarize_chain"
      ],
      "metadata": {
        "id": "7eze_9dizsyl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if \"query_history\" not in st.session_state:\n",
        "    st.session_state.query_history = []\n",
        "\n",
        "query = st.text_input(\"Enter your query\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h05ahz1k1oqW",
        "outputId": "f71a4429-ead1-4cf9-cb58-df47301b4bca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-04-15 05:22:07.187 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.192 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
            "2025-04-15 05:22:07.194 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.196 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.198 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.201 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.201 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.203 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.206 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:22:07.328 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-04-15 05:22:07.330 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if st.button(\"Get News\"):\n",
        "    if query:\n",
        "      summaries = load_summarize_chain(query)\n",
        "      response =LLMChain.run({\"query\": query,\"summaries\": summaries})\n",
        "\n",
        "      # Save Query & Response\n",
        "      st.session_state.query_history.append({\"Query\": query, \"Summary\": response})\n",
        "\n",
        "      st.subheader(\" Summary:\")\n",
        "      st.write(response)\n",
        "\n",
        "        # Download as CSV\n",
        "      df = pd.DataFrame(st.session_state.query_history)\n",
        "      csv = df.to_csv(index=False).encode(\"utf-8\")\n",
        "\n",
        "      st.download_button(\" Download History\", csv, \"summary_history.csv\", \"text/csv\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HwVbSnoC5cOu",
        "outputId": "60498685-2187-46a3-c0b2-f101fcbf5fee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-04-15 05:37:58.592 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:37:58.593 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:37:58.594 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:37:58.597 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-15 05:37:58.602 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "b150lzy38khi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}