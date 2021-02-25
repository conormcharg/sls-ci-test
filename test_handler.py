import boto3
import pytest
import numpy as np
import scipy as sp
from handler import main

def test_handler_output():

    target = np.arange(15).reshape(3, 5).tolist()
    print(target)

    actual = main(None, None).tolist()
    print(actual)

    assert main(None, None).tolist() == target