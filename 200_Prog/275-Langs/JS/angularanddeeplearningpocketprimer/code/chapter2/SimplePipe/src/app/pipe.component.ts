import {Component} from '@angular/core';
import {Pipe}      from '@angular/core';

@Pipe({
  name: "MyPipe"
})
export class MyPipe {
  transform(item) {
    return item.filter((item) => item.fname.startsWith("J"));
  //return item.filter((item) => item.lname.endsWith("th"));
  //return item.filter((item) => item.lname.contains("n"));
  }
}

