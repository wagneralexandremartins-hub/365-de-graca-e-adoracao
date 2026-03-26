# 📚 Guia Completo - Projeto 365 de Graça & Adoração

## 🎯 Visão Geral do Projeto

O **365 de Graça & Adoração** é um site de estudos bíblicos estruturado em **12 blocos temáticos**, cobrindo toda a história bíblica desde a criação até o apocalipse.

---

## 📂 Estrutura de Pastas do Projeto

```
365-de-graca-e-adoracao/
│
├── index.html                    # Página inicial com os 12 blocos
├── vercel.json                   # Configuração do Vercel
├── convert_md_to_html.py         # Script para converter Markdown → HTML
│
├── assets/                       # Arquivos estáticos
│   ├── css/
│   │   └── style.css            # Estilos do site
│   ├── js/
│   │   └── script.js            # JavaScript do site
│   └── img/                     # Imagens
│
├── 01-principio/                # Bloco 1: O Princípio de Tudo
│   └── index.html
│
├── 02-pentateuco/               # Bloco 2: Pentateuco
│   ├── index.html               # Hub do Pentateuco
│   ├── genesis/
│   │   ├── index.html           # Hub do Gênesis
│   │   └── estudos/             # Estudos do Gênesis
│   │       ├── 01_Criacao.html
│   │       ├── 02_Genesis_1_1_2.html
│   │       └── ...
│   ├── exodo/
│   ├── levitico/
│   ├── numeros/
│   └── deuteronomio/
│
├── 03-historicos/               # Bloco 3: Livros Históricos
├── 04-poeticos/                 # Bloco 4: Livros Poéticos
├── 05-profetas/                 # Bloco 5: Profetas
├── 06-apocrifos/                # Bloco 6: Apócrifos
├── 07-novo-testamento/          # Bloco 7: Novo Testamento
├── 08-igreja-primitiva/         # Bloco 8: Igreja Primitiva
├── 09-concilios/                # Bloco 9: Concílios
├── 10-cruzadas/                 # Bloco 10: Cruzadas
├── 11-conflitos/                # Bloco 11: Conflitos Contemporâneos
└── 12-apocalipse/               # Bloco 12: Apocalipse
```

---

## 🛠️ O que Fizemos Até Agora

### ✅ **1. Criamos a Estrutura Base**
- Organizamos as pastas por blocos temáticos
- Criamos a página inicial com os 12 blocos
- Configuramos o Vercel para deploy automático

### ✅ **2. Desenvolvemos o Bloco 2 - Pentateuco**
- Página hub do Pentateuco (`02-pentateuco/index.html`)
- Página hub do Gênesis (`02-pentateuco/genesis/index.html`)
- Convertemos seus estudos de Markdown para HTML
- Organizamos os estudos por capítulo (Gênesis 1-5)

### ✅ **3. Criamos um Script de Conversão**
- Script Python que converte arquivos `.md` em páginas HTML
- Aplica automaticamente o design do site
- Facilita adicionar novos estudos

### ✅ **4. Configuramos Git e Vercel**
- Repositório GitHub conectado
- Deploy automático no Vercel
- Cada push atualiza o site automaticamente

---

## 🚀 Como Adicionar Novos Estudos

### **Método 1: Usando Markdown (Recomendado)**

1. **Escreva seu estudo em Markdown** (`.md`)
   ```markdown
   # Gênesis 6:1-4 - Os Filhos de Deus
   
   ## Introdução
   Este texto apresenta um dos trechos mais enigmáticos...
   
   ## Análise Versículo por Versículo
   
   ### Versículo 1
   **"E aconteceu que..."**
   
   - Ponto 1
   - Ponto 2
   ```

2. **Salve o arquivo** na pasta correta:
   ```
   02-pentateuco/genesis/estudos/16_Genesis_6_1_4.md
   ```

3. **Execute o script de conversão**:
   ```bash
   cd 365-de-graca-e-adoracao
   python3 convert_md_to_html.py
   ```

4. **Faça commit e push**:
   ```bash
   git add .
   git commit -m "Adicionar estudo Gênesis 6:1-4"
   git push origin main
   ```

