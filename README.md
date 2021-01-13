
# Download

Para clonar o projeto:

	git clone --recursive https://github.com/WesleyMPG/film_bot.git

# Descrição
O projeto é composto de um motor de inferência que está num repositório separado com a finalidade de uma possível futura reutilização em outros projetos.
A base de dados é passada através de um arquivo json, no seguinte formato:
json
{
	"description": {
		"A": "",
		"B": "It's raining?",
		"C": "", 
		"D": "",
		"E": "",
		"F": ""
	},
	"rules": [
		["A and C", "E"],
		["B or !D", "A"],
		["C and (!B or D)", "F"]
	]
}

Cada variável é declarada na seção "description" juntamente com uma string descritiva, que nesse caso se trata da pergunta relacionada à mesma e em seguida tem-se a seção "rules" onde são especificadas as regras. Nessa seção à esquerda está a regra propriamente dita e à direita  está a "consequência".

# Base de Dados

  Essa base de dados visa reunir alguns gêneros e estilos de filmes encontrados nas últimas produções cinematográficas, relacionando-os com o padrão comportamental da sociedade em relação a eles.

O principal objetivo é predizer ou sugerir uma lista de filmes que mais se encaixem com o gosto do usuário e com a ocasião que ele se encontra no momento (com quem irá assistir o filmes, por exemplo, se é com família, amigos ou sozinho).

	
### Documentação completa
 Nesse arquivo pdf é possível encontrar a base de conhecimento completa, com suas variáveis, regras, e árvores utilizadas para decidir as perguntas a serem feitas pelo motor de inferência.

=> [Acesse a Base de Dados](https://drive.google.com/file/d/1Y4bWL2h0d9lczzN-5qB-RudJEDcjcxYX/view?usp=sharing)

A Base de dados dessa aplicação encontra-se no arquivo: 

	knowledge_base.json
