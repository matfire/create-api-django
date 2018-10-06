#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `create_api_django` package."""

import pytest

from click.testing import CliRunner

from create_api_django import create_api_django
from create_api_django import cli
import os
import sys
import shutil


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_folder_creation():
	cli.create_folder("test_folder")
	assert os.path.isdir("test_folder")
	shutil.rmtree("test_folder")
