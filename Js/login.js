//busco el input
let email = document.getElementById("email");
let contrasenia = document.getElementById("contrasenia");
//validacion del formulario
function validacionForm() {
  let em = email.value;
  let pass = contrasenia.value;

  if (em === "" || pass === "") {
    alert("Por favor ingrese usuario y/o contraseña");
  } else if (pass.length <= 6) {
    alert("Tiene que tener un minimo de 6 caracteres");
  } else {
    //cambia la ventana
    window.open("/home.html");
  }
}
function cargarDatos() {
  let bienvenido = document.getElementById("bienvenido");
  bienvenido.value = prompt("Ingrese un nombre");
}
