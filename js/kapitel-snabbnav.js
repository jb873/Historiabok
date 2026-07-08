// kapitel-snabbnav.js — visar sticky snabbnav efter scroll förbi hero.
// DELAD-BAS-kandidat: används av kapitel-startsidor med lång layout.
(function () {
  var hero = document.querySelector(".hero-banner");
  var nav  = document.getElementById("snabbnav");
  if (!hero || !nav) return;
  function upd() {
    if (window.scrollY > (hero.offsetHeight - 8)) nav.classList.add("synlig");
    else nav.classList.remove("synlig");
  }
  window.addEventListener("scroll", function () { requestAnimationFrame(upd); }, { passive: true });
  upd();
})();
