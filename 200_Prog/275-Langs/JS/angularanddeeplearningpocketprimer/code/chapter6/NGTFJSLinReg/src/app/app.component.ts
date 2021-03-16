import { Component } from '@angular/core';
import * as tf       from '@tensorflow/tfjs';
// remember: npm install @tensorflow/tfjs -–save

@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.css'],
  template: `
    <h3>Prediction for Value 50:</h3>
    <div id="mydiv">
     {{predict}}
    </div>
  `,
})
export class AppComponent {
  title = 'NGTFJSLinReg';
  public predict = "";
 
  constructor() {
     this.LinearRegression();
  }

  private async LinearRegression(){
     // 1) DEFINE THE MODEL:
     const model = tf.sequential();
 
     model.add(
       tf.layers.dense({
           units:1,
           inputShape:[1]
       })
     );
 
     // 2) COMPILE THE MODEL:
     // specify the loss, optimizer, and metrics:
     model.compile({
        loss:'meanSquaredError',
        optimizer: 'sgd',
        metrics: ['mse']
     });
 
     // 3) FIT/TRAIN THE MODEL:
     // y = 2*x+1 (relationship between xs and ys)
     const xs = tf.tensor1d([1,2,3,4,5,6,7,8,9,10]);
     const ys = tf.tensor1d([3,5,7,9,11,13,15,17,19,21]);
     await model.fit(xs, ys, {epochs:100});
 
     // 4) MAKE SOME PREDICTIONS 
     // 4a) PREDICT Y for X=50:
     var mydiv = document.getElementById('mydiv');
     mydiv.innerText += model.predict(tf.tensor1d([50]));
  }
}

