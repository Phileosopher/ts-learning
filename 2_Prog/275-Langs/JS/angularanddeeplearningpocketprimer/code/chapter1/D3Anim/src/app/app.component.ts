import { Component } from '@angular/core';
import * as d3 from 'd3';

// remember: npm install d3 --save

@Component({
  selector: 'app-root',
  template: `<app-root><mysvg></mysvg></app-root>`,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor() { 
     var width = 800, height = 500, duration=2000;
     var radius = 30, moveCount = 0, index = 0;
     var circleColors = ["red", "yellow", "green", "blue"];

     var svg = d3.select("body")
                 .append("svg")
                 .attr("width",  width)
                 .attr("height", height);

     svg.on("mousemove", function() {
       index = (++moveCount) % circleColors.length;

       var circle = svg.append("circle")
                       .attr("cx", (width-100)*Math.random())
                       .attr("cy", (height-100)*Math.random())
                       .attr("r",  radius)
                       .attr("fill", circleColors[index])
                       .transition()
                       .duration(duration) 
                       .attr("transform", function() {
                          return "scale(0.5, 0.5)";
                        //return "rotate(-20)";
                       }) 
     });
  }
}
