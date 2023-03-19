from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 크롬 웹 드라이버를 설정합니다.
options = webdriver.ChromeOptions()
options.add_argument('headless') # 브라우저 창을 띄우지 않습니다.
options.add_argument('window-size=1920x1080') # 화면 크기를 설정합니다.
options.add_argument("disable-gpu") # GPU 가속을 사용하지 않습니다.

# webdriver를 실행합니다.
driver = webdriver.Chrome(options=options)

# 데이터를 가져올 웹 페이지 URL을 지정합니다.
url = "https://example.com/"

# webdriver를 사용하여 URL에 액세스합니다.
driver.get(url)

# 페이지 소스를 파싱합니다.
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 데이터 수집 및 가공 작업을 수행합니다.
# ...

# webdriver를 종료합니다.
driver.quit()