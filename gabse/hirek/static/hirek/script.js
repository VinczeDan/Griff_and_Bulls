// Hamburger menü megnyitása/zárása
function toggleMenu() {
  const navLinks = document.querySelector(".nav-links");
  const overlay = document.getElementById("overlay");
  const body = document.body;

  navLinks.classList.toggle("active");
  overlay.classList.toggle("active");

  if (navLinks.classList.contains("active")) {
    body.classList.add("menu-open");
  } else {
    body.classList.remove("menu-open");
  }
}

function toggleDropdown(event) {
  if (window.innerWidth <= 1200) {
    event.preventDefault();
    const dropdown = event.target.closest(".dropdown");
    if (dropdown) {
      const dropdownMenu = dropdown.querySelector(".dropdown-menu");
      dropdownMenu.classList.toggle("active");
    }
  }
}

document.addEventListener("click", function (event) {
  if (!event.target.matches(".dropdown a")) {
    const dropdowns = document.querySelectorAll(".dropdown-menu");
    dropdowns.forEach(function (dropdown) {
      dropdown.classList.remove("active");
    });
  }
});

document.querySelectorAll(".dropdown").forEach(function (dropdown) {
  dropdown.addEventListener("click", function () {
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");
    dropdownMenu.classList.toggle("active");
  });
});

window.addEventListener("scroll", function () {
  const header = document.querySelector("header");
  if (window.scrollY > 50) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});

document.querySelectorAll(".nav-links a").forEach(function (link) {
  link.addEventListener("click", function () {
    const navLinks = document.querySelector(".nav-links");
    const overlay = document.getElementById("overlay");
    const body = document.body;

    navLinks.classList.remove("active");
    overlay.classList.remove("active");
    body.classList.remove("menu-open");
  });
});
document.getElementById("overlay").addEventListener("click", function () {
  const navLinks = document.querySelector(".nav-links");
  const overlay = document.getElementById("overlay");
  const body = document.body;

  navLinks.classList.remove("active");
  overlay.classList.remove("active");
  body.classList.remove("menu-open");
});


document.addEventListener("DOMContentLoaded", function () {
  const checkbox = document.getElementById("checkbox");

  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
    checkbox.checked = true;
  }

  checkbox.addEventListener("change", function () {
    if (this.checked) {
      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  });
}); 