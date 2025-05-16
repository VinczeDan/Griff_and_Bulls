document.querySelectorAll(".hirek_section").forEach((section) => {
  section.addEventListener("click", function () {
    // Eltávolítjuk az active osztályt minden sectionről
    document.querySelectorAll(".hirek_section").forEach((s) => {
      s.classList.remove("active");
    });
    // Hozzáadjuk a kattintott sectionhoz
    this.classList.add("active");
  });
});
