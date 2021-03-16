import {Component}  from '@angular/core';
import {Injectable} from '@angular/core';

@Injectable()
class Service {
  somedata = ["one", "two", "three"];
  constructor() { }

  getData()  { return this.somedata; }
  toString() { return "From toString"; }
}

@Component({
  selector: 'app-root',
  providers: [ Service ],
  template: `Data from the service: {{ service.getData() }}`
})
export class AppComponent {
  constructor(public service: Service) { }
}
