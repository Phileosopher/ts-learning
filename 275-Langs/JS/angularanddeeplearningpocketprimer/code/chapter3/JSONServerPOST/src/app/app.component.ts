import { Component } from '@angular/core';
import {Inject}      from '@angular/core';
import { HttpClient} from '@angular/common/http';

// remember: npm install jquery --save
import * as $ from "jquery";

@Component({
   selector: 'app-root',
   template: `
     <button (click)="getAuthorData()">Click to Display Author Info</button>
     <div>
       <table>
         <thead *ngIf="foundData">
           <th>AUTHORID</th>
           <th>Title</th>
           <th>Author</th>
         </thead>
         <tbody>
           <tr *ngFor="let author of authorData">
             <td>{{author.id}}</td>
             <td>{{author.title}}</td>
             <td>{{author.author}}</td>
           </tr>
         </tbody>
       </table>
       <button (click)="postAuthorData()">Click to Add New Author</button>
     </div>
    `  
})
export class AppComponent {
  foundData   = false;
  authorData  : any;
  currData    = {};
  idIncr      = 100;
  newAuthorId = 0;
  newTitle    = "";
  newAuthor   = "";
  largestId   = 1000000;

  constructor(@Inject(HttpClient) public https:HttpClient) {}

  postAuthorData() {
  //this.newAuthorId = 0+this.largestId+this.idIncr;
    this.newAuthorId = Math.round(Math.random()*this.largestId);
    this.newTitle    = "The Book of "+this.newAuthorId;
    this.newAuthor   = "My New Title"+this.newAuthorId;

    var postNewAuthor = {id:this.newAuthorId,
                         title:this.newTitle,
                         author:this.newAuthor};

//console.log("postNewAuthor: "+JSON.stringify(postNewAuthor));

    $.post("https://localhost:3000/authors",
       postNewAuthor,
       function(result, textStatus, jqXHR) {
  //console.log("2returned result: "+JSON.stringify(result));
           this.authorData.push(postNewAuthor);
       }.bind(this),"json")
        .fail(function(jqXHR, textStatus, errorThrown) {
  console.log("error: "+errorThrown+" textStatus: "+textStatus);
       });

    // prevent a page reload:
    return false;
  }

  getAuthorData() {
    this.http.get('https://localhost:3000/authors')
      .subscribe(
        data => this.authorData = data,
        err => console.log('error: '+err),
        () => this.authorInfo()
      );

    // prevent a page reload:
    return false;
  }

  authorInfo() {
     this.largestId = 
         parseInt(this.authorData[this.authorData.length-1].id,10);

   //console.log("largestId   = "+ this.largestId);
   //console.log("authorData1 = "+ JSON.stringify(this.authorData));
     this.foundData = true;

    // prevent a page reload:
    return false;
  } 
}

