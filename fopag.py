from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://portal.fazenda.sp.gov.br/")

navegador.find_element_by_xpath('//*[@id="plHome"]/div[2]/aside/div/div[2]/ul/li/div[4]/div/div/div[2]/a').click()

navegador.find_element_by_xpath('//*[@id="ctl00_PlaceHolderMain_EditModePnlDisplay_NoteField5__ControlWrapper_RichHtmlField"]/p[1]/a').click()
