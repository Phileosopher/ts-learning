This sample demonstrates how to integrate a chat application using Redis as message broker

As pre-requisite to this sample, you first need to install Redis.
  https://redis.io/download

To try the sample install the dependencies:
  npm install

Then run (in two separate terminals):
  node app 8081
  node app 8082
  
To access the application open a browser at the address:
  https://localhost:8081

And then at the same time open another browser at the following address:
  https://localhost:8082
