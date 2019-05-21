# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from utils import L
from utils.ExtentHTMLTestRunner import HTMLTestRunner
import pytest
from allure.constants import AttachmentType


class TestLogin:
    #def login(self, action: ElementActions):#test_login
        #L.d('test_login')
        #account = Steps.get_account()
        #action.click(HomePage.登录入口)
       #action.text(LoginPage.账户, account[0])
       # action.text(LoginPage.密码, account[1])
       # action.sleep(1)
       # action.click(LoginPage.登录)
       # assert action.is_toast_show('欢迎回来')
   
    def test_rrtv_login(self, action: ElementActions):
        L.d('rrtv login')
        account = Steps.get_account()
        action.click(MyPage.我的)
        action.click(MyPage.头像)
        action.click(LoginPage.账号密码登录)		
        action.text(LoginPage.账户, account[0])
        action.back_press()
        action.text(LoginPage.密码, account[1])
        action.back_press()
        action.click(LoginPage.登录)
        assert action.is_text_displayed("test")

        
        