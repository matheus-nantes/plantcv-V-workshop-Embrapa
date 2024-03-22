# plantcv-V-workshop-Embrapa

Repositório utilizado para compartilhamento de códigos para execução de tutoriais na ferramenta plantcv durante o V Workshop de Melhoramento Vegetal da Embrapa Gado de Corte

  

### Como executar:

```python
python .\exec.py
#o  nome  do  arquivo neste  caso  é .\exec.py, porém, se quiser criar e executar outros, basta substituir no terminal
```

  

>*repare que, o seu terminal está localizado na pasta considerando que o seu terminal está localizado na pasta "PLANTCV", para verificar isto, basta confirir se o ultimo nome que aparece na última linha do terminal, antes do símbolo ">", é "PLANTCV".

 
### Dica:
 Para navegar nas pastas do seu computador pelo terminal, basta utilizar o comando "ls" para exibir os arquivos do diretório atual e "cd nome-da-pasta" para mandar o terminal para dentro da pasta, ou "cd .." para voltar uma pasta para trás. Por exemplo, considere que seu computador tem as pastas e atualmente o seu terminal está localizado em "atual": 
<ul>
	<li> atual<b><-</b> </li>
	<ul>
		<li>um</li>
		<li>dois</li>
		<ul>
			<li>destino1</li>
		</ul>
		<li>três</li>
	<ul>
		<li>destino2</li>
	</ul>
</ul>

---
Ao executar o comando:
```c
cd dois
```
Teremos:
<ul>
	<li> atual </li>
	<ul>
		<li>um</li>
		<li>dois<b><-</b></li>
		<ul>
			<li>destino1</li>
		</ul>
		<li>três</li>
		<ul>
		<li>destino2</li>
	</ul>
	</ul>
</ul>

---
Ao executar o comando:
```c
cd destino1
```
Teremos:
<ul>
	<li> atual </li>
	<ul>
		<li>um</li>
		<li>dois</li>
		<ul>
			<li>destino1<b><-</b></li>
		</ul>
		<li>três</li>
	<ul>
		<li>destino2</li>
	</ul>
</ul>

---
Ao executar o comando:
```c
cd ..
```
Teremos:
<ul>
	<li> atual </li>
	<ul>
		<li>um</li>
		<li>dois<b><-</b></li>
		<ul>
			<li>destino1</li>
		</ul>
		<li>três</li>
	<ul>
		<li>destino2</li>
	</ul>
</ul>

---
Ao executar o comando:
```c
cd ..
```
Teremos:
<ul>
	<li> atual <b><-</b></li>
	<ul>
		<li>um</li>
		<li>dois</li>
		<ul>
			<li>destino1</li>
		</ul>
		<li>três</li>
	<ul>
		<li>destino2</li>
	</ul>
</ul>

---
Ao executar o comando:
```c
cd três
```
Teremos:
<ul>
	<li> atual </li>
	<ul>
		<li>um</li>
		<li>dois</li>
		<ul>
			<li>destino1</li>
		</ul>
		<li>três<b><-</b></li>
	<ul>
		<li>destino2</li>
	</ul>
</ul>

---
Ao executar o comando:
```c
cd destino2
```
Teremos:
<ul>
	<li> atual </li>
	<ul>
		<li>um</li>
		<li>dois</li>
		<ul>
			<li>destino1</li>
		</ul>
		<li>três</li>
	<ul>
		<li>destino2<b><-</b></li>
	</ul>
</ul>

Vamos supor que seu código em Python esteja dentro da pasta "destino2", após essas operações, basta executar o comando informado no início para que seu script em Python seja executado corretamente


  ---

### Detalhes do código:

Verifique na linha 17 está definido o nome da imagem que será analisada, então, caso você deseje realizar testes com outras imagens, basta arrastá-las para esta pasta e colocar corretamente nesta parte do código.

```python
self.image = "./quinoa_seeds.jpg"
```
  <br>

No arquivo "exec.py", na linha 18, que contém o seguinte código:

```python
self.debug = "print"
```
Esta linha define como será a saída do seu código, se o valor for print, os resultados e novas imagens geradas serão salvas na pasta atual, e se o valor for plot, as imagens geradas serão exibidas em uma nova aba e assim que você fechar essa aba, a imagem será excluída e o próximo comando será executado.

