# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from .import package
from .package import variables as glv






from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd
import ast

def main(id,link,password):
    # === 1. 配置并启动一次浏览器 ===
    options = Options()
    options.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data")
    options.add_argument("--profile-directory=Default")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 15)
    try:
        print(f"🔄 正在处理id为 {id} 的链接: {link}")
        # 打开新链接（复用同一个窗口）
        driver.get(link)
        # 等待页面加载完成
        wait.until(EC.presence_of_element_located((By.ID, "ice-container")))
        sleep(1)  # 给 JS 渲染留时间（Quark 需要）
        error_elements = driver.find_elements(
            By.XPATH,
            '//*[@id="ice-container"]/div[1]/div[2]/div[1]/div[1]/div[2]/p'
        )
        if error_elements:
            print("❌ 分享已失效，跳过")
            return 2

        # 提取码
        # //*[@id="accessCode"]
        # ant-btn ShareReceivePC--submit-btn--1tyQVhs ant-btn-primary
        # //*[@id="ice-container"]/div[1]/div[2]/div/div[1]/div[5]/button
        elements1 = driver.find_elements(By.XPATH, '//*[@id="ice-container"]/div[1]/div[2]/div/div[1]/div[5]/button')
        if elements1:
            if not password:
                print(f"{link}需要提取码，但是为空")
                return 2
            # 找到输入框并输入文本
            input_element = driver.find_element(By.XPATH, '//*[@id="ice-container"]/div[1]/div[2]/div/div[1]/div[3]/input')
            input_element.send_keys(password)
            input_element.send_keys(Keys.ENTER)
            sleep(1)
            # elements_pp = driver.find_elements(By.XPATH, '//*[@id="ice-container"]/div[1]/div[2]/div/div[1]/div[3]/input')
            # if not elements_pp:
            #     break
            # else:
            #     input_element.clear()
            #     sleep(0.5)
            # sleep(1)
            elements_hh = driver.find_elements(By.XPATH, '//*[@id="ice-container"]/div[1]/div[2]/div/div[1]/div[3]/input')
            if elements_hh:
                print(f"{link}的提取码失效或者转存失败")
                return 3
        # 等待页面关键元素加载（避免未加载完就操作）
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ice-container"]')))
        sleep(1)  # 可选：Quark 渲染可能需要一点时间
        # tar='//*[@id="ice-container"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]'
        # element_text = wait.until(EC.element_to_be_clickable((By.XPATH, tar))).text
        # print(element_text)
        # if "T" in element_text:
        #     return 4
        #     continue
        # === 点击文件图标 ===
        target_xpath = '//*[@id="ice-container"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/div[3]'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
        element.click()
        sleep(1)
        # === 点击“全部文件” ===
        target_xpath = '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li/span[2]/span[2]'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
        element.click()
        sleep(1.5)
        # === 点击“新建文件夹” ===
        target_xpath = '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/button'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
        element.click()
        sleep(1.5)
        # === 全选 + 输入文件夹名 + 回车 ===
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        sleep(1)
        actions.send_keys(id).perform()
        actions.send_keys(Keys.ENTER).perform()
        sleep(0.5)
        # === 点击“确认”按钮 ===
        target_xpath = '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div/button[2]'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
        element.click()

        # === 点击“保存网盘” ===
        target_xpath = '//*[@id="ice-container"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div/div[2]/button'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
        element.click()

        sleep(2)
        print(f"✅ {link} 处理完成")
        return 1

    except Exception as e:
        print(f"❌ 处理失败: {e}")
        # # 可选：保存错误截图
        # driver.save_screenshot(f"{index}quark_error.png")
        return 3
    driver.quit()






id1="1"
link1="https://pan.quark.cn/s/73be6acc2b43#/list/share"
passward1=""

main(id1,link1,passward1)
