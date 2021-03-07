import { BrowserModule }        from '@angular/platform-browser';
import {CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';
import { NgModule }             from '@angular/core';
import { AppComponent }         from './app.component';
import { ChildComponent }       from './childcomponent';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [ChildComponent],
  bootstrap: [AppComponent],
  schemas:   [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
