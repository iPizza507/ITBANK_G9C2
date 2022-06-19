//obtener el elemento PADRE
let div = document.getElementById("inversionesSection");

//obtener los datos a partir de fetch
fetch("https:dolarsi.com/api/api.php?type=valoresprincipales")
  .then((data) => data.json())
  .then((data) =>
    //recorrer los datos, añadiendolos en HTML
    data.forEach((e) => {
      //div col
      let div2 = document.createElement("div");
      div2.setAttribute("class", "col");
      div.appendChild(div2);
      //div estructura
      let div3 = document.createElement("div");
      div2.appendChild(div3);
      div3.setAttribute("class", "p-3 mx-auto text-center");
      //div estructura2
      let div4 = document.createElement("div");
      div3.appendChild(div4);
      div4.setAttribute("class", "card mb-4 rounded-3 shadow-sm");
      //div header
      let div5 = document.createElement("div");
      div4.appendChild(div5);
      div5.setAttribute("class", "card-header py-3");
      //h4 dentro del HEADER
      let h4 = document.createElement("h4");
      h4.setAttribute("class", "my-0 fw-normal");
      h4.innerText = `${e.casa.nombre}`;
      div5.appendChild(h4);
      //div body
      let div5A = document.createElement("div");
      div4.appendChild(div5A);
      div5A.setAttribute("class", "card-body");
      //titulo del h1
      let h1 = document.createElement("h3");
      h1.innerText = `Compra: $${e.casa.compra} - Venta: $${e.casa.venta}`;
      div5A.appendChild(h1);
      //Button
      let butt = document.createElement("button");
      butt.setAttribute("class", "w-100 btn btn-lg btn-primary");
      butt.setAttribute("onClick", "edsad()");
      butt.innerText = `Invertir`;
      div5A.appendChild(butt);
      //leyenda button
      let buttSmall = document.createElement("smaill");
      buttSmall.setAttribute("class", "text-muted fw-light");
      buttSmall.innerText = `/Retirar`;
      butt.appendChild(buttSmall);
    })
  );

const edsad = () => {
  console.log("asd");
};
