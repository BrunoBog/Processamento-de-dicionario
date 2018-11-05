<h1> Vetor de palavras </h1>
Algoritimo que lê frases contidas nos arquivos texto1.txt e texto2.txt e estrutura as palavras contidas nas frases em forma de um dicionario estruturado.
<h2>Setup</h2>
Para o processamento das stop-words este algotitimo utiliza a biblioteca open source 
 <a href ="https://github.com/nltk/nltk"> Natural Language Toolkit (NLTK) </a> <br/>
 
Para executar este algoritimo é necessario instalar sua dependência com o comando: <br/>
<h5>pip install -r requirements.txt</h5>
Após instalada a dependência executar no terminal o comando: <br/>
<h5>python -m nltk.downloader stopwords</h5>

<h2> Testes Unitários </h2>
Para executar os testes unitarios do projeto basta ir até a pasta raiz do sistema (Yellow) e executar o seguinte comando:<br/>
<h5>python setup.py test</h5>

Após esta configuração prévia você deve copiar os arquivos que contém as frases para a pasta Yellow. <br/>
 Então executar com Python3 o arquivo app.py que está em: Yellow/scr/app.py ex:
 <h5>python3 Yellow/scr/app.py</h5>
