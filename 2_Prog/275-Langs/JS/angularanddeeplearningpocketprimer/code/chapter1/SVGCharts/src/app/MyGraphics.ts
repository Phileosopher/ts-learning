import {Component} from '@angular/core';

@Component({
 selector: 'mycharts',
 template: `<svg id="svg" width="600" height="600"
              (click)="drawCharts($event)">
            </svg>
           ` 
})
export class MyGraphics {
   public scatterWidth:number  = 400;
   public scatterHeight:number = 400;
   public scatterCount:number  = 40;
   public offsetX:number       = 0;
   public offsetY:number       = 0;
   public clickCount:number    = 0;
   public radius:number        = 5;
   public barCount:number      = 15;
   public barWidth:number      = 30;
   public barHeight:number     = 50;
   public maxBarHeight:number  = 200;
   public barHeights:any       = [];
   public polyPts:any          = ""; 

   public colors = ["#ff0000","#00ff00","#ffc800","#0000ff"];
   public svgns  = "http://www.w3.org/2000/svg";

   private generateBarHeights() {
     for(let i=0; i<this.barCount; i++) { 
        this.barHeights[i] = ""+Math.random()*this.maxBarHeight;
     }
   }

   drawCharts(event) {
      this.generateBarHeights();
      this.drawBarChart();
      this.drawScatterPlot();
      this.drawLineGraph();
      this.clickCount += 1;
   }

   private drawBarChart() {
     var svg = document.getElementById("svg");
     var gElem = document.createElementNS(this.svgns, "g");
     svg.appendChild(gElem);

     for(let i=0; i<this.barCount; i++) { 
        var rect = document.createElementNS(this.svgns, "rect");
        rect.setAttribute("x",      ""+i*this.barWidth);
        rect.setAttribute("y",      ""+(200-this.barHeights[i]));
        rect.setAttribute("width",  ""+this.barWidth);
        rect.setAttribute("height", ""+this.barHeights[i]);
   
        rect.setAttribute("fill", this.colors[i%this.colors.length]);
        gElem.appendChild(rect);
     } 
     svg.appendChild(gElem);
   } 

  private drawLineGraph() {
     var svg = document.getElementById("svg");
     var gElem = document.createElementNS(this.svgns, "g");
     svg.appendChild(gElem);

     // construct a line graph 
     for ( let i = 0; i < this.barCount; i++) {
        this.polyPts += (i*this.barWidth).toString() + "," + 
                        (600-this.barHeights[i]) + " ";
     }
 
     var polyline = document.createElementNS(this.svgns, "polyline");
     polyline.setAttribute("points", ""+this.polyPts);
     polyline.setAttribute("style",  
                "fill:none;stroke:blue;stroke-width:3");
     gElem.appendChild(polyline);
     svg.appendChild(gElem);
  }

  private drawScatterPlot() {
     var svg = document.getElementById("svg");
     var gElem = document.createElementNS(this.svgns, "g");
     svg.appendChild(gElem);

     // construct circles 
     for(let i=0; i<this.scatterCount; i++) { 
        var circle = document.createElementNS(this.svgns, "circle");
        this.offsetX = this.scatterWidth*Math.random();
        this.offsetY = 200*Math.random();
        circle.setAttribute("cx", ""+this.offsetX);
        circle.setAttribute("cy", ""+(200+this.offsetY));
        circle.setAttribute("r",  ""+this.radius);
   
        circle.setAttribute("fill", this.colors[i%this.colors.length]);
        gElem.appendChild(circle);
     } 
     svg.appendChild(gElem);
  }
}

