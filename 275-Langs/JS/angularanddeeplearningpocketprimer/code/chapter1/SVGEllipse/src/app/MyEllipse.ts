import {Component} from '@angular/core';

@Component({
   selector: 'my-svg',
   template: `
     <svg width="500" height="300">
       <ellipse cx="100" cy="100"
                rx="80" ry="40" 
                fill="red"/>
       <ellipse cx="180" cy="100"
                rx="80" ry="40" 
                fill="blue"/>
       <ellipse cx="140" cy="140"
                rx="80" ry="40" 
                fill="yellow"/>
     </svg> 
     `
})
export class MyEllipse{}

