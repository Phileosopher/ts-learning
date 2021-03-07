import {Component} from '@angular/core';

@Component({
   selector: 'cclick',
   styles:   [` li { inline: block } `], 
   template: `
     <div>
      <ul>
       <li><img (click)="onClick(100)" 
                width="100" height="100" src="/src/app/sample1.png"></li>
       <li><img (click)="onClick(200)" 
                width="100" height="100" src="/src/app/sample2.png"></li>
       <li><img (click)="onClick(300)" 
                width="100" height="100" src="/src/app/sample3.png"></li>
      </ul>
     </div>
    ` 
})
export class ClickItem {
  onClick(id) {
    console.log("clickitem clicked: "+id);
  } 
}

