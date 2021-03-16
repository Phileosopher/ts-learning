import { Component } from '@angular/core';

@Component({
   selector: 'app-root',
   template: `<div>
               <button (click)="clickMe()">ClickMe</button>
               <p>Click count is now {{clickCount}}</p>
              </div>`,
   styles: [` button {
                 color: red;
              }`
           ]
})
export class AppComponent {
   clickCount = 0;

   clickMe() {
      ++this.clickCount;
      console.log("click count: "+this.clickCount);
   }
}
