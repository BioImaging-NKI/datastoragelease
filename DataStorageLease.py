import logging
import os

from datastoragelease import datastoragelease

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    datastoragelease()
    os.system("pause")
