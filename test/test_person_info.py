# -*- coding: utf-8 -*-
__author__ = 'bizhen'

from page.pages import *
from base.action import ElementActions
import pytest

class TestPersonInfo:
 
    @pytest.fixture
    def open_person_info(self, action: ElementActions):
        action.click(MyPage.我的)
        action.click(MyPage.已登录头像)
        action.click(UpOwnerPage.编辑)
    
    @pytest.allure.step("用户资料页面") 
    def test_not_change_person_info(self,open_person_info):
        '''
            预置条件：用户已登录
            操作步骤：.......
        '''
        open_person_info
		
    #def test_1(self,open_person_info):
       # open_person_info