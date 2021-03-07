import {Component} from '@angular/core';

@Component({
 selector: 'mouse-move',
 template: `<svg id="svg" width="600px" height="400px"
              (mousemove)="mouseMove($event)">
            </svg>
           `
})
export class MouseMove {
   // => Angular 9 syntax:
   //mouseMove(event) 
   mouseMove(event:any) {
     console.log("Position x: "+event.clientX+" y: "+event.clientY); 
   } 
}

