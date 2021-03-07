import { Component }   from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { FormGroup }   from '@angular/forms';

@Component({
  selector: 'app-root',
  template: `
    <div>
      <h2>A FormBuilder Form</h2>

      <form [formGroup]="myForm"
            (ngSubmit)="onSubmit(myForm.value)"
            class="ui form">

        <div class="field">
          <label for="fname">fname</label>
          <input type="text"
                 id="fname"
                 placeholder="fname"
                 [formControl]="myForm.controls['fname']">
        </div>

        <div class="field">
          <label for="lname">lname</label>
          <input type="text"
                 id="lname"
                 placeholder="lname"
                 [formControl]="myForm.controls['lname']">
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
   `
})
export class AppComponent {
//myForm: any;
  myForm: FormGroup;

  constructor(fb: FormBuilder) {
    this.myForm = fb.group({
      'fname': ['John'],
      'lname': ['Smith']
    });
  }

  onSubmit(value: string): void {
    console.log('you submitted value:', value);
  }
}

