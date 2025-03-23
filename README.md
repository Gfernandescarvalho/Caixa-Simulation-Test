# Testa automatizado Selenium
### Jornada de simulação de crédito bancário

#### Dependências para a resolução do teste: 
- Google Chrome
- Selenium
- Phyton
---
#### Ao abrir o projeto, utilize o comando para instalar o selenium caso não tenha instalado ainda: pip install selenium 

O teste consiste em uma jornada completa da simulação de crédito imobiliário no banco Caixa Econômica Federal.  

A jornada consiste em abrir o chrome, preencher os campos obrigatórios com valores válidos, finalizar a simulação e baixar o PDF com o resultado (arquivo estará presente na pasta de downloads)  

OBS: utilizei o time.freeze(1) na função de preencher os espaços da simulação, porque 2 dropbox estavam causando problema na hora de carregar e precisei usar o time.freeze(1) para garantir que rodasse corretamente, além de que deixe nesse valor para que o avaliador conseguisse acompanhar o teste e verificar os valores que estão sendo preenchidos durante a simulação.  

