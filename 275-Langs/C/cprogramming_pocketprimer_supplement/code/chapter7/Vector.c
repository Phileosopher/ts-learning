#include <stdio.h>
#include <math.h>

// a 2D vector:
typedef struct {
   double x, y;
} vector2D;

// a 3D vector:
typedef struct {
    union {
        struct {
           double x, y;
        };
        vector2D v2;
    };
    double z;
} vector3D;

double length2D (vector2D v){
   return sqrt(v.x*v.x + v.y*v.y);
}

double length3D (vector3D v){
   return sqrt(v.x*v.x + v.y*v.y + v.z*v.z);
}

int main(){
   vector3D v = {.x=5, .y=8, .z=4};
   printf("Vector v:   (%f,%f,%f)\n", v.x,v.y,v.z);
   printf("Magnitude:  %g\n", length3D(v));
   double projected = length2D(v.v2);
   printf("Projection: length of %g\n", projected);

   return 0;
}

