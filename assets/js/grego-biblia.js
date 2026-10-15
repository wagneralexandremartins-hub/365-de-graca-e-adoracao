/* grego-biblia:v1 — botão ocultar/mostrar o grego nos capítulos da Bíblia ACF (scripts/aplicar_grego_biblia.py).
   Sem JS o botão fica escondido e o grego visível. */
(function () {
  var b = document.querySelector('[data-grego-alternar]');
  var v = b && document.getElementById(b.getAttribute('aria-controls'));
  if (!v) return;
  b.hidden = false;
  b.addEventListener('click', function () {
    var oculto = v.classList.toggle('sem-grego');
    b.setAttribute('aria-pressed', oculto ? 'true' : 'false');
    b.textContent = oculto ? b.getAttribute('data-mostrar') : b.getAttribute('data-ocultar');
  });
})();
