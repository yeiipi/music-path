let nombre_banda = "LasBistecs"
let n_recurcion  = "2"

let info_del_buscador = navigator.userAgent


/*--- poder elegir aristas ---*/
// function menu_artistas(data) {
//     for (let i in data) {
//         console.log(data[i].nombre + "|" + data[i].recursion +" -> "+ data[i].jn);
//     }
// };
//
// d3.json("../relaciones/nombres.json").then(function (D) {
//     console.log(D);
//     menu_artistas(D);
// });

/*--- Variables técnicas ---*/
let width = window.innerWidth
let height = window.innerHeight
let k = height/width;

/*--- mapeos de datos ---*/

let radio = d3.scalePow()
    .exponent(2.5)
    .domain([0,100])
    .range([10,60]);

let chargeS = d3.scaleLinear()
    .domain([0, 100])
    .range([0, -1000]);

function max_letras (d) {
    let m = Math.max(d);
    console.log(m);
    return m;
};

/*--- Variables D3JS ---*/

let universo_cambiante = d3.select("div#universo");
universo_cambiante.attr('width', width).attr('height', height)

let titulo = d3.select('p#titulo-principal')
    .on("mouseover",function (d) {
        d3.select(this).style("cursor", "pointer")
        d3.select(this).style("font-weight",300)
        d3.select("p#sub-titulo").style("font-weight",900)
    })
    .on("mouseout",function (d) {
        d3.select(this).style("cursor", "default")
        d3.select(this).style("font-weight",100)
        d3.select("p#sub-titulo").style("font-weight",700)
    })
    .on("click",function (d) {
        d3.selectAll(".descripcion").transition()
            .duration(200)
            .style("font-size","0px")
            .style("opacity",0);
        a_correr_se_dijo()

    });

let letrerito = d3.select("body").append("div")
    .attr("class","tooltip")
    .style("opacity",1e-6);


let svg = universo_cambiante.append('svg');
svg.attr('width', width).attr('height', height)

/*--- Funciones letrerito ---*/
function mouseover() {
    letrerito.transition()
        .duration(300)
        .style("opacity",1);
}

function mousemove(d) {
    let textoA = "Nombre: ";
    let textoB = "Popularidad: ";
    let textoC = "Seguidores: " ;
    if (info_del_buscador.includes("Firefox")) {
        // console.log("U in Firefox");
        textoA += d.explicitOriginalTarget.__data__.nombre + " ";
        textoB += d.explicitOriginalTarget.__data__.popularidad + " ";
        textoC += d.explicitOriginalTarget.__data__.seguidores + " ";
    } else if (info_del_buscador.includes("Chrome")) {
        // console.log("U in chrome");
        textoA += d.toElement.__data__.nombre + " ";
        textoB += d.toElement.__data__.popularidad + " ";
        textoC += d.toElement.__data__.seguidores + " ";
    } else {
        console.log("U in neither");
    }

    let lA = textoA.length;
    let lB = textoB.length;
    let lC = textoC.length;
    let lM = Math.max(lA,lB,lC);


    letrerito.html(textoA+"<br/>"+textoB+"<br/>"+textoC)
        .attr("width",(lM*15)+"px")
        .style("left", (event.pageX) + "px")
        .style("top", (event.pageY) + "px");
}

function mouseout() {
    letrerito.transition()
        .duration(300)
        .style("opacity",1e-6);
}

function a_correr_se_dijo() {
    d3.selectAll(".descripcion").transition().delay(1000).style('position','absolute')
    d3.json("relaciones/"+nombre_banda+"_r"+n_recurcion+".json").then( function (data) {

        // SIMULATION | 23.09.2020 | jpi
    let simulation = d3.forceSimulation(data.nodes)
        .force('link',d3.forceLink(data.links).id( d => d.id))
        .force('charge', d3.forceManyBody().strength(chargeS(85)))
        .force('center', d3.forceCenter(1*width/2,2*height/3))
        .force('collision', d3.forceCollide().radius(function(d) {
                return radio(d.popularidad) * 2;
              }))
        .on('tick',ticked);

    /*--- GRAFICA DE GRAFOS ---*/
    let g = svg.append('g')
        .attr('class','everything');


    // Se generan las aristas | 24.09.2020 | jpi
    let link = g.append("g")
        .selectAll("line")
        .data(data.links)
        .enter().append('line')
        .attr('stroke-width',function(d) {
            return 3;
        })
        .style('stroke','#CC9E9B');


    // Se genera un espacio compartido entre nodos y texto | 24.09.2020 | jpi
    let textAndNodes = g.append('g')
        .selectAll('g')
        .data(data.nodes)
        .enter().append('g');


    // Se agregan los nodos | 24.09.2020 | jpi
    let node = textAndNodes.append('circle')
        .attr("class","node")
        .attr("cursor","crosshair")
        .attr('r',function (d) {
            return radio(d.popularidad);
        })
        .attr('fill', function (d) { return '#9BCCAF'; })
        .attr('stroke',function (d) { return '#5F9962'; })
        .style('opacity',1)
        .on('mouseover', mouseover)
        .on('mousemove',function (d){ mousemove(d); })
        .on('mouseout',mouseout);


    /*--- EVENTOS DE ZOOM ---*/
    let zoom = d3.zoom()
        .scaleExtent([0.05,32])
        .on('zoom',zoomed);


    svg.call(zoom).call(zoom.transform,d3.zoomIdentity);


    function zoomed ({transform}) {
        g.attr("transform", transform)
            .attr("stroke-width", 3 / transform.k);
    }


    /*--- FUNCIONES IMPORTANTES ---*/
    function ticked() {
        simulation.force('charge', d3.forceManyBody().strength(chargeS(90)));
        textAndNodes.attr('transform',function (d) { return "translate(" + d.x + "," + d.y + ")"; });
        link.attr('x1',function (d) { return d.source.x; })
        link.attr('y1',function (d) { return d.source.y; })
        link.attr('x2',function (d) { return d.target.x; })
        link.attr('y2',function (d) { return d.target.y; })
    };

    })};


