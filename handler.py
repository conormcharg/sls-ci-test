# handler.py

import numpy as np
import boto3


def main(event, context):
    a = np.arange(15).reshape(3, 5)

    print("Your numpy array:")
    print(a)

    return("Hello world")


if __name__ == "__main__":
    main('', '')
