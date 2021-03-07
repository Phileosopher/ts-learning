import {Component} from '@angular/core';
import { Inject } from '@angular/core';

@Component({
  selector: 'current-user',
  template: '<h1></h1>'
})
export class UserComponent {
  constructor(@Inject(String) private field1: string, 
              @Inject(String) private field2: string, 
              @Inject(String) private field3: string) { 
     this.field1 = field1;
     this.field2 = field2;
     this.field3 = field3;
  }
}

