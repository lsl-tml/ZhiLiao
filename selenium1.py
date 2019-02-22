import time

from selenium import webdriver

from MySQL import Mysqlcz
ips = Mysqlcz().getAll("select ht,ip,post from ips3")
# 谷歌驱动地址
driver_path='C:\ProgramData\Anaconda3\chromedriver.exe'
# 保存参数的变量           o可能是小写
options = webdriver.ChromeOptions()
# 设置不加载图片
prefs = {'profile.managed_default_content_settings.images': 2}

for ht,ip,post in ips:

    ipx = ht.lower()+"://"+ip+":"+post
    print(ipx)
    # 设置代理ip
    options.add_argument("--proxy-server=%s"%ipx)
    # 设置不加载图片参数实例化
    options.add_experimental_option('prefs',prefs)
    #实例参数
    driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
    # 设置隐式等待时间（即不管页面是否加载完成，等待时间后执行下面程序）
    driver.implicitly_wait(15)
    # 打开网站
    driver.get('http://www.171011.com')
    # time.sleep(5)
    driver.close()