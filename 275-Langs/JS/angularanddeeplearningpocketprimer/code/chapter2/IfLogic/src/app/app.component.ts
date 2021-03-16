import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
     <h3>Hello everyone!</h3>
     <h3>My name is {{emp.fname}} {{emp.lname}}</h3>
     <button (click)="moreInfo()">More Details</button>
     <div *ngIf="showMore === true">
       <h3>I live in {{emp.city}}</h3>
     </div>

    <div (click)="showDiv = !showDiv">Toggle Me</div>
    <div *ngIf="showDiv"
         style="color:white;background-color:blue; width:25%">Content1</div>
    <div *ngIf="showDiv"
         style="background-color:red; width:25%;">Content2</div>
  `
})
export class AppComponent {
  public emp = {fname:'John',lname:'Smith',city:'San Francisco'};
  public showMore = false;
  public showDiv  = false;

  moreInfo() {
    this.showMore = true;
  }
}
