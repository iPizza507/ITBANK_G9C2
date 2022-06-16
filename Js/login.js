console.log("entro al js");
//busco el input
let email = document.getElementById("email");
let contrasenia = document.getElementById("contrasenia");
let nombre = document.getElementById("name");
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
    window.location.href = "../Components/HomeCuentas.html";
    //window.open("../Components/HomeCuentas.html");
  }

  let name = nombre.value;
  localStorage.setItem("name", name);
}

function cargarDatos() {
  let getName = localStorage.getItem("name");
  let welkomeText = document.getElementById("bienvenido");
  welkomeText.innerText = "Bienvenid@ " + getName + "!";
}
