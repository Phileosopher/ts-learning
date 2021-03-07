import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div> 
      <h2>A Sample Form</h2> 
      <form #f="ngForm"
            (ngSubmit)="onSubmit(f.value)"
            class="ui form">
        <div class="field">
          <label for="fname">fname</label>
          <input type="text"
                 id="fname"
                 placeholder="fname"
                 name="fname" ngModel>

          <label for="lname">lname</label>
          <input type="text"
                 id="lname"
                 placeholder="lname"
                 name="lname" ngModel>
        </div>

        <button type="submit">Submit</button> 
      </form>
    </div>
   ` 
}) 
export class AppComponent {
  myForm: any;

  onSubmit(form: any): void {
    console.log('you submitted value:', form);
  }
}

