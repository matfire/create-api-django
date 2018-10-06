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


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
# 	"""Test the CLI."""
# 	runner = CliRunner()
# 	result = runner.invoke(cli.main)
# 	assert result.exit_code == 0
# 	help_result = runner.invoke(cli.main, ['--help'])
# 	assert help_result.exit_code == 0
# 	assert '--help  Show this message and exit.' in help_result.output

def test_folder_creation():
	cli.create_folder("test_folder")
	assert os.path.isdir("test_folder")
	shutil.rmtree("test_folder")
