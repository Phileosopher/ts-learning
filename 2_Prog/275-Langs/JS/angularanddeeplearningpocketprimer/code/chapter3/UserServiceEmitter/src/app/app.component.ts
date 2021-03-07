import {Component}     from '@angular/core';
import {EventEmitter}  from '@angular/core';
import {UserService}   from './user.service';
import {User}          from './user.component';

@Component({ 
  selector: 'app-root',
  providers: [User, UserService],
  template: `
     <div class="ui items">
       <user-comp
        *ngFor="let user of userList; let i=index" 
          [user]="user"
          (mouseover)="mouseEvent(user)"
          [class.chosen]="isSelected(user)">
          USER {{i+1}}: {{user.fname}}-{{user.lname}}
          <img class="user-image" [src]="user.imageUrl" 
               (mouseenter)="mouseEnter(user)"
               width="50" height="50">
       </user-comp>
     </div> 
    ` 
}) 
export class AppComponent {
  user:User;
  currentUser:User;
  userList:User[];
  onUserSelected: EventEmitter<User>;

  mouseEvent(user:User) {
     console.log("current user: "+user.fname+" "+user.lname); 
     this.currentUser = user;
     this.onUserSelected.emit(user);
  }

  mouseEnter(user:User) {
     console.log("image name: "+user.imageUrl);
     alert("Image name: "+user.imageUrl);
  }

  isSelected(user: User): boolean {
    if (!user || !this.currentUser) {
      return false;
    }

    return user.lname === this.currentUser.lname;
  //return true;
  }

  constructor(userService:UserService) {
     this.onUserSelected = new EventEmitter();
     this.userList = userService.getUserList();
  }
}

