import { Component } from '@angular/core';

@Component({
   selector: 'app-root',
   template: `
     <h2>Employee Information</h2>
     <ul>
       <li *ngFor="let emp of employees">
         {{emp.fname}} {{emp.lname}} lives in {{emp.city}}
       </li>
     </ul>
    `,
    styles:  [`
      @keyframes hoveritem {
          0%   {background-color: red;}
          25%  {background-color: #880;}
          50%  {background-color: #ccf;}
          100% {background-color: #f0f;}
      }

      li:hover {
          width: 50%;
          animation-name: hoveritem;
          animation-duration: 4s;
      }
    `]
})
export class AppComponent {
  // => Angular 9 syntax:
  // employees = [];
  employees : any;

  constructor() {
    this.employees = [
     {"fname":"Jane","lname":"Jones","city":"San Francisco"},
     {"fname":"John","lname":"Smith","city":"New York"},
     {"fname":"Dave","lname":"Stone","city":"Seattle"},
     {"fname":"Sara","lname":"Edson","city":"Chicago"}
   ];
  }
}

