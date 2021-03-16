import { Component }   from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { FormGroup }   from '@angular/forms';
import { FormControl } from '@angular/forms';

@Component({
  selector:    'app-root',
  templateUrl: './app.component.html',
  styleUrls:   ['./app.component.css']
})
export class AppComponent {
   userForm: FormGroup;
   disabled:boolean;

   constructor(fb: FormBuilder) {
     this.userForm = fb.group({
        name:    'Jane',
        email:   'jsmith@yahoo.com',
        address: fb.group({
          city:  'San Francisco',
          state: 'California'
        })
     });
   }

   onFormSubmitted(theForm : FormGroup) {
      console.log("name  = "+theForm.controls['name'].value);
      console.log("email = "+theForm.controls['email'].value);
      console.log("city  = "+theForm.get('address.city').value);
      console.log("state = "+theForm.get('address.state').value);
   }
}

