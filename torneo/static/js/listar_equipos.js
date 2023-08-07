let ciudades = [];

const listarEquipos = async (idJugador) => {
    try {
        const response = await fetch(`./sorteo/${idJugador}`);
        const data = await response.json();

        if (data.message === "Success") {
            equipos = data.equipos;
            let filas = ``;
            equipos.forEach((equipo) => {
                filas += `<tr value='${equipo.id}'> <td>${equipo.id}</td> <td><img src="${equipo.escudo}" height="60" /></td> <td>${equipo.nombre}</td> <td>${equipo.pais}</td> <td>${equipo.estrellas}</td> </tr>`;
            });
            bodyEquipos.innerHTML = filas;

        } else {
            alert("Países no encontrados...");
        }
    } catch (error) {
        console.log(error);
    }
};

const listarJugadores = async () => {
    try {
        const response = await fetch("./sorteo/jugadores");
        const data = await response.json();
        console.log(data);
        if (data.message === "Success") {
            let opciones = ``;
            data.jugadores.forEach((jugador) => {
                opciones += `<option value='${jugador.id}'>${jugador.nombre}</option>`;
            });
            cboPais.innerHTML = opciones;
            listar(data.jugadores[0].id);
        } else {
            alert("Países no encontrados...");
        }
    } catch (error) {
        console.log(error);
    }
};

const cargaInicial = async () => {
    await listarJugadores();
    cboPais.addEventListener("change", (event) => {
        listarEquipos(event.target.value);
    });

    cboCiudad.addEventListener("change", (event) => {
        listarOpciones(event.target.value);
    });
};

window.addEventListener("load", async () => {
    await cargaInicial();
});