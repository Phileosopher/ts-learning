import { Component }   from '@angular/core';
import { Observable}   from 'rxjs';
import { Inject }      from '@angular/core';
import { HttpClient }  from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
declare var $: any;

@Component({
  selector: 'app-root',
  template: `
     <button (click)="httpRequest()">Employee Info</button>
     <ul>
       <li *ngFor="let emp of employees">
         {{emp.fname}} {{emp.lname}} lives in {{emp.city}} 
       </li>
     </ul>
  `
})
export class AppComponent {
  employees : any;

  constructor(@Inject(HttpClient) public http:HttpClient) {}

  httpRequest() {  
    this.http.get('assets/employees.json')
      .subscribe(
        // this function runs on success
        data => this.employees = data,
        // this function runs on error
        err => console.log('error reading data: '+err),
        // this function runs on completion
        () => this.userInfo()
      );
  }

  userInfo() {  
 //console.log("employees = "+JSON.stringify(this.employees));
  }
}

