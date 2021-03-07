import { Component }     from '@angular/core';
import { Inject }        from '@angular/core';
import { HttpClient }    from '@angular/common/http';
import { UserComponent } from './user.component';
import { Observable }    from 'rxjs';

@Component({
  selector: 'app-root',
  template: `
    <div>
      <form> 
        <h3>Search Github For User:</h3>
        <div class="field">
          <label for="guser">Github Id</label>
          <input type="text" #guser>
        </div>

        <button (click)="findGithubUser(guser)">
          >>> Find User <<<
        </button>
      </form>

      <div id="container">
       <div class="onerow">
        <h3>List of Users:</h3>
        <ul>
         <li *ngFor="let user of users"
             (mouseover)="currUser(user)">
          {{user.field1}} {{user.field2}}</li>
        </ul>
       </div>
      </div>
    </div>
  `
})
export class AppComponent {
  currentUser:UserComponent = new UserComponent('ABC', 'DEF', '');
  users: UserComponent[];
  githubUserInfo : any;
  githubUserJSON:JSON;
  user:UserComponent;
  userStr:string = "";
  guserStr:string = "";

  constructor(@Inject(HttpClient) public http:HttpClient) { 
    this.users = [
      new UserComponent('Jane', 'jsmith', ''),
      new UserComponent('John', 'jstone', ''),
    ];
  }

  currUser(user) {
    console.log("fname: "+user.field1+" lname: "+user.field2);
    this.currentUser = new UserComponent(user.field1, 
                                         user.field2, 
                                         user.field3);
  }

  findGithubUser(guser: HTMLInputElement): boolean {
    if((guser.value == undefined) || (guser.value == "")) {
       alert("Please enter a user name");
       return;
    }

    // guser.value is not available in the 'subscribe' method
    this.guserStr = guser.value;

    this.http.get('https://api.github.com/users/'+guser.value)
     .subscribe(data => {
        this.githubUserInfo = data; 
        //console.log("github info = "+JSON.stringify(data));

        // create a new User instance:
        this.user = new UserComponent(this.githubUserInfo.name, 
                                      this.guserStr,
                                      this.githubUserInfo.created_at);

        // append new User instance to list of users:
        this.users.push(this.user); },
       err => { 
         console.log("Lookup error: "+err);
         alert("Lookup error: "+err);
       } 
     );

    // reset the input field to an empty string
    guser.value = "";

    // prevent a page reload:
    return false;
  }
}

