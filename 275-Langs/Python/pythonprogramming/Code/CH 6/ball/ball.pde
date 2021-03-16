// Bouncing ball sim

float ballHeight = 12;  // Feet
float ballE = 0.5;      // Elasticity
float balla = 32.0;     // Acceleration (=G)
float ballSpeed = 0;    // Down is +, ft per sec.
float dt = 0.1;         // Time interval, sampling
float ppf = 12;

void setup ()
{
  size (200, 500);
  frameRate (15);
}

void draw ()
{
float startHeight, startSpeed;
float s, xt;
int ys = 30, xs = 100;
    background(128);
        startHeight = ballHeight;
        startSpeed = ballSpeed;
        s = 0.5*balla*dt*dt + ballSpeed*dt;
        ballHeight = ballHeight - s;
        ballSpeed = ballSpeed + balla*dt;
        if (ballHeight < 0)       // The sign changed; when?
        {
          xt = (-startSpeed - sqrt(startSpeed*startSpeed +2*balla*startHeight))/balla;
          if (xt < 0)
                xt = (-startSpeed + sqrt(startSpeed*startSpeed +2*balla*startHeight))/balla;
          println ("Bounces at time "+ xt);
          ballSpeed = -(ballSpeed + balla*xt)*ballE;
          ballHeight = -ballHeight * ballE;
          if (ballE <0.03) ballE = 0.0;
            else ballE = ballE - 0.03;
         } else if(startSpeed*ballSpeed < 0)                  // Ball peaks and falls again
         {
            xt = (-startSpeed - sqrt(startSpeed*startSpeed +2*balla*startHeight))/balla;
            if (xt < 0)
                xt = (-startSpeed + sqrt(startSpeed*startSpeed +2*balla*startHeight))/balla;
            ballSpeed = 0;
//            ballHeight = ballHeight - 0.5*balla*xt*xt;
            println ("Peak");
          }
          println ("New speed is "+ballSpeed+ " and height starts at "+ ballHeight);
        if (ballHeight < 0) ballHeight = 0;
        line (xs-5, ys, xs-5, ys+12*ppf);
        ellipse (xs, ys+12*ppf - ballHeight*ppf, 5, 5);
        text ("Height "+ballHeight, xs+6, ys+12*ppf);
        text ("Speed is "+ballSpeed, xs+6, ys+12*ppf +15);
}
        

