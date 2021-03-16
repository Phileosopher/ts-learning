import { Component } from '@angular/core';

@Component({
   selector: 'app-root',
   template: `
     <div>
       <input #fname>
       <button (click)="clickMe(fname.value)">ClickMe</button>
       <ul>
         <li *ngFor="let user of users">
           <button (click)="deleteMe(user)">Delete</button>
           {{user}}
         </li>
       </ul>
     </div>`
})
export class AppComponent {
   users = ["Jane", "Dave", "Tom"];

   deleteMe(user) {
      console.log("delete user = "+user);
      var index = this.users.indexOf(user);

      if(index >=0 ) {
         this.users.splice(index, 1);
      }
   }
   clickMe(user) {
      console.log("new user = "+user);
      this.users.push(user);
/*
      // prevent empty user or duplicates
      if(user is non-null) {
        if(user is duplicate) {
          // display alert message
        } else {
          // display alert message
        }
      } else {
        // display alert message
      }
*/
   }
}
