const header = document.querySelector("header");
const footer = document.querySelector("footer");

header.innerHTML = `<nav class="navbar navbar-expand-lg navbar-light">
        <div class="container">
            <img class="logo_img" src="{% static "logo.png" %}" alt="eye">
            <a class="navbar-brand">Sistema de monitoreo</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/..">pagina principal</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/servers">servidores</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Monitoreo de salas</a>
                        <ul class="submenu">
                            <li><a href="/sub" class="nav-link">piso -1</a></li>
                            <li><a href="/one" class="nav-link">piso 1</a></li>
                            <li><a href="/two" class="nav-link">piso 2</a></li>
                            <li><a href="/three" class="nav-link">piso 3</a></li>
                            <li><a href="/four" class="nav-link">piso 4</a></li>
                            <li><a href="/five" class="nav-link">piso 5</a></li>
                            <li><a href="/top" class="nav-link">piso 6</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/admin">Admin</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>`;