### **Método 2: Criando HTML Diretamente**

Se preferir criar o HTML manualmente, use este template:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seu Título - 365 de Graça & Adoração</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <header>
        <nav>
            <a href="/" class="logo">365 de Graça & Adoração</a>
            <div class="nav-links">
                <a href="/02-pentateuco/genesis/index.html">← Voltar ao Gênesis</a>
                <a href="/">Início</a>
            </div>
        </nav>
    </header>

    <main class="study-content">
        <h1>Seu Título Aqui</h1>
        
        <h2>Introdução</h2>
        <p>Seu conteúdo aqui...</p>
        
        <div class="navigation">
            <a href="/02-pentateuco/genesis/index.html">← Voltar aos Estudos</a>
            <a href="/">Início</a>
        </div>
    </main>

    <footer>
        <p>&copy; 2025 365 de Graça & Adoração. Todos os direitos reservados.</p>
    </footer>

    <script src="/assets/js/script.js"></script>
</body>
</html>
```

---

## 💻 Workflow Completo no VS Code

### **1. Clonar o Repositório (Primeira Vez)**

```bash
# Opção 1: Via terminal
git clone https://github.com/wagneralexandremartins-hub/365-de-graca-e-adoracao.git
cd 365-de-graca-e-adoracao
code .

# Opção 2: No VS Code
# Ctrl+Shift+P → Git: Clone → Cole o link do repositório
```

### **2. Antes de Começar a Trabalhar (SEMPRE)**

```bash
# Atualiza com as mudanças mais recentes
git pull origin main
```

### **3. Fazer Alterações**

- Edite arquivos no VS Code
- Crie novos arquivos
- Adicione imagens em `assets/img/`

### **4. Visualizar Localmente (Opcional)**

```bash
# Instalar servidor local
npm install -g http-server

# Rodar servidor
http-server -p 8000

# Abrir no navegador: http://localhost:8000
```

### **5. Salvar Alterações no Git**

```bash
# Ver o que mudou
git status

# Adicionar todos os arquivos modificados
git add .

# Ou adicionar arquivos específicos
git add 02-pentateuco/genesis/estudos/novo-estudo.html

# Fazer commit com mensagem descritiva
git commit -m "Adicionar estudo sobre Gênesis 6"

# Enviar para o GitHub
git push origin main
```

### **6. Aguardar Deploy Automático**

- O Vercel detecta o push automaticamente
- Faz o build e deploy em 1-3 minutos
- Acesse: https://365-de-graca-e-adoracao.vercel.app/

---

## 🎨 Personalizando o Design

### **Cores do Tema**

Edite `assets/css/style.css`:

```css
:root {
    --primary-color: #e50914;      /* Vermelho principal */
    --bg-dark: #141414;            /* Fundo escuro */
    --bg-card: #1f1f1f;            /* Fundo dos cards */
    --text-light: #ffffff;         /* Texto claro */
    --text-gray: #b3b3b3;          /* Texto secundário */
}
```

### **Adicionar Novas Seções**

No `index.html`, adicione novos cards:

```html
<div class="block-card">
    <span class="block-number">13</span>
    <h3>Novo Bloco</h3>
    <p>Descrição do novo bloco...</p>
    <a href="/13-novo-bloco/index.html" class="btn">Explorar →</a>
</div>
```

---

## 📝 Dicas de Markdown

### **Formatação Básica**

```markdown
# Título Principal (H1)
## Subtítulo (H2)
### Seção (H3)

**Texto em negrito**
*Texto em itálico*

> Citação ou versículo bíblico

- Lista não ordenada
- Item 2
- Item 3

1. Lista ordenada
2. Item 2
3. Item 3

[Link](https://exemplo.com)
```

### **Exemplo de Estudo em Markdown**

```markdown
# Gênesis 1:1 - No Princípio

## Contexto Histórico

Este versículo abre não apenas o livro de Gênesis, mas toda a Bíblia...

## Análise do Texto

### "No princípio"

> "No princípio criou Deus os céus e a terra." (Gênesis 1:1)

A palavra hebraica **bereshit** (בְּרֵאשִׁית) significa...

### "Criou Deus"

O verbo **bara** (בָּרָא) é usado exclusivamente para...

## Aplicação Prática

1. **Reconhecer a soberania de Deus**
2. **Confiar no propósito divino**
3. **Adorar o Criador**

## Reflexão

Como este versículo transforma nossa visão de mundo?

---

**Próximo estudo:** [Gênesis 1:2](/02-pentateuco/genesis/estudos/02_Genesis_1_2.html)
```

---

## 🔧 Comandos Git Úteis

```bash
# Ver histórico de commits
git log --oneline

# Desfazer mudanças não commitadas
git checkout -- nome-do-arquivo.html

# Criar uma branch para testar
git checkout -b teste-nova-feature

# Voltar para a branch principal
git checkout main

# Ver diferenças antes de commitar
git diff

# Adicionar apenas parte de um arquivo
git add -p arquivo.html
```

---

## 🚨 Resolução de Problemas

### **Problema: Vercel não atualiza**

```bash
# Limpar cache do navegador: Ctrl+Shift+R

# Verificar status do deployment:
# https://vercel.com/dashboard

# Forçar novo deploy:
git commit --allow-empty -m "Forçar redeploy"
git push origin main
```

### **Problema: Conflito no Git**

```bash
# Atualizar antes de fazer push
git pull origin main

# Se houver conflito, resolver manualmente no VS Code
# Depois:
git add .
git commit -m "Resolver conflito"
git push origin main
```

### **Problema: Arquivo não aparece no site**

1. Verifique se o caminho está correto (use `/` no início)
2. Verifique se fez commit e push
3. Aguarde o deploy do Vercel (1-3 minutos)
4. Limpe o cache do navegador

---

## 📊 Próximos Passos Sugeridos

### **Curto Prazo**
- [ ] Completar estudos de Gênesis 6-50
- [ ] Adicionar estudos de Êxodo
- [ ] Criar linha do tempo interativa
- [ ] Adicionar imagens ilustrativas

### **Médio Prazo**
- [ ] Desenvolver os 12 blocos temáticos
- [ ] Criar sistema de busca
- [ ] Adicionar comentários/notas
- [ ] Implementar modo de leitura

### **Longo Prazo**
- [ ] App mobile (PWA)
- [ ] Sistema de progresso do usuário
- [ ] Planos de leitura personalizados
- [ ] Comunidade de estudos

---

## 🎓 Recursos para Aprender Mais

### **HTML & CSS**
- [MDN Web Docs](https://developer.mozilla.org/pt-BR/)
- [W3Schools](https://www.w3schools.com/)

### **Git & GitHub**
- [Git - Guia Prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html)
- [GitHub Docs](https://docs.github.com/pt)

### **Markdown**
- [Markdown Guide](https://www.markdownguide.org/)

### **Vercel**
- [Vercel Documentation](https://vercel.com/docs)

---

## 💡 Boas Práticas

### **Commits**
✅ Mensagens claras e descritivas  
✅ Commits pequenos e frequentes  
✅ Testar antes de commitar  

❌ Commits gigantes com muitas mudanças  
❌ Mensagens vagas como "update" ou "fix"  

### **Organização**
✅ Um arquivo por estudo  
✅ Nomes de arquivo descritivos  
✅ Estrutura de pastas consistente  

❌ Arquivos com nomes genéricos  
❌ Tudo na mesma pasta  

### **Conteúdo**
✅ Revisão ortográfica  
✅ Referências bíblicas corretas  
✅ Formatação consistente  

---

## 📞 Precisa de Ajuda?

Se tiver dúvidas ou problemas:

1. **Consulte este guia** primeiro
2. **Pesquise no Google** o erro específico
3. **Verifique a documentação** do Git/Vercel
4. **Peça ajuda** em fóruns ou comunidades

---

## 🎉 Parabéns!

Você agora tem todo o conhecimento necessário para desenvolver o **Projeto 365 de Graça & Adoração** de forma independente!

Continue aprendendo, praticando e construindo este projeto incrível! 🚀

---

**Última atualização:** 16 de fevereiro de 2025  
**Versão do guia:** 1.0
