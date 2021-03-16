This sample demonstrates how to distribute the traffic
across multiple servers without the need of a standalone load balancer.
This is a variation of the previous sample, using a service registry.

First install the dependencies:
  npm install

Make sure you have a seaport server running
  seaport listen 9090
  
Start some instances of an api-service server:
  node app api-service
  node app api-service
  
Run the client application with:
  node client
