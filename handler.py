# handler.py

import numpy as np
import scipy as sp
import boto3


def main(event, context):
    a = np.arange(15).reshape(3, 5)

    print("Your numpy array:")
    print(a)

    return(a)


if __name__ == "__main__":
    main('', '')
