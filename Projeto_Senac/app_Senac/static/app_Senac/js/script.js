// app_Senac/static/app_Senac/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    
    // --- Lógica da NavBar Lateral ---
    const menuToggle = document.getElementById('menu-toggle');
    const sidebarNav = document.getElementById('sidebar-nav');
    const closeMenuBtn = document.getElementById('close-menu-btn');

    if (menuToggle && sidebarNav && closeMenuBtn) {
        console.log("Elementos do menu principal (toggle, sidebar, closeBtn) encontrados."); // Log de depuração

        menuToggle.addEventListener('click', function(event) {
            event.stopPropagation(); // Impede que o clique se propague para o document
            sidebarNav.classList.add('open');
            console.log("Menu toggle clicado, sidebar DEVE abrir. Classe 'open' adicionada."); // Log de depuração
        });

        closeMenuBtn.addEventListener('click', function(event) {
            event.stopPropagation();
            sidebarNav.classList.remove('open');
            console.log("Botão de fechar clicado, sidebar DEVE fechar. Classe 'open' removida."); // Log de depuração
        });

        // Fechar a navbar ao clicar fora dela (no restante do documento)
        document.addEventListener('click', function(event) {
            // Verifica se a navbar está aberta E o clique NÃO foi dentro da navbar E NÃO foi no botão de toggle
            if (sidebarNav.classList.contains('open') && 
                !sidebarNav.contains(event.target) && 
                event.target !== menuToggle) { // Garante que clicar no toggle não feche imediatamente
                sidebarNav.classList.remove('open');
                console.log("Clique fora da sidebar (e não no toggle), sidebar DEVE fechar."); // Log de depuração
            }
        });

        // Impede que cliques dentro da sidebar a fechem (necessário por causa do listener no document)
        sidebarNav.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    } else {
        // Log de erro se algum elemento essencial do menu não for encontrado
        if (!menuToggle) console.error("Erro JS: Elemento #menu-toggle não encontrado.");
        if (!sidebarNav) console.error("Erro JS: Elemento #sidebar-nav não encontrado.");
        if (!closeMenuBtn) console.error("Erro JS: Elemento #close-menu-btn não encontrado.");
    }

    // --- Lógica para Fechar Alertas (do messages framework do Django) ---
    const alertCloseButtons = document.querySelectorAll('.close-alert-btn');
    if (alertCloseButtons.length > 0) {
        console.log("Botões de fechar alerta encontrados:", alertCloseButtons.length); // Log de depuração
    }
    alertCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.display = 'none';
        });
    });

    // --- Lógica para Adicionar Classe 'active' ao Link da NavBar Atual ---
    const navLinks = document.querySelectorAll('#sidebar-nav ul li a');
    const currentPath = window.location.pathname;

    if (navLinks.length > 0) {
        console.log("Links de navegação para 'active' state encontrados:", navLinks.length); // Log de depuração
    }
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        
        // Tratamento para o link da home ser exato e outros links baseados em 'startsWith'
        if (linkPath === '/' && currentPath === '/') {
            link.parentElement.classList.add('active');
        } else if (linkPath !== '/' && linkPath.length > 1 && currentPath.startsWith(linkPath)) {
            link.parentElement.classList.add('active');
        }
    });

});