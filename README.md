# notas-suap-bot


Este documento descreve o processo de instalação das dependências necessárias para um projeto que utiliza Selenium, Pandas, OpenPyXL e WebDriver Manager.

## Requisitos

Certifique-se de ter o Python instalado no sistema. Para verificar a versão instalada, utilize:

```sh
python --version
```

Caso o comando acima não funcione, tente:

```sh
python3 --version
```

Se o Python não estiver instalado, baixe e instale a versão mais recente em [python.org](https://www.python.org/downloads/).

## Instalação das Dependências

Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal ou prompt de comando:

```sh
pip install selenium pandas openpyxl webdriver-manager
```


## Criação do Arquivo de Acesso

É necessário criar manualmente um arquivo `.env` dentro da pasta do projeto, contendo as credenciais de acesso:

```
username=seu login
password=sua senha
```

Esse arquivo será utilizado para armazenar informações sensíveis de forma segura.

## Automação do Preenchimento de Notas no SUAP

Este projeto inclui um bot para automatizar o preenchimento das notas no sistema SUAP. As notas devem estar no formato de tabela do Excel com a seguinte estrutura:

| Nome      | Nota 1 | Nota 2 | Nota 3 |
|-----------|--------|--------|--------|
| Aluno 1   | 7,5    | 6,5    | 8      |
| Aluno 2   | 8      | 7,5    | 7      |
| Aluno 3   | 6      | 8      | 6,5    |
| Aluno 4   | 9      | 10     | 9,5    |
| Aluno 5   | 7      | 6      | 7,5    |


O bot utilizará as bibliotecas instaladas para processar e enviar esses dados automaticamente para o sistema.

## Referências
- [Documentação do Selenium](https://www.selenium.dev/documentation/)
- [Documentação do Pandas](https://pandas.pydata.org/docs/)
- [Documentação do OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
- [Documentação do WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## Contato

**Autor:** Rafael Tosta  
**Email:** [rafa.ecomp@gmail.com](mailto:rafa.ecomp@gmail.com)

