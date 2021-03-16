import {Component}    from '@angular/core';
import {TodoService } from './todoservice';

@Component({
 selector: 'todo-list',
 template: `<div>
             <ul>
               <li *ngFor="let todo of todoService.todos">
                 {{todo}}
               </li>
             </ul>
            </div>`
}) 
export class TodoList {
   constructor(public todoService:TodoService) {}  
}   

