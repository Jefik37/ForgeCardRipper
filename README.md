<h2><b>Requisitos</b></h2>
<ul>
  <li><a href="https://www.python.org/downloads/release/python-3115/">Python 3.11</a></li>
  <li><a href="https://github.com/tesseract-ocr/tesseract">Tesseract</a></li>
  <li><a href="https://pypi.org/project/pytesseract/">Pytesseract 0.3.10</a></li>
  <li><a href="https://pypi.org/project/PyAutoGUI/">PyAutoGUI 0.9.54</a></li>
  <li><a href="https://pypi.org/project/Pillow/">Pillow 10.0.0</a></li>
  <li><a href="https://pypi.org/project/pynput/">pynput 1.7.6</a></li>
</ul>

<h2><b>Configurações</b></h2>

<ul><li>Tamanho Padrão da Fonte no Forge: 18</li></ul>
<li>Atualize o arquivo <code>main.py</code> com o diretório de instalação do Tesseract (linha 9), de acordo com a sua instalação.</li>
<li>Para gerar um arquivo atualizado com os nomes usando o <code>name_generator.py</code>, coloque-o em <code>[LOCAL DE INSTALAÇÃO DO FORGE]\res\languages</code> e execute. Será gerado um arquivo <code>names.csv</code>. Coloque-o no mesmo diretório do <code>main.py</code>.</li>

<h3>Em monitores 1920x1080p:</h3>
<ul>
  <li>Definir escala do sistema em: 100%</li>
  <li>Definir a variável <code>four_k</code> no <code>main.py</code> como <code>False</code>.</li>
</ul>

<h3>Em monitores 3840x2160p (melhor qualidade das imagens):</h3>
<ul>
  <li>Definir escala do sistema em: 200%</li>
  <li>Definir a variável <code>four_k</code> no <code>main.py</code> como <code>True</code>.</li>
</ul>

<h2><b>Usagem</b></h2>


  <h3>Gerar Cartas Individuais</h3>
  <ul>
    <li>Selecione a carta que quiser e clique nela com o botão do meio do mouse. As cartas irão para a parta <code>card</code>, no mesmo diretório do <code>main.py</code>.
    Recomenda-se segurar o botão do meio do mouse com a carta aberta por pelo menos dois segundos.</code></li>
  <li>Caso a imagem esteja cortada ou não tenha carregado direito, basta clicar novamente que ela irá ser carregada mais uma vez.</li>
  </ul>
  <h3>Gerar Cartas A Partir De Um Deck</h3>
  <ul>
    <li>Abra o deck e selecione a primeira carta.</li>
    <li>Aperte a tecla <code>ctrl</code> e <b>NÃO</b> mexa o mouse nem aperte nenhuma tecla até que tenha terminado.</li>
  </ul>


<h2><b>Guia e Demonstração</b></h2

https://youtu.be/MbFaPJ6pBqY
