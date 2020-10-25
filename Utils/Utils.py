from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


def getProjectFolder() -> str:
    """Retornando a pasta do projeto."""
    return str(Path(__file__).parent.parent)


def printLin():
    print("-------------------------")


def getValue(item, parameter):
    try:
        value = item.get(parameter, None)
        return value
    except:
        value = None
        return value


def getEnv(name):
    return str(os.getenv(name))
