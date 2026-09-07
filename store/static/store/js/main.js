(function () {
  function getCart() {
    try {
      return JSON.parse(localStorage.getItem("cart") || "[]");
    } catch (e) {
      return [];
    }
  }

  function setCart(items) {
    localStorage.setItem("cart", JSON.stringify(items));
  }

  function updateBadge() {
    var items = getCart();
    var count = items.reduce(function (sum, it) {
      return sum + (it.quantity || 1);
    }, 0);
    var badge = document.getElementById("cart-count");
    if (!badge) return;
    if (count > 0) {
      badge.style.display = "inline-flex";
      badge.textContent = String(count);
    } else {
      badge.style.display = "none";
    }
  }

  function addItem(item) {
    var items = getCart();
    var existing = items.find(function (it) {
      return it.id === item.id && it.size === item.size;
    });
    if (existing) {
      existing.quantity = (existing.quantity || 1) + (item.quantity || 1);
    } else {
      items.push(item);
    }
    setCart(items);
    updateBadge();
  }

  function setupMenu() {
    var toggle = document.getElementById("menu-toggle");
    var drawer = document.getElementById("nav-drawer");
    if (!toggle || !drawer) return;
    toggle.addEventListener("click", function () {
      var open = drawer.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    updateBadge();
    setupMenu();
  });

  window.PageStore = {
    getCart: getCart,
    setCart: setCart,
    updateBadge: updateBadge,
    addItem: addItem,
  };
})();
