import {Component} from '@angular/core';
import { Inject } from '@angular/core';

@Component({ 
  selector: 'user',
  template: '<h2></h2>'
})
export class User {
  fname: string; 
  lname: string; 
  imageUrl: string;
  
  constructor(@Inject(String) fname: string, 
              @Inject(String) lname: string, 
              @Inject(String) imageUrl: string) {
     this.fname = fname; 
     this.lname = lname; 
     this.imageUrl = imageUrl; 
  }              
} 

