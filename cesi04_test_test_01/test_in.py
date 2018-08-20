import os, sys

sys.path.append(os.getcwd())
import yaml
import pytest
import allure


def data_in():
    data = []
    with open("./test_1.yaml", "r", encoding="utf-8") as f:
        data_1 = yaml.load(f)
        for x in data_1.values():
            for y in x.values():
                i = y.get("age"), y.get("name"), y.get("height")
                data.append(i)
    return data


class Test_01:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a,b,c", data_in())
    def test_01(self, a, b, c):
        allure.attach("a","asd")
        print(a, b, c)
