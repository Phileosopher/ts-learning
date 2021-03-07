import {Component}    from '@angular/core';
import {Input}        from '@angular/core';
import {Output}       from '@angular/core';
import {EventEmitter} from '@angular/core';

@Component({
  selector: 'child-comp',
  template: `
     <button (click)="decrement();">Subtract</button>
     <input type="text" [value]="childValue">
     <button (click)="increment();">Add</button>
   `   
})
export class ChildComponent {
  @Input() childValue:number = 3;  
  @Output() childValueChange = new EventEmitter();

  constructor() {
    console.log("constructor childValue = "+this.childValue); 
  }
  increment() {
    this.childValue++;

    this.childValueChange.emit({
      value: this.childValue
    })
  }
  decrement() {
    this.childValue--;

    this.childValueChange.emit({
      value: this.childValue
    })
  }
}

