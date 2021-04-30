# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from pyprojroot import here as get_project_root
import os
os.chdir(get_project_root()) # hack for notebook development

from data_acquisition.main import get_data
from constants import features
import pytest

dataset = get_data()


def test_get_data() -> None:
    # testing that the expected features are all present
    data = dataset.normal
    assert set(data.columns)==set(features), "not all features present in `data`"
