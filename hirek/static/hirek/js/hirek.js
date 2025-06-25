document.querySelectorAll(".hirek_section").forEach((section) => {
  section.addEventListener("click", function () {
    document.querySelectorAll(".hirek_section").forEach((s) => {
      s.classList.remove("active");
    });
    this.classList.add("active");
  });
});
