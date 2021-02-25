import boto3
import pytest
from handler import main

def test_handler_output():
    assert main(None, None) == "Hello world"