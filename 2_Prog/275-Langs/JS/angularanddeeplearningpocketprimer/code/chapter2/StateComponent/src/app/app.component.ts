import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: '<h3>My name is {{emp.fname}} {{emp.lname}}</h3>'
})
export class AppComponent {
  public emp = {fname:'John',lname:'Smith',city:'San Francisco'};
  public name  = 'John Smith'

  constructor() {
    this.name = 'Jane Edwards'
    this.emp  = {fname:'Sarah',lname:'Smith',city:'San Francisco'};
  }
}

