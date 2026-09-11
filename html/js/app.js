(function () {
  const STORAGE_KEY = "ufz-progress";
  const THEME_KEY = "ufz-theme";

  function getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    } catch {
      return {};
    }
  }
  function saveProgress(p) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
  }

  function applyTheme() {
    const t = localStorage.getItem(THEME_KEY);
    if (t === "dark" || t === "light") {
      document.documentElement.classList.add("theme-" + t);
    }
  }
  applyTheme();

  window.UFZ = {
    toggleTheme() {
      const html = document.documentElement;
      const dark = html.classList.contains("theme-dark") ||
        (!html.classList.contains("theme-light") &&
          window.matchMedia("(prefers-color-scheme: dark)").matches);
      html.classList.remove("theme-dark", "theme-light");
      if (dark) {
        html.classList.add("theme-light");
        localStorage.setItem(THEME_KEY, "light");
      } else {
        html.classList.add("theme-dark");
        localStorage.setItem(THEME_KEY, "dark");
      }
    },
    markDone(id) {
      const p = getProgress();
      p[id] = true;
      saveProgress(p);
      updateUI();
    },
    isDone(id) {
      return !!getProgress()[id];
    },
    resetProgress() {
      localStorage.removeItem(STORAGE_KEY);
      updateUI();
    },
  };

  function updateUI() {
    const p = getProgress();
    const links = document.querySelectorAll(".nav a[data-id]");
    let done = 0;
    const total = links.length || 17;
    links.forEach((a) => {
      const id = a.getAttribute("data-id");
      if (p[id]) {
        a.classList.add("done");
        done++;
      } else {
        a.classList.remove("done");
      }
    });
    const bar = document.getElementById("progress-bar");
    const label = document.getElementById("progress-label");
    if (bar) bar.style.width = Math.round((done / total) * 100) + "%";
    if (label) label.textContent = done + " of " + total + " lessons completed";

    const markBtn = document.getElementById("mark-done-btn");
    if (markBtn) {
      const lid = markBtn.getAttribute("data-id");
      if (p[lid]) {
        markBtn.textContent = "Completed ✓";
        markBtn.disabled = true;
      }
    }
  }

  // Search
  const search = document.getElementById("lesson-search");
  if (search) {
    search.addEventListener("input", () => {
      const q = search.value.trim().toLowerCase();
      document.querySelectorAll(".nav a[data-id]").forEach((a) => {
        const text = a.textContent.toLowerCase();
        a.classList.toggle("hidden", q && !text.includes(q));
      });
    });
  }

  // Mobile menu
  const toggle = document.getElementById("menu-toggle");
  const sidebar = document.querySelector(".sidebar");
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => sidebar.classList.toggle("open"));
  }

  document.addEventListener("DOMContentLoaded", updateUI);
  updateUI();
})();
