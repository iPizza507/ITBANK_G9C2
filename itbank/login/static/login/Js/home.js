function cargarDatos() {
  let getName = localStorage.getItem("name");
  let welkomeText = document.getElementById("bienvenido");
  welkomeText.innerText = "Bienvenid@ " + getName + "!";
}
