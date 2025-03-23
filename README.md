# Testa automatizado Selenium
### Jornada de simulação de crédito bancário

#### Dependências para a resolução do teste: 
- Google Chrome
- Selenium
- Phyton
- Visual Studio Code
---
#### Ao abrir o projeto, utilize o comando para instalar o selenium caso não tenha instalado ainda: 
- pip install selenium 

O teste consiste em uma jornada completa da simulação de crédito imobiliário no banco Caixa Econômica Federal.  

Para rodar o teste, basta abrir ele no Visual Studio Code, instalar o selenium usando o comando citado à cima e dar play.  

A jornada consiste em abrir o chrome, preencher os campos obrigatórios com valores válidos, finalizar a simulação e baixar o PDF com o resultado (arquivo estará presente na pasta de downloads)  

OBS: quando usar o comando para instalar o Selenium, as vezes, o Visual Studio pode não rodar a instalação por conta de proteção, mas aparece uma mensagem para confiar na fonte do código. É só clicar para confiar que o problema é resolvido.  

OBS 2: utilizei o time.freeze(1) na função de preencher os espaços da simulação, porque 2 dropbox estavam causando problema na hora de carregar e precisei usar o time.freeze(1) para garantir que rodasse corretamente, além de que deixei nesse valor para que o avaliador conseguisse acompanhar o teste e verificar os valores que estão sendo preenchidos durante a simulação.  

