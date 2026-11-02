
const appShell = document.querySelector(".app-shell");
const menuToggle = document.querySelector(".menu-toggle");
const sidebarBackdrop = document.querySelector(".sidebar-backdrop");

if (appShell && menuToggle && sidebarBackdrop) {
    const closeSidebar = () => {
        appShell.classList.remove("is-sidebar-open");

        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Abrir menu");

        sidebarBackdrop.hidden = true;

        menuToggle.focus();
    };

    menuToggle.addEventListener("click", () => {
        const isOpen = appShell.classList.toggle("is-sidebar-open");

        menuToggle.setAttribute("aria-expanded", String(isOpen));

        menuToggle.setAttribute(
            "aria-label",
            isOpen ? "Fechar menu" : "Abrir menu"
        );

        sidebarBackdrop.hidden = !isOpen;
    });

    sidebarBackdrop.addEventListener("click", closeSidebar);

    document.addEventListener("keydown", (event) => {
        if (
            event.key === "Escape" &&
            appShell.classList.contains("is-sidebar-open")
        ) {
            closeSidebar();
        }
    });

    document.querySelectorAll(".navigation a").forEach((link) => {
        link.addEventListener("click", () => {
            if (appShell.classList.contains("is-sidebar-open")) {
                closeSidebar();
            }
        });
    });
}
