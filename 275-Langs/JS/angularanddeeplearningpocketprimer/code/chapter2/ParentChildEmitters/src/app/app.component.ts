import {Component}      from '@angular/core';
import {EventEmitter}   from '@angular/core';
import {ChildComponent} from './childcomponent';

@Component({
  selector: 'app-root',
  providers: [ChildComponent],
  template: `
     <div>
      <child-comp [childValue]="parentValue"
        (childValueChange)="reportValueChange($event)">
      </child-comp>
     </div>
    `
})
export class AppComponent {
  public parentValue:number = 77;

  constructor() {
    console.log("constructor parentValue = "+this.parentValue);
  }

  reportValueChange(event) {
    console.log(event);
  }
}

