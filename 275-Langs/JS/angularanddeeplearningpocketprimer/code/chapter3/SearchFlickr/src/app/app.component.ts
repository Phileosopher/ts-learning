import { Component } from '@angular/core';

// remember: npm install jquery --save
import * as $ from "jquery";

@Component({
   selector: 'app-root',
   template: `
       Enter a word and search for related images:
       <br />
       <input id="searchterm" />
       <button (click)="httpRequest()">Search</button>
       <div id="images"></div>
   `
})
export class AppComponent {
  imageCount = 4;
  url = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";

  constructor() {} 

  httpRequest() {  
    $.getJSON(this.url,
    {
      tags: $("#searchterm").val(),
      tagmode: "any",
      format: "json"
    },
    function(data) {
      $.each(data.items, function(i,item){
        $("<img/>").attr("src", item.media.m).prependTo("#images");
      //if ( i == this.imageCount ) return false;
      });
    });
  }
}

