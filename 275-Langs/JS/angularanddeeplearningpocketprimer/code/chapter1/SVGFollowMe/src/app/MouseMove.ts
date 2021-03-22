import {Component} from '@angular/core';

@Component({
 selector: 'mouse-move',
 template: `<svg id="svg" width="600" height="400"
              (mousemove)="mouseMove($event)">
            </svg>
           ` 
})
export class MouseMove {
   radiusX = 25;
   radiusY = 50;

   mouseMove(event) {
     var svgns = "https://www.w3.org/2000/svg";
     var svg   = document.getElementById("svg");
     var colors = ["#ff0000", "#88ff00", "#3333ff"];

     var sum = Math.floor(event.clientX+event.clientY); 

     var ellipse = document.createElementNS(svgns, "ellipse");
     ellipse.setAttribute("cx", ""+event.clientX);
     ellipse.setAttribute("cy", ""+event.clientY);
     ellipse.setAttribute("rx", ""+this.radiusX);
     ellipse.setAttribute("ry", ""+this.radiusY);
     ellipse.setAttribute("fill", colors[sum % colors.length]);
     svg.appendChild(ellipse);
   } 
}

