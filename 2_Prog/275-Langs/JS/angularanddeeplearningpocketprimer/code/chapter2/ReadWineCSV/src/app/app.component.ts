import { Component }   from '@angular/core';  
import { Inject }      from '@angular/core';
import { HttpClient }  from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Observable }  from 'rxjs';

@Component({  
  selector: 'app-root',  
  styleUrls: ['./app.component.css'],
  template: `
    <table> 
      <thead>    
       <tr>    
         <th>{{headers[0]}}</th>    
         <th>{{headers[1]}}</th>    
         <th>{{headers[2]}}</th>    
       </tr>    
      </thead>    
      <tbody>    
        <tr *ngFor="let record of records;let i = index;">    
          <td> <span>{{record[0]}}</span> </td>    
          <td> <span>{{record[1]}}</span> </td>    
          <td> <span>{{record[2]}}</span> </td>    
        </tr>    
      </tbody>    
    </table>     
  `,
})  
export class AppComponent {
  public headers: any = []; 
  public records: any = []; 
  public csvUrl = 'assets/wine.csv';

  constructor(@Inject(HttpClient) public http:HttpClient) {
     this.readCsvData (); 
  }

  readCsvData () {
    this.http.get(this.csvUrl, {responseType: 'text'})
      .subscribe(
         data => { this.extractData(data) },
         err => { console.log(err) }
      );
  }

  private extractData(res: any) {
    let csvData = res || '';
    let allTextLines = csvData.split(/\r\n|\n/);

    // headers: Alcohol, Malic acid, class
    this.headers = allTextLines[0].split(',');
    // console.log("headers: "+this.headers)

    let lines = [];

    // skip the header row: start from index 1 
    for (let i=1; i < allTextLines.length; i++) {
       // split content based on comma
       let data = allTextLines[i].split(',');

       if (data.length == this.headers.length) {
           let tarr = [];
           for ( let j = 0; j < this.headers.length; j++) {
               tarr.push(data[j]);
           }
           lines.push(tarr);
       }
    }
    // console.log("lines: "+lines)
    this.records = lines;
  }
}

