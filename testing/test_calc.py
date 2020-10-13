#-*- coding:utf-8 -*-

import sys

import pytest
import yaml

print(sys.path.append('..'))
from PythonCode.calc import Calculator

with open("../TestData/calc.yaml") as f:
    data = yaml.safe_load(f)
    adddatas = data['add'].values()
    addids = data['add'].keys()

    subdatas = data['sub'].values()
    subids = data['sub'].keys()

    muldatas = data['mul'].values()
    mulids = data['mul'].keys()

    divdatas = data['div'].values()
    divids = data['div'].keys()


class TestCalc:
    cal = Calculator()

    @pytest.mark.parametrize('a,b,c', list(adddatas), ids=addids)
    def test_add(self,start, a, b, c):
        assert 3 == self.cal.add(1, 2)
        assert c == self.cal.add(a, b)

    # @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['check_add'])
    @pytest.mark.parametrize('a,b,c', subdatas, ids=subids)
    def test_sub(self,start, a, b, c):
        assert c == self.cal.sub(a, b)
        # assert 2 == self.cal.sub(3, 1)

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,c', muldatas, ids=mulids)
    def test_mul(self,start, a, b, c):
        assert c == self.cal.mul(a, b)
        # assert 0 == self.cal.mul(0, 3)

    @pytest.mark.parametrize('a,b,c', divdatas, ids=divids)
    def test_div(self,start, a, b, c):
        assert c == self.cal.div(a, b)
        # assert 1 == self.cal.div(5, 5)

# 控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
# 减法依赖加法， 除法依赖乘法
    @pytest.mark.first
    def check_add(self):
        assert 3==self.cal.add(2,1)

    @pytest.mark.dependency(depends=['test_mul'])
    @pytest.mark.parametrize('a,b,c', [(1,2,0.5),(3,1,3)])
    # @pytest.mark.run(order=4)
    def check_div(self,start, a, b, c):
        assert c == self.cal.div(a, b)