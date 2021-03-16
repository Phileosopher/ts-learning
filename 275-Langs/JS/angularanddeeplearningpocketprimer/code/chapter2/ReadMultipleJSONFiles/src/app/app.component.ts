import { Component }  from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.css'],
  template:`
    <h2>Angular HTTP and Observables</h2>
    <h3>Some of our Employees</h3>
    <ul>
      <li *ngFor="let emp of employees">
        {{emp.fname}} {{emp.lname}} lives in {{emp.city}}
      </li>
    </ul>
    <h3>Some of our Customers</h3>
    <ul>
      <li *ngFor="let cust of customers">
        {{cust.fname}} {{cust.lname}} lives in {{cust.city}}
      </li>
    </ul>
    <h3>Some of our Relatives</h3>
    <ul>
      <li *ngFor="let rel of relatives">
        {{rel.fname}} {{rel.lname}} lives in {{rel.city}}
      </li>
    </ul>
  `
})
export class AppComponent {
  public employees : any = [];
  public customers : any = [];
  public relatives : any = [];

  constructor(private http:HttpClient) { 
   //this.getCustomers();
   //this.getEmployees();
   //this.getRelatives();
     this.getEveryone();
  }

  getCustomers() {
    this.http.get('assets/customers.json')
      .subscribe(
        // this function runs on success
        data => { this.customers = data },
        // this function runs on error 
        err => console.log('error reading customer data: '+err),
        // this function runs on completion
        () => console.log('Loading customers completed')
      );
  }

  getEmployees() {
    this.http.get('assets/employees.json')
      .subscribe(
        // this function runs on success
        data => { this.employees = data },
        // this function runs on error
        err => console.log('error reading employee data: '+err),
        // this function runs on completion
        () => console.log('Loading employees completed')
      );
  }

  getRelatives() {
    this.http.get('assets/relatives.json')
      .subscribe(
        // this function runs on success
        data => { this.relatives = data },
        // this function runs on error
        err => console.log('error reading relatives data: '+err),
        // this function runs on completion
        () => console.log('Loading relatives completed')
      );
  }

  getEveryone() {
    this.getCustomers();
    this.getEmployees();
    this.getRelatives();
  }

  infoResults() {
    console.log('inside infoResults');
    console.log('this.customers:',this.customers);
    console.log('this.employees:',this.employees);
    console.log('this.relatives:',this.relatives);
  }
}

