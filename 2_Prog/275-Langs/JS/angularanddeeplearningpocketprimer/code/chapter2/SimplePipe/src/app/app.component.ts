import { Component } from '@angular/core';
import {User}        from './user.component';
import {MyPipe}      from './pipe.component';

@Component({
  selector: 'app-root',
  template: `
    <div>
      <h2>Complete List of Users:</h2>
      <ul>
       <li
       *ngFor="let user of userList"
         (mouseover)='mouseEvent(user)'
         [class.chosen]="isSelected(user)">
         {{user.fname}}-{{user.lname}}<br/>
       </li>
      </ul>

      <h2>Filtered List of Users:</h2>
      <ul>
       <li
       *ngFor="let user of userList|MyPipe"
         (mouseover)='mouseEvent(user)'
         [class.chosen]="isSelected(user)">
         {{user.fname}}-{{user.lname}}<br/>
       </li>
      </ul>
    </div>
   `
})
export class AppComponent {
  user:User;
  currentUser:User;
  userList:User[];

  mouseEvent(user:User) {
     console.log("current user: "+user.fname+" "+user.lname);
     this.currentUser = user;
  }

  isSelected(user: User): boolean {
    if (!user || !this.currentUser) {
      return false;
    }

    return user.lname === this.currentUser.lname;
  //return true;
  }

  constructor() {
     this.userList = [
                  new User('Jane','Smith'),
                  new User('John','Stone'),
                  new User('Dave','Jones'),
                  new User('Rick','Heard'),
                 ]
  }
}


