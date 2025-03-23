from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import time


#Install Selenium
try:
    import selenium
except ImportError:
    import os
    os.system("pip install selenium")

#Set Chrome to download the final result PDF in the end
download_path = os.path.join(os.path.expanduser("~"), "Downloads")
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local"}],"selectedDestinationId":"Save as PDF","version":2}',
    "savefile.default_directory": download_path,  
    "savefile.prompt_for_download": False,
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})
chrome_options.add_argument("--kiosk-printing")  


#Set driver
driver = webdriver.Chrome(options=chrome_options)


#Function to put elements in the center
def go_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", element)


#Function to select an element
def fieldValue(driver, dropDown_element, dropDownn_id, valor):
    go_to_element(driver, dropDown_element)
    time.sleep(1)
    dropDown = driver.find_element(By.ID, dropDownn_id)
    dropDown.click()
    dropDown.send_keys(valor)
    dropDown.send_keys(Keys.ENTER)


#Initialize Browser
driver.get("https://www8.caixa.gov.br/siopiinternet-web/simulaOperacaoInternet.do?method=inicializarCasoUso&isVoltar=true")
driver.maximize_window()


#TimerController
timerController = WebDriverWait(driver, 20)


#//////////////////////////////////////////////////////////////////////////////

#"Dados Iniciais" section

#//////////////////////////////////////////////////////////////////////////////


#Set individual or legal
personTypeButton  = timerController.until(
    EC.element_to_be_clickable((By.ID, "pessoaF"))
)
go_to_element(driver, personTypeButton)
personTypeButton.click()
time.sleep(0.5)


#Set FinancingType's dropdown
financingTypeDropdown = timerController.until(
    EC.element_to_be_clickable((By.ID, "tipoImovel_input"))
)
fieldValue(driver, financingTypeDropdown, "tipoImovel_input", "Residencial")


#Set FinancingOption's dropdown
finanncingOptionDropdown = timerController.until(
    EC.element_to_be_clickable((By.ID, "grupoTipoFinanciamento_input"))
)
fieldValue(driver,finanncingOptionDropdown, "grupoTipoFinanciamento_input", "Construção")


#Set property value
propertyValue = timerController.until(
    EC.element_to_be_clickable((By.ID, "valorImovel"))
)
fieldValue(driver, propertyValue, "valorImovel", "30000000")


#Set state dropdown
stateDropdown = timerController.until(
    EC.element_to_be_clickable((By.ID, "uf_input"))
)
fieldValue(driver,stateDropdown, "uf_input", "SP" )

#Set city dropdown
cityDropdown = timerController.until(
    EC.element_to_be_clickable((By.ID, "cidade_input"))
)
fieldValue(driver, cityDropdown, "cidade_input", "sao paulo")

print("Section 1 succeeded!! Waiting 1 seconds...")
time.sleep(1)

#Finish the first section
finishFirstSectionButton = timerController.until(
    EC.element_to_be_clickable((By.ID, "btn_next1"))
)
go_to_element(driver, finishFirstSectionButton)
finishFirstSectionButton.click()

#//////////////////////////////////////////////////////////////////////////////

#"Seus Dados" section

#//////////////////////////////////////////////////////////////////////////////


#Set the cpf
cpfNumber = timerController.until(
    EC.element_to_be_clickable((By.ID, "nuCpfCnpjInteressado"))
)
fieldValue(driver, cpfNumber, "nuCpfCnpjInteressado", "346.635.820-52" )


#Set phone number
phoneNumber = timerController.until(
    EC.element_to_be_clickable((By.ID, "nuTelefoneCelular"))
)
fieldValue(driver, phoneNumber, "nuTelefoneCelular", "11949374588")


#Set family income value
familyIncome = timerController.until(
    EC.element_to_be_clickable((By.ID, "rendaFamiliarBruta"))
)
fieldValue(driver, familyIncome, "rendaFamiliarBruta", "30000000")


#Set user's birth date
birthDate = timerController.until(
    EC.element_to_be_clickable((By.ID, "dataNascimento"))
)
fieldValue(driver, birthDate, "dataNascimento", "14011999")


#Checklist confirmations
fgtsCheck = timerController.until(
    EC.element_to_be_clickable((By.ID, "vaContaFgtsS"))
)
go_to_element(driver, fgtsCheck)
fgtsCheck.click()

familyStatusCheck = timerController.until(
    EC.element_to_be_clickable((By.ID, "icFatorSocial"))
)
go_to_element(driver, familyStatusCheck)
familyStatusCheck.click()

print("Section 2 succeeded!! Waiting 1 seconds...")
time.sleep(1)


#Finish the second section
finishSecondStepButton = timerController.until(
    EC.element_to_be_clickable((By.ID, "btn_next2"))
)
go_to_element(driver, finishSecondStepButton)
finishSecondStepButton.click()

#//////////////////////////////////////////////////////////////////////////////

#"Opções" section

#//////////////////////////////////////////////////////////////////////////////


#Verify the chosen option
time.sleep(2)
financingOptionClass = driver.find_elements(By.CLASS_NAME, "js-form-next")
financingOption = financingOptionClass[1]
driver.execute_script("arguments[0].click();", financingOption)

#Final results check
finalTestCheck = timerController.until(
    EC.element_to_be_clickable((By.ID, "botaoVoltar"))
)


#Download Results PDF
driver.execute_script('window.print();')

# Esperar a impressão ser concluída (ajuste o tempo conforme necessário)
time.sleep(10)

# Fechar o navegador
driver.quit()

print("PDF saved at your Downloads Folder!")


#//////////////////////////////////////////////////////////////////////////////

#End

#//////////////////////////////////////////////////////////////////////////////
print("Test succeeded!")  
time.sleep(1)
driver.quit()
