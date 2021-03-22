import { Component }      from '@angular/core';
import {Inject}           from '@angular/core';
import {HttpClient}       from '@angular/common/http';
//import {HTTP_BINDINGS}  from '@angular/common/http';

@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.css'],
  template: `
    <button (click)="httpRequest()">Post Information</button>
    <div>
<p>
found postData: {{postData}}
</p>
      <li *ngFor="let post of postData">
        {{post.author}}
        {{post.title}}
      </li>
    </div>
  `
})
export class AppComponent {
//postData = [];
  postData:any = [];

  constructor(@Inject(HttpClient) public https:HttpClient) { 
  }

  httpRequest() {  
  //this.http.get('localhost:3000/authors')
    this.http.get('https://localhost:3000/posts')
      .subscribe(
        data => this.postData = JSON.stringify(data),
        err => console.log('error getting data: '+err),
        () => this.postInfo()
      );
  }

  postInfo() {  
     //----------------------------------------------
     // the 'eval' statement is required in order to
     // convert the data retrieved from json-server
     // to an array of JSON objects (else an error) 
     //----------------------------------------------
     var myObject = eval('(' + this.postData + ')');
     console.log("myObject = "+JSON.stringify(myObject));
     this.postData = myObject;
  }
}

