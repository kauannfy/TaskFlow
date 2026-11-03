
const appShell = document.querySelector(".app-shell");
const menuToggle = document.querySelector(".menu-toggle");
const sidebarBackdrop = document.querySelector(".sidebar-backdrop");
const sidebar = document.querySelector(".sidebar");
const mobileNavigation = window.matchMedia("(max-width: 760px)");

if (appShell && menuToggle && sidebarBackdrop && sidebar) {
    const setSidebarOpen = (isOpen, restoreFocus = false) => {
        appShell.classList.toggle("is-sidebar-open", isOpen);

        menuToggle.setAttribute("aria-expanded", String(isOpen));
        menuToggle.setAttribute(
            "aria-label",
            isOpen ? "Fechar menu" : "Abrir menu"
        );

        sidebarBackdrop.hidden = !isOpen;
        sidebar.inert = mobileNavigation.matches && !isOpen;

        if (restoreFocus) {
            menuToggle.focus();
        } else if (isOpen && mobileNavigation.matches) {
            sidebar.querySelector(".navigation a[href]")?.focus();
        }
    };

    setSidebarOpen(false);

    menuToggle.addEventListener("click", () => {
        const isOpen = !appShell.classList.contains("is-sidebar-open");
        setSidebarOpen(isOpen);
    });

    sidebarBackdrop.addEventListener("click", () => {
        setSidebarOpen(false, true);
    });

    document.addEventListener("keydown", (event) => {
        if (
            event.key === "Escape" &&
            appShell.classList.contains("is-sidebar-open")
        ) {
            setSidebarOpen(false, true);
        }
    });

    sidebar.querySelectorAll("a[href]").forEach((link) => {
        link.addEventListener("click", () => {
            if (appShell.classList.contains("is-sidebar-open")) {
                setSidebarOpen(false, true);
            }
        });
    });

    mobileNavigation.addEventListener("change", (event) => {
        if (!event.matches) {
            setSidebarOpen(false);
            return;
        }

        sidebar.inert = !appShell.classList.contains("is-sidebar-open");
    });
}
