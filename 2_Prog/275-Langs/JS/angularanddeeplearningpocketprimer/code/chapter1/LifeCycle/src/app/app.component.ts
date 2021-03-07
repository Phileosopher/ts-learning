import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: '<h2>Angular Lifecycle Methods</h2>',
})
export class AppComponent{
   ngOnInit() {
     // invoked after child components are initialized
     console.log("ngOnInit");
   }
   ngOnDestroy() {
     // invoked when a component is destroyed
     console.log("ngOnDestroy");
   }
   ngDoCheck() {
     // custom change detection
     console.log("ngDoCheck");
   }
   // => Angular 9 syntax: ngOnChanges(changes) 
   ngOnChanges(changes:any) {
     console.log("ngOnChanges");
     // Invoked after bindings have been checked
     // but only if one of the bindings has changed.
     //
     // changes is an object of the format:
     // {
     //   'prop': PropertyUpdate
     // }
   }
   ngAfterContentInit() {
     // Component content has been initialized
     console.log("ngAfterContentInit");
   }
   ngAfterContentChecked() {
     // Component content has been checked
     console.log("ngAfterContentChecked");
   }
   ngAfterViewInit() {
     // Component views are initialized
     console.log("ngAfterViewInit");
   }
   ngAfterViewChecked() {
     // Component views have been checked
     console.log("ngAfterViewChecked");
   }
}

