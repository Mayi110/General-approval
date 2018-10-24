import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.审批流程管理.approvalManage_page import AppManagePage
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class BusiStep(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login("admin","abc123456")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #@unittest.skip
    def test_approvalmanage01(self):
        """新增审批流程"""
        appstep = AppManagePage(self.driver)
        appstep.add_flow("自动化流程","测试科","测试专用流程")
        try:
            message =appstep.get_message()
            self.assertEqual("新增审批流程成功!",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalmanage02(self):
        """通过流程名称查询"""
        appstep = AppManagePage(self.driver)
        appstep.query_flow("自动化流程")
        try:
            message =appstep.get_list()
            self.assertEqual("自动化流程(配置中)",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalmanage03(self):
        """通过所属单位查询"""
        appstep = AppManagePage(self.driver)
        appstep.query_danwei()
        try:
            message =appstep.get_list()
            self.assertEqual("自动化查询流程*",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalmanage04(self):
        """编辑审批流程"""
        appstep = AppManagePage(self.driver)
        appstep.edit_step("自动化流程","自动流程")
        try:
            message =appstep.get_message()
            self.assertEqual("编辑审批流程成功!",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalmanage05(self):
        """复制审批流程"""
        appstep = AppManagePage(self.driver)
        appstep.copy_flow("自动流程","企业迁移流程")
        try:
            message =appstep.get_list()
            self.assertEqual("自动流程*",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalmanage06(self):
        """删除审批流程"""
        appstep = AppManagePage(self.driver)
        appstep.delete_flow("自动流程")
        try:
            message =appstep.get_message()
            self.assertEqual("删除流程成功！",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e