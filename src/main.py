# linear algebra
import numpy as np

# data processing
import pandas as pd

import logging


def main():
    logging.info("Start processing")
    training_data = pd.read_csv("../data/train.csv")
    print(training_data.head())
    logging.info("the end")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.DEBUG)
    main()

