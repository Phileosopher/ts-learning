import {Component} from '@angular/core';
import { Inject } from '@angular/core';

@Component({
  selector: 'my-user',
  template: '<h1></h1>'
})
export class User {
  fname: string;
  lname: string;

  constructor(@Inject(String) fname: string, @Inject(String) lname: string) {
     this.fname = fname;
     this.lname = lname;
  }
}

