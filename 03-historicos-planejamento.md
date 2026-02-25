# Planejamento: Introdução aos Livros Históricos

## 1. Análise da Estrutura Existente

O projeto `365-de-graca-e-adoracao` segue um padrão claro:

- **Estrutura de Blocos:** O conteúdo é dividido em blocos temáticos (ex: `02-pentateuco`). O próximo será `03-historicos`.
- **Páginas de Hub:** Cada bloco e cada livro possui uma página `index.html` que serve como um hub, apresentando o conteúdo daquela seção (livros, capítulos, blocos temáticos).
- **Estilo Consistente:** Todas as páginas utilizam o mesmo arquivo CSS (`/assets/css/style.css`), garantindo uma identidade visual coesa.
- **Conteúdo Detalhado:** Os estudos são divididos por capítulos e, dentro deles, versículo por versículo, além de blocos temáticos que agrupam capítulos.

## 2. Estrutura a ser Criada para os Livros Históricos

Para manter a consistência, a seguinte estrutura de arquivos e pastas será criada:

1.  **Pasta Principal do Bloco:**
    - `/03-historicos/`

2.  **Página Hub do Bloco:**
    - `/03-historicos/index.html`: Esta página apresentará os Livros Históricos, similar à página do Pentateuco.

3.  **Subpastas para Cada Livro Histórico:**
    - `/03-historicos/josue/`
    - `/03-historicos/juizes/`
    - `/03-historicos/rute/`
    - `/03-historicos/1samuel/`
    - `/03-historicos/2samuel/`
    - `/03-historicos/1reis/`
    - `/03-historicos/2reis/`
    - `/03-historicos/1cronicas/`
    - `/03-historicos/2cronicas/`
    - `/03-historicos/esdras/`
    - `/03-historicos/neemias/`
    - `/03-historicos/ester/`

4.  **Páginas Hub para Cada Livro:**
    - Dentro de cada subpasta de livro, um `index.html` será criado (ex: `/03-historicos/josue/index.html`). Inicialmente, eles servirão como placeholders, prontos para receber a lista de capítulos e blocos temáticos.

## 3. Conteúdo da Introdução

A página `03-historicos/index.html` será a introdução geral. Ela conterá:

- **Título:** Livros Históricos.
- **Descrição:** Uma explicação sobre o período que esses livros cobrem (da conquista de Canaã ao exílio e retorno).
- **Citação Relevante:** Um versículo que capture a essência do período.
- **Lista de Livros:** Cards para cada um dos 12 livros históricos, com uma breve descrição e um link para a respectiva página de hub.
- **Navegação:** Links para o bloco anterior (Pentateuco) e o próximo (Livros Poéticos).

## 4. Próximos Passos

- **Executar a criação** das pastas e arquivos descritos acima.
- **Popular o conteúdo** da página `03-historicos/index.html` usando o template do `02-pentateuco/index.html`.
- **Criar as páginas hub** para cada livro histórico como placeholders.
- **Atualizar o `index.html` principal** para que o link para os Livros Históricos funcione.
- **Apresentar a estrutura** ao usuário para validação antes de prosseguir com o conteúdo detalhado de cada livro.
