import {Component} from '@angular/core';
import {User}      from './user.component';

@Component({ 
  selector: 'user-comp',
  template: '<h2></h2>'
})
export class UserService {
  userList:User[];
     
  constructor() {
     this.userList = [
                  new User('Jane','Smith','assets/sample1.png'),
                  new User('John','Stone','assets/sample2.png'),
                  new User('Dave','Jones','assets/sample3.png'),
                 ]
  }       
       
  getUserList() {
     return this.userList;
  }
}

