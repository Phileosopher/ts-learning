// part #1: new import statement 
import { Component, Input } from '@angular/core';
import {trigger, state, style, transition, animate} from '@angular/animations';

// part #2: new Emp class 
class Emp {
  constructor(public fname: string, 
              public lname: string, 
              public city:  string, 
              public state = 'inactive') {
  }
   
  toggleState() {
    this.state = (this.state === 'active' ? 'inactive' : 'active');
    console.log(this.fname+" "+"new state = "+this.state);
  }
}
@Component({
   selector: 'app-root',
   // part #3: new animations property 
   animations: [
     trigger('empState', [
       state('inactive', style({
         backgroundColor: '#eee',
         transform: 'scale(1)'
       })),
       state('active',   style({
         backgroundColor: '#cfd8dc',
         transform: 'scale(1.1)'
       })),
       transition('inactive => active', animate('100ms ease-in')),
       transition('active => inactive', animate('100ms ease-out'))
     ])
   ],
   template: `
     <h2>Employee Information</h2>
     <ul>
       <li *ngFor="let emp of employees" 
                   [@empState]="emp.state" 
                   (mousemove)="emp.toggleState()">
         {{emp.fname}} {{emp.lname}} lives in {{emp.city}}
       </li>
     </ul>
    `
})
export class AppComponent {
  // => Angular 9 syntax:
  // employees = [];
  employees : any;

  constructor() {
    // part #5: array of Emp objects 
    this.employees = [
     new Emp("Jane","Jones","San Francisco"),
     new Emp("John","Smith","New York"),
     new Emp("Dave","Stone","Seattle"),
     new Emp("Sara","Edson","Chicago")
   ];
  }
}

