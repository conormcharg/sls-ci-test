import boto3
import pytest
import numpy as np
import scipy as sp
from handler import main

def test_handler_output():
    assert main(None, None) == np.arange(15).reshape(3, 5)