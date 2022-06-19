//busco el inputlet
let email = document.getElementById("email");
let contrasenia = document.getElementById("password");
let nombre = document.getElementById("name");
//validacion del formulario
function validacionForm() {
  let em = email.value;
  let pass = contrasenia.value;
  let name = nombre.value;

  if (em === "" || pass === "" || name === "") {
    alert("Por favor ingrese nombre, usuario y/o contraseña");
  } else if (pass.length <= 6) {
    alert("La contraseña debe tener un minimo de 6 caracteres");
  } else if (name.length <= 4) {
    alert("El nombre debe tener un minimo de 4 caracteres");
  } else {
    //cambia la ventana
    localStorage.setItem("name", name);
    alert("Load..");
    setTimeout(function () {
      location.href = "/Components/Home/HomeCuentas.html";
    }, 100);
  }
}
