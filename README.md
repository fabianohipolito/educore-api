# EduCore API 🎓

API REST para gerenciamento acadêmico de estudantes, desenvolvida como projeto de aprendizado e evolução em desenvolvimento backend.

O objetivo deste projeto é construir uma aplicação capaz de organizar informações de alunos, permitindo o gerenciamento de dados acadêmicos como cadastro, notas, frequência e consulta de boletins.

Durante o desenvolvimento serão aplicados conceitos de:

* Desenvolvimento de APIs REST
* Python com Flask
* Banco de dados MongoDB
* Organização de projetos backend
* Boas práticas de programação
* Testes e documentação de APIs

---

## 🚀 Objetivo do Projeto

O EduCore API tem como objetivo criar uma base para um sistema acadêmico onde seja possível:

* Cadastrar estudantes
* Atualizar informações dos alunos
* Registrar notas
* Registrar frequência
* Consultar boletins
* Controlar o status do aluno (ativo/inativo)

O projeto também servirá como base para estudos futuros envolvendo análise de dados e inteligência artificial aplicada à educação.

---

## 🛠️ Tecnologias utilizadas

Atualmente o projeto está sendo desenvolvido utilizando:

* Python
* Flask
* MongoDB
* Git e GitHub

---

## 📚 Funcionalidades planejadas

### Gestão de alunos

* Cadastro de alunos
* Atualização de dados cadastrais
* Identificação de alunos com nomes iguais
* Controle de situação do aluno:

  * Ativo
  * Inativo

### Gestão acadêmica

* Cadastro de disciplinas
* Lançamento de notas
* Atualização de notas
* Registro de faltas
* Justificativa de faltas
* Consulta de boletim

---

## 📊 Regras acadêmicas

O projeto considera um modelo de avaliação composto por:

* Exercícios em aula: 10%
* Trabalho: 30%
* Prova: 60%

Essas informações serão utilizadas para calcular o desempenho acadêmico do estudante.

---

## 🏗️ Estrutura do projeto

A estrutura será organizada buscando separar responsabilidades:

```
educore-api/
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── database/
│
├── tests/
│
├── docs/
│
├── requirements.txt
├── README.md
└── run.py
```

---

## 🔄 Próximas etapas

* [x] Criar repositório no GitHub
* [x] Configurar ambiente de desenvolvimento
* [ ] Criar estrutura inicial Flask
* [ ] Configurar conexão com MongoDB
* [ ] Criar endpoints da API
* [ ] Implementar validações
* [ ] Criar testes automatizados
* [ ] Documentar API

---

## 🎯 Aprendizado

Este projeto faz parte da minha jornada de aprendizado em desenvolvimento backend, buscando aplicar na prática conceitos de programação, banco de dados, APIs e arquitetura de software.

A ideia é evoluir o projeto gradualmente, documentando cada etapa e aplicando novos conhecimentos adquiridos durante o desenvolvimento.

---

## 👨‍💻 Autor

Fabiano Hipolito

Projeto desenvolvido para estudos e evolução técnica em desenvolvimento de software.

