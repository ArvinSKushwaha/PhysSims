void setup()
{
  size(1600, 800);
  background(255);
}



void plot(float x, float y)
{
  x = x*plotScaleX + 3 * width/4;
  y = height/2 - y*plotScaleY;
  //println(x);
  //println(y);
  point(x, y);
} 
float plotScaleX = (width);
float plotScaleY = (height);
color[] colors = {color(0), color(0, 0, 255), color(255, 0, 0)};
float[] angle1s = {1, 1.000001, 1.0001};
float[] angle2s = {-2, -2, -2};
float[] p1s = {0, 0, 0};
float[] p2s = {0, 0, 0};
float[] dt1s = {0, 0, 0};
float[] dt2s = {0, 0, 0};
float l = 175;
float m = 1;
float dt = 1e-5;
float g = 10;

void draw()
{
  stroke(0);
  line(width/2, 0, width/2, height);
  fill(0);
  textSize(50);
  text("Angle 1", width - 200, height - 25);
  text("Angle 2", width/2 + 20, 50);
  noStroke();
  fill(255);
  rect(-1, -1, width/2, height);
  for(int ml = 0; ml < angle1s.length; ml++)
  {
    stroke(colors[ml]);
    fill(255);
    line(width/4, height/2, width/4 + l * sin(angle1s[ml]), height/2 + l * cos(angle1s[ml]));
    circle(width/4 + l * sin(angle1s[ml]), height/2 + l * cos(angle1s[ml]), 10);
    line(width/4 + l * sin(angle1s[ml]), height/2 + l * cos(angle1s[ml]), width/4 + l * sin(angle1s[ml]) + l * sin(angle2s[ml]), height/2 + l * cos(angle1s[ml]) + l * cos(angle2s[ml]));
    circle(width/4 + l * sin(angle1s[ml]), height/2 + l * cos(angle1s[ml]), 10);
    circle(width/4 + l * sin(angle1s[ml]) + l * sin(angle2s[ml]), height/2 + l * cos(angle1s[ml]) + l * cos(angle2s[ml]), 10);
    fill(255, 5);
    stroke(0);
    rect(width/2-1, -2, width, height);
    stroke(colors[ml]);
    for(int i = 0; i < 20000; ++i)
    {
      p1s[ml] += -0.5 * m * l * l * (dt1s[ml] * dt2s[ml] * sin(angle1s[ml]  - angle2s[ml]) + 3 * g/l * sin(angle1s[ml])) * dt;
      p2s[ml] += -0.5 * m * l * l * (-dt1s[ml] * dt2s[ml] * sin(angle1s[ml]  - angle2s[ml]) + g/l * sin(angle2s[ml])) * dt;
      dt1s[ml] = 6 * (2 * p1s[ml]  - 3 * cos(angle1s[ml] - angle2s[ml]) * p2s[ml]) / (m * l * l * (16 - 9 * pow(cos(angle1s[ml] - angle2s[ml]), 2)));
      dt2s[ml] = 6 * (8 * p2s[ml]  - 3 * cos(angle1s[ml] - angle2s[ml]) * p1s[ml]) / (m * l * l * (16 - 9 * pow(cos(angle1s[ml] - angle2s[ml]), 2)));
      angle1s[ml] += dt1s[ml] * dt;
      angle2s[ml] += dt2s[ml] * dt;
      if(i % 1000 == 0)
      {
        plot(angle1s[ml], angle2s[ml]);
      }
    }
    if(angle1s[ml] > PI)
    {
      angle1s[ml] -= TWO_PI;
    }
    if(angle1s[ml] < -PI)
    {
      angle1s[ml] += TWO_PI;
    }
    if(angle2s[ml] > PI)
    {
      angle2s[ml] -= TWO_PI;
    }
    if(angle2s[ml] < -PI)
    {
      angle2s[ml] += TWO_PI;
    }
  }
  strokeWeight(3);
}
