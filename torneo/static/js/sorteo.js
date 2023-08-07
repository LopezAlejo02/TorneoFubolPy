let registros = [];
let indiceActual = 0;
async function hacerPeticion(url, method, body) {
    let headers = {
        'Content-Type': 'sorteo/json',
        'X-CSRFToken': csrfToken,
    }

    let response = await fetch( url, {
        method: method,
        headers: headers,
        body: body
    })

    return await response.json()
}
const consultarEquipos = async (idJugador) => {
    try {
        const response = await fetch(`./sorteo/exclude/${idJugador}`);
        const data = await response.json();
        const nombre_equipo = document.getElementById(`nombre_eq_jug_${idJugador}`);
        const escudo_equipo = document.getElementById(`escudo_eq_jug_${idJugador}`);
        const equipos = data.equipos;
        numeroSorteo = Math.round(Math.random() * equipos.length) + 1;
        registros.forEach(registro => {
            if(registro.id_equipo == equipos[numeroSorteo].id){
                numeroSorteo = Math.round(Math.random() * equipos.length) + 1;
            }
        });
        registros.push({'id_jugador':idJugador,'id_equipo': equipos[numeroSorteo].id});
        animacionCarga = setInterval(()=>{
            if (indiceActual < equipos.length) {
                nombre_equipo.textContent = equipos[indiceActual].nombre;
                escudo_equipo.src = equipos[indiceActual].escudo;
                indiceActual++;
            } else {
                indiceActual = 0;
            }
        } ,80)
        setTimeout(() => {
            clearInterval(animacionCarga); // Detiene el intervalo
            nombre_equipo.textContent = (equipos[numeroSorteo].nombre); // Cambia el texto después de detener la animación
            escudo_equipo.src = (equipos[numeroSorteo].escudo);
            //console.log(equipos);
            //console.log('finito');
        }, 4000);
    } catch (error) {
        console.log(error)
    }
};

function post_cruce(data) {
    fetch("sorteo/post", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'sorteo/json',
            'X-CSRFToken': csrfToken,
        },
    })
}

function enviarCruces() {
    registros.forEach(registro => {
        hacerPeticion('sorteo/post',"POST",JSON.stringify(registro)); 
    });
}
