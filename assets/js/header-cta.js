/* prototipo-header.js — botão "Começar Dia 1 ›" no cabeçalho (só nas páginas do protótipo).
   O cabeçalho é montado por /assets/js/site-nav.js; este script roda depois (defer, na ordem)
   e acrescenta o botão. Texto e link iguais ao botão da home no ar. */
(function () {
  'use strict';
  var HREF = '/08-novo-testamento/mateus/capitulos/capitulo-01.html';
  var LABEL = 'Começar Dia 1 ›';
  function init() {
    var tools = document.querySelector('#site-header .sh-tools');
    var nav = document.querySelector('#site-header .sh-nav');
    if (!tools || document.querySelector('#site-header .sh-cta')) return;
    var a = document.createElement('a');
    a.className = 'sh-cta'; a.href = HREF; a.textContent = LABEL;
    tools.insertBefore(a, tools.firstChild);
    if (nav) {                       // cópia para o menu aberto no celular
      var m = a.cloneNode(true);
      m.className = 'sh-cta sh-cta-menu';
      nav.appendChild(m);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
