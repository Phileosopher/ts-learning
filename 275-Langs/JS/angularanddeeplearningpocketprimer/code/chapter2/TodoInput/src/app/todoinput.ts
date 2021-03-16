import {Component}    from '@angular/core';
import {TodoService } from './todoservice';

@Component({
   selector: 'todo-input',
   template: `
      <div>
        <input type="text" #myInput>
        <button (click)="mouseEvent(myInput.value)">Add Item</button>
      </div>
   `
})
export class TodoInput{
   constructor(public todoService:TodoService) {}          

   mouseEvent(value) {
      if((value != null) && (value.length > 0)) {
        this.todoService.todos.push(value);
        console.log("todos: "+this.todoService.todos);
      } else { 
         console.log("value must be non-null");
      } 
   }
}

