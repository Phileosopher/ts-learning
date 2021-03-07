import { BrowserModule } from '@angular/platform-browser';
import { NgModule }      from '@angular/core';
import { FormsModule }   from '@angular/forms';
import { AppComponent }  from './app.component';
import { MyPipe }        from './pipe.component';
import { User }          from './user.component';

@NgModule({
  declarations: [
    AppComponent,
    MyPipe,
    User
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
