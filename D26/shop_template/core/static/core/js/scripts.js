document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const toggle = document.getElementById("themeToggle");
    const label = document.getElementById("themeLabel");

    // Load saved theme from localStorage
    let theme = localStorage.getItem("theme") || "light";

    const applyTheme = (theme) => {
        if (theme === "dark") {
            body.classList.add("dark-mode");
            toggle.checked = true;
            label.textContent = "☀️";
        } else {
            body.classList.remove("dark-mode");
            toggle.checked = false;
            label.textContent = "🌙";
        }
    };

    // Apply saved theme on page load
    applyTheme(theme);

    // Listen for toggle changes
    toggle.addEventListener("change", function () {
        if (this.checked) {
            theme = "dark";
        } else {
            theme = "light";
        }
        localStorage.setItem("theme", theme);
        applyTheme(theme);
    });
});
