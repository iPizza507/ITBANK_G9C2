//busco el inputlet
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
    let name = nombre.value;
    localStorage.setItem("name", name);
    alert("Load..");
    setTimeout(function () {
      location.href = "../Components/HomeCuentas.html";
    }, 100);
  }
}
