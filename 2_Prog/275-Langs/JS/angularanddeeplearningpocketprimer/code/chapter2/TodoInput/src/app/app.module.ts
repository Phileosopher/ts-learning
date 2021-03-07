import { BrowserModule } from '@angular/platform-browser';
import { NgModule }      from '@angular/core';

import { TodoInput }     from './todoinput';
import { TodoList }      from './todolist';
import { TodoService }   from './todoservice';
import { AppComponent }  from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    TodoInput,
    TodoList
  ],
  imports: [
    BrowserModule
  ],
  providers: [TodoService],
  bootstrap: [AppComponent]
})
export class AppModule { }
