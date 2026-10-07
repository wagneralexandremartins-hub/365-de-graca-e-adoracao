/* hub.js — filtro dos hubs AT/NT e destaque do livro em leitura (protótipo) */
(function () {
  'use strict';
  function init() {
    var buttons = document.querySelectorAll('.filter [data-filter]');
    var groups = document.querySelectorAll('.group[data-group]');
    Array.prototype.forEach.call(buttons, function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.getAttribute('data-filter');
        Array.prototype.forEach.call(buttons, function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        Array.prototype.forEach.call(groups, function (g) { g.hidden = f !== 'todos' && g.getAttribute('data-group') !== f; });
      });
    });

    var S = window.Site365;
    if (!S) return;
    var p = S.getProgress();
    // Sem progresso salvo: convida a começar por Mateus 1
    var slug = p ? p.slug : 'mateus';
    var book = document.querySelector('.book[data-book="' + slug + '"]');
    if (book) {
      book.classList.add('is-current');
      book.href = p ? p.url : S.chapterUrl('mateus', 1);
      // Hub com tema por livro: o estado vai na linha de dias; senão, no primeiro <span>
      (book.querySelector('.dias') || book.querySelector('span')).textContent = p ? 'Continuar no cap. ' + p.ch + ' →' : 'Começar no NT →';
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
