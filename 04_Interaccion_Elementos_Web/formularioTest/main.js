
let usuarios=[]

function mostrarNombreCompleto() {
    const nombre = document.getElementById("nombre").value.trim();
    const apellido = document.getElementById("apellido").value.trim();
    const activo = document.getElementById("activo").checked;
    const genero = document.getElementById("genero").value;
    const edad = document.querySelector(".edad").value.trim();
    const nombreCompleto = `${nombre} ${apellido} ${activo ? 'Activo' : 'Inactivo'} ${edad} ${genero}`;
    alert("Nombre completo: " + nombreCompleto);
    usuarios.push({
        nombre:nombreCompleto,
        edad:edad,
        estado: activo ? "Activo" : "Inactivo",
        genero:genero
    })
    renderizarUsuarios();
}

function renderizarUsuarios() {
    const contenedor = document.getElementById("listaUsuarios");
    contenedor.innerHTML = "";

    usuarios.forEach(usuario => {
        const div = document.createElement("div");
        div.innerHTML = `
            <label id="lblnombre"><strong>Nombre:</strong> ${usuario.nombre} </label>
            <label id="lbledad"><strong>Edad:</strong> ${usuario.edad} </label>
            <label id="lblestado"><strong>Estado:</strong> ${usuario.estado} </label>
            <label id="lblgenero"><strong>Género:</strong> ${usuario.genero} </label>
            <hr>
        `;
        contenedor.appendChild(div);
    });
}