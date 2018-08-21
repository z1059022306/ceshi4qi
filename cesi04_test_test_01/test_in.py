import os, sys

sys.path.append(os.getcwd())
import yaml
import pytest
import allure


def data_in():
    data = []
    with open("../test_1.yaml", "r", encoding="utf-8") as f:
        data_1 = yaml.load(f)
        for x in data_1.values():
            for y in x.values():
                i = y.get("age"), y.get("name"), y.get("height")
                data.append(i)
    return data


class Test_01:
   def test_01(self):
        assert 1
        
   def test_02(self):
        assert 0
