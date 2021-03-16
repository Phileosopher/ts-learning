import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { MouseMove }     from './mousemove';

@NgModule({
  imports: [ BrowserModule ],
  declarations: [ AppComponent, MouseMove ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
