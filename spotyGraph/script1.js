


let name = "DoblePorcion";
let rec = '2';
 d3.select('h1').append('h1').text("Relaciones de " + name);

let svg = d3.select('svg');
let width  = svg.attr('width');
let height = svg.attr('height');
let k = height / width;


let radio = d3.scaleLinear()
    .domain([0,100])
    .range([10,35]);

// SLIDER Charge | 23.09.2020 | jpi
var sliderCharge = d3
    .sliderBottom()
    .min(-300)
    .max(0)
    .width(300)
    .tickFormat(d3.format(''))
    .ticks(0)
    .default(-30)
    .on('onchange', val => {
        d3.select('p#value-simple').text(d3.format('')(val));
    });


var gSimple = d3
    .select('div#charge-slider')
    .append('svg')
    .attr('width', 500)
    .attr('height', 100)
    .append('g')
    .attr('transform', 'translate(30,30)');


gSimple.call(sliderCharge);


d3.select('p#value-simple').text(d3.format('')(sliderCharge.value()));


// importar información | 23.09.2020 | jpi
d3.json(name + "_r" + rec + ".json").then(function (data) {


    // SIMULATION | 23.09.2020 | jpi
    let simulation = d3.forceSimulation(data.nodes)
        .force('link',d3.forceLink(data.links).id( d => d.id))
        .force('charge', d3.forceManyBody().strength(sliderCharge.value()))
        .force('center', d3.forceCenter(width/2,1*height/2))
        .force('collision', d3.forceCollide().radius(function(d) {
                return radio(d.popularidad);
              }))
        .on('tick',ticked);


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
            return 'orange';
        })
        .attr('stroke','yellow')
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


    /*--- EVENTOS DE ZOOM Y DRAG  ---*/
    let zoom = d3.zoom()
        .scaleExtent([0.5,32])
        .on('zoom',zoomed);

    svg.call(zoom).call(zoom.transform,d3.zoomIdentity);


    // Escalas con respecto a X y Y | 24.09.2020 | jpi
    x = d3.scaleLinear()
        .domain([-4.5, 4.5])
        .range([0, width]);
    y = d3.scaleLinear()
        .domain([-4.5 * k, 4.5 * k])
        .range([height, 0])


    function zoomed ({transform}) {
        // const zx = transform.rescaleX(x).interpolate(d3.interpolateRound);
        // const zy = transform.rescaleY(y).interpolate(d3.interpolateRound);
        g.attr("transform", transform).attr("stroke-width", 5 / transform.k);
    }



    /*--- FUNCIONES IMPORTANTES ---*/
    function ticked() {
        simulation.force('charge', d3.forceManyBody().strength(sliderCharge.value()));
        textAndNodes.attr('transform',function (d) {
            return "translate(" + d.x + "," + d.y + ")";
        });
        link.attr('x1',function (d) { return d.source.x; })
        link.attr('y1',function (d) { return d.source.y; })
        link.attr('x2',function (d) { return d.target.x; })
        link.attr('y2',function (d) { return d.target.y; })
        // node.attr('cx',function (d) { return d.x;})
        // node.attr('cy',function (d) { return d.y;});
    };


});
