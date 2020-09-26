

let name = 'SodaStereo';
let rec = '2';
 d3.select('h2').text("Relaciones de " + name);


let svg = d3.select('svg#simulacion-principal');
let svgA = d3.select('svg#ficha-artista');


let width  = svg.attr('width');
let height = svg.attr('height');
let k = height / width;


let radio = d3.scalePow()
    .exponent(2.5)
    .domain([0,100])
    .range([10,60]);

let chargeS = d3.scaleLinear()
    .domain([0, 100])
    .range([0, -1000]);


// SLIDER Charge | 23.09.2020 | jpi


let sliderCharge = d3.sliderBottom()
    .min(0)
    .max(100)
    .width(200)
    .tickFormat(d3.format(''))
    .ticks(0)
    .default(50);


let gSimple = d3.select('div#charge-slider')
    .append('svg')
    .attr('width', 300)
    .attr('height', 100)
    .append('g')
    .attr('transform', 'translate(30,30)');


gSimple.call(sliderCharge);


// importar información | 23.09.2020 | jpi
d3.json("./relaciones/" + name + "_r" + rec + ".json").then(function (data) {


    // SIMULATION | 23.09.2020 | jpi
    let simulation = d3.forceSimulation(data.nodes)
        .force('link',d3.forceLink(data.links).id( d => d.id))
        .force('charge', d3.forceManyBody().strength(chargeS(sliderCharge.value())))
        .force('center', d3.forceCenter(width/2,1*height/2))
        .force('collision', d3.forceCollide().radius(function(d) {
                return radio(d.popularidad) * 1.5;
              }))
        .on('tick',ticked);

    /*--- FICHA DE ARTISTA ---*/
    let image = svgA.append('rect')
        .attr('height', 80)
        .attr('width', 80)
        .style('fill','yellow')
        .attr('transform', 'translate(30,30)');


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
        .style('stroke','pink');


    // Activar y desactivar texto | 24.09.2020 | jpi
    function textON () {
        texto.on('mouseover',function (d) {
            d3.select(this).style('opacity',1)});
    };
    function textOFF () {
        texto.on('mouseout',function (d) {
            d3.select(this).style('opacity',0)});
    };


    // Se genera un espacio compartido entre nodos y texto | 24.09.2020 | jpi
    let textAndNodes = g.append('g')
        .selectAll('g')
        .data(data.nodes)
        .enter().append('g');


    // Se agregan los nodos | 24.09.2020 | jpi
    let node = textAndNodes.append('circle')
        .attr('r',function (d) {
            return radio(d.popularidad);
        })
        .attr('fill', function (d) {
            if (d.nombre.replace(' ','') == name){
                return '#DAF238';
            } else {
                return 'orange';
            }
        })
        .attr('stroke',function (d) {
            if (d.nombre.replace(' ','') == name){
                return '#27DB90';
            } else {
                return 'yellow';
            }
        })
        .on('mouseover',function () {
            textON();
        })
        .on('mouseout',function () {
            textOFF();
        });


    // agregan los elementos de texto | 24.09.2020 | jpi
    let texto = textAndNodes.append('text')
        .text(function (d) {return d.nombre;})
        .style('fill','#3B5499')
        .style('opacity',0);


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
        simulation.force('charge', d3.forceManyBody().strength(chargeS(sliderCharge.value())));
        textAndNodes.attr('transform',function (d) {
            return "translate(" + d.x + "," + d.y + ")";
        });
        link.attr('x1',function (d) { return d.source.x; })
        link.attr('y1',function (d) { return d.source.y; })
        link.attr('x2',function (d) { return d.target.x; })
        link.attr('y2',function (d) { return d.target.y; })
    };


});
