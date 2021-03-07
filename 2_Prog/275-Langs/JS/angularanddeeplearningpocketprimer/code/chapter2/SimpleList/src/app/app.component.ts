import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `<div *ngFor="let item of items">
               {{item}}
             </div>`
})
export class AppComponent {
  items : any;

  constructor() {
    this.items = ['one','two','three','four'];
  }
}

