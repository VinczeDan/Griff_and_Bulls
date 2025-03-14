// Hamburger menü megnyitása/zárása
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    const hamburger = document.querySelector('.hamburger');
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active');
}

// Legördülő menü megnyitása/zárása
function toggleDropdown(event) {
    if (window.innerWidth <= 1200) { // Csak mobil esetén
        event.preventDefault();
        const dropdown = event.target.closest('.dropdown');
        if (dropdown) {
            const dropdownMenu = dropdown.querySelector('.dropdown-menu');
            dropdownMenu.classList.toggle('active');
        }
    }
}

// Kattintás esemény kezelése a dokumentumon
document.addEventListener('click', function (event) {
    if (!event.target.matches('.dropdown a')) {
        const dropdowns = document.querySelectorAll('.dropdown-menu');
        dropdowns.forEach(function (dropdown) {
            dropdown.classList.remove('active');
        });
    }
});

// Legördülő menü ikonokhoz eseményfigyelő hozzáadása
document.querySelectorAll('.dropdown').forEach(function(dropdown) {
    dropdown.addEventListener('click', function() {
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        dropdownMenu.classList.toggle('active');
    });
});

window.addEventListener("scroll", function() {
    const header = document.querySelector("header");
    if (window.scrollY > 50) { // Adjust the scroll threshold as needed
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});






