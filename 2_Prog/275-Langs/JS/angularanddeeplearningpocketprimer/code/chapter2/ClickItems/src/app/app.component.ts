import { Component } from '@angular/core';
import {ClickItem} from './clickitem';

@Component({
   selector: 'app-root',
   styles:   [`li { display: inline; }`],
   template: `
    <div>
      <ul>
       <li><img (click)="onClick(100)"
             width="100" height="100" src="assets/sample1.png"></li>
       <li><img (click)="onClick(200)"
             width="100" height="100" src="assets/sample2.png"></li>
       <li><img (click)="onClick(300)"
             width="100" height="100" src="assets/sample3.png"></li>
      </ul>
    </div>

    <div>
    </div>
    `
})
export class AppComponent {
  onClick(id) {
    console.log("app.component.ts: you clicked me: "+id);
  }
}

