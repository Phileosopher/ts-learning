import {Component}  from '@angular/core';
import {Injectable} from '@angular/core';

@Injectable()
class Service {
  somedata = ["a","b","c"];
  constructor() { } 
  
  getData() { return this.somedata; }
  toString() { return "From toString"; }
}
 
@Component({
  selector: 'my-app',
  providers: [ Service ],  
  template: `{{ service.getData() }}`
})
export class AppComponent {
  constructor(public service: Service) { } 
}

