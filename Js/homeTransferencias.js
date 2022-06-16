//Esconder o mostrar Comprobantes
let listasComprobantes = document.getElementById("listasComprobantes");
function mostrar() {
  if (listasComprobantes.style.display != "none") {
    listasComprobantes.style.display = "none";
  } else {
    listasComprobantes.style.display = "block";
  }
}

//AÑADOR O ELIMINAR CONTACTOS
//obtener los elementos del DOM
let lista = document.getElementById("listaContato"),
  contactoInput = document.getElementById("contactoInput");
//cuando hacen click, activa la funcion:
const agregarContacto = function () {
  //crea las etiquetas
  let contacto = contactoInput.value,
    nuevaTarea = document.createElement("li"),
    enlace = document.createElement("a"),
    contenido = document.createTextNode(contacto),
    img = document.createElement("img");
  //si el input no tiene nigun dato, mostrar el msj
  if (contacto === "") {
    contactoInput.setAttribute("placeholder", "Agregar una tarea valida");
    return false;
  }

  //añade contenido a etitqueta A
  enlace.appendChild(contenido);
  // le agrega el atributo href
  enlace.setAttribute("href", "#");
  //le agrega el atributo src y class
  img.setAttribute("src", "/imagen/logo-header.jpeg");
  img.setAttribute("class", "imagen-contacto");
  // le añade el ancla al li
  nuevaTarea.appendChild(img);
  nuevaTarea.appendChild(enlace);
  //añade el li al ul
  lista.appendChild(nuevaTarea);
  contactoInput.value = "";

  for (let i = 0; i <= lista.children.length - 1; i++) {
    lista.children[i].addEventListener("click", function () {
      this.parentNode.removeChild(this);
    });
  }

  let comprobarInput = function () {
    contactoInput.className = "";
    contactoInput.setAttribute("placeholder", "Agregar contacto");
  };
  let eliminarTarea = function () {
    this.parentNode.removeChild(this);
  };

  contactoInput.addEventListener("click", comprobarInput);

  for (let i = 0; i < lista.length - 1; i++) {
    lista.children[i].addEventListener("click", eliminarTarea);
  }
};
