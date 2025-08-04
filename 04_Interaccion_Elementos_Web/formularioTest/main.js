let usuarios = [];

document.getElementById("userForm").addEventListener("submit", function (e) {
    e.preventDefault();
    mostrarNombreCompleto();
});

function mostrarNombreCompleto() {
    const nombre = document.getElementById("nombre").value.trim();
    const apellido = document.getElementById("apellido").value.trim();
    const activo = document.getElementById("activo").checked;
    const genero = document.getElementById("genero").value;
    const edad = document.querySelector(".edad").value.trim();

    const nombreCompleto = `${nombre} ${apellido}`;
    const estado = activo ? 'Activo' : 'Inactivo';

    alert("Nombre completo: " + nombreCompleto);

    usuarios.push({
        nombre: nombreCompleto,
        edad: edad,
        estado: estado,
        genero: genero
    });

    renderizarUsuarios();
    document.getElementById("nombre").value="";
    document.getElementById("apellido").value="";
    document.getElementById("activo").checked = false;
    document.getElementById("genero").value="";
    document.querySelector(".edad").value="";

}

function renderizarUsuarios() {
    const contenedor = document.getElementById("listaUsuarios");
    contenedor.innerHTML = "";

    usuarios.forEach((usuario,index) => {
        const div = document.createElement("div");
        div.innerHTML = `
            <label id="lblnombre_${index}"><strong>Nombre:</strong> ${usuario.nombre} </label>
            <label id="lbledad_${index}"><strong>Edad:</strong> ${usuario.edad} </label>
            <label id="lblestado_${index}"><strong>Estado:</strong> ${usuario.estado} </label>
            <label id="lblgenero_${index}"><strong>Género:</strong> ${usuario.genero} </label>
            <hr>
        `;
        contenedor.appendChild(div);
    });
}
