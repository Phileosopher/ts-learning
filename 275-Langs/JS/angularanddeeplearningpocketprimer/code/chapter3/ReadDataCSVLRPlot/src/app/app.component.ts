import { Component }  from '@angular/core';  
import { Inject }     from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({  
  selector: 'app-root',  
  styleUrls: ['./app.component.css'],
  template: `
    <svg width="600" height="200">
      <rect x="0" y="0" width="600" height="200" 
            stroke="black" stroke-width="4" fill="white" />
      <polyline [attr.points]="polyPts"
                style="fill:none;stroke:red;stroke-width:4" />
    </svg> 
    <table> 
      <tbody>    
        <p>Data points for this line graph:</p>
        <tr *ngFor="let record of records;let i = index;">    
          <td> <span>{{record[0]}}</span> </td>    
          <td> <span>{{record[1]}}</span> </td>    
        </tr>    
      </tbody>    
    </table>     
  `,
})  
export class AppComponent {
  public xValue:number   = 0;
  public yValue:number   = 0;

  // points for an SVG polyline 
  public polyPts : any = ""; 

  // populate an array with CSV data 
  public records : any = []; 
  public csvUrl  = 'assets/rand20.csv';
  public allTextLines:any = "";

  constructor(@Inject(HttpClient) public https:HttpClient) {
     this.readCsvData (); 
  }

  readCsvData () {
    this.http.get(this.csvUrl, {responseType: 'text'})
      .subscribe(
         data => { this.extractData(data) },
         err => { console.log(err) }
      );
  }

  //---------------------------------------------------
  // After the readCsvData reads the CSV file in the 
  // assets directory, the extractData method is invoked 
  // in order to populate an array with that CSV data. 
  // This method also invokes constructLineGraph that 
  // constructs a line graph of the set of datapoints 
  //---------------------------------------------------
  private extractData(res: any) {
    let csvData = res || '';
    this.allTextLines = csvData.split(/\r\n|\n/);

    let lines = [];
    let onerow = this.allTextLines[0].split(',');
    let columnCount = onerow.length;
     
    for ( let i = 0; i < this.allTextLines.length-1; i++) {
       // split content based on comma
       let data = this.allTextLines[i].split(',');

       let tarr = [];
       for ( let j = 0; j < columnCount; j++) {
          tarr.push(data[j]);
       }
       lines.push(tarr);
    }
    this.records = lines;

    this.constructLineGraph();
  }

  private constructLineGraph() {
    // construct a line graph 
    for ( let i = 0; i < this.records.length; i++) {
     //console.log("this.xValue:",  this.records[i][0]);
     //console.log("this.yValue:",  this.records[i][1]);

       // append current point to the SVG polyline:
       this.polyPts += this.xValue.toString() + "," + 
                       this.yValue.toString() + " ";

       this.xValue += +this.records[i][0];
       this.yValue = +this.records[i][1];
    }
  }
}

