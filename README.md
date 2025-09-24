# vision
This is a small python script that filters incoming messages for ones with a command prefix, interprets those commands, and then sends the required response. For example it might receive the message `!temp 2000` and send back `the local forecast is a high of 65 fahrenheit for 20:00`.

# notes
right now I'm not sure exactly what a text message dictionary looks like. I'm trying to find the format somewhere but it's difficult and the documentation says just wait for one to come through and look at it. I have a logged telemetry packet but I also need an explanation of the fields. I also need to figure out how to keep the script listening since the listeners are asynchronous and the script just reaches end of execution otherwise.

the message field we need is `"text"`