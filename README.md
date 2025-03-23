Para o desenvolvimento desse teste automatizado, foi utilizado Selenium em phyton.
O teste consiste em uma jornada completa ded simulação de crédito imobiliário no banco Caixa Econômica Federal.
A jornada consiste em abrir o chrome, preencher os campos obrigatórios com valores válidos, finalizar a simulação e baixar o PDF com o resultado (arquivo estará presente na paste de downloads)
OBS: utilizei o time.freeze() na função de preencher os espaços da simulação, porque 2 dropbox estavam causando problema na hora de carregar e precisei usar o time.freeze() para garantir que rodasse corretamente.
