import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
   <h2>{{radioTitle}}</h2>
   <label *ngFor="let item of radioItems">
      <input type="radio" name="options"
             (click)="model.options = item"
             [checked]="item === model.options">
      {{item}}
   </label>
   <p><button (click)="model.options='option1'">Set Option #1</button>
  `
})
export class AppComponent {
  radioTitle = "Radio Buttons in Angular";
  radioItems = ['option1','option2','option3','option4'];
  model = { options: 'option3' };
}

