(function(){
  function getCart(){
    try { return JSON.parse(localStorage.getItem('cart')||'[]'); } catch(e){ return []; }
  }
  function setCart(items){ localStorage.setItem('cart', JSON.stringify(items)); }
  function updateBadge(){
    var items = getCart();
    var count = items.reduce(function(sum, it){ return sum + (it.quantity||1); }, 0);
    var badge = document.getElementById('cart-count');
    if (!badge) return;
    if (count > 0) { badge.style.display = 'inline-flex'; badge.textContent = String(count); }
    else { badge.style.display = 'none'; }
  }
  document.addEventListener('DOMContentLoaded', updateBadge);
  window.PageStore = { getCart: getCart, setCart: setCart, updateBadge: updateBadge };
})();
