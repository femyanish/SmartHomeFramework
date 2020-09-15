# SmartHomeFramework
____________________

	SmartHomeFramework is a IoT based web application through which we connect hardware devices of home appliances like washing machine/dryer/ dish washer to the backend and managed by web and Mobile applications. These devices are controlled online through IoT using Raspberry pi controller. The customer uses these devices at home and pays the bill according to their usage. The real-time usages of these devices are stored in the customer’s usage history and paid accordingly.  So, each time the status of the devices will be sent as a message to the registered customers.


# The requirements of SmartHomeFramework are:

•The customer or user registers through the website by ordering the home appliances Washing machine, Dryer & Dishwasher. The customer details are validated at the backend.  
•The connection of the Smart Home Framework  with the customer is established for the home appliances he/she ordered.
•The appliances are delivered to the customer on rental as “Pay per Use” basis.
•Connection between the home appliances and the mobile app are provided.
•As customer uses the home appliances, they will be charged based on their usage and online payment initiated.

    Throughout the above scenarios with Python as the main scripting language, MQTT messaging protocol and Raspberry Pi are used to connect the home appliances (like washing machine, Dryer & Dishwasher) to the mobile app through Internet of Things.  MQTT stands for Message Queuing Telemetry Transport. It is a lightweight publish and subscribe system where you can publish and receive messages as a client. MQTT is a simple messaging protocol, designed for constrained devices with low-bandwidth. In this way the above software stack satisfies to fulfil the requirements

 # Software to Install

1.	Python 38-32.
2.	VS source or PyCharm tool. 
3.	Mosquitto Broker or Server - mosquitto-1.6.12-install-windows-x64.
4.	Linux Ubuntu.
5.	Windows 10 Home Edition.
6.	SQLite Database.



# The components of the SmartHomeFramework are:

1.	Server Application.
2.	Web Application.
3.	Home Appliance (simulating in program).
4.	Mobile Phone Application.
5.	Database Server.

# SmartHomeFramework works based on the MQTT protocol - 
MQTT is a publish/subscribe protocol that allows edge-of-network devices to publish to a broker based on the Topics. Clients connect to this broker, which then mediates communication between the two devices. When another client publishes a message on a subscribed topic, the broker forwards the message to any client that has subscribed.

# MQTT Messages: 

MQTT messages which are communicated among user like Home Appliance and the Server, their structure and how they are built is shown below. Topics and Messages are combined together and send for communication. Different Topics are formulated, few of them are

	Status
	Login &
	<Machine ID>Login Response

1. Send the regular status HomeAppliance->Broker
2. Send login request HomeAppliance->Broker
3. Send login Response Server->Broker->HomeAppliance
4. List of Programs Server->Broker->HomeAppliance
5. Washing Status Change HomeAppliance->Broker

Device Types for: 
1.	Washing machine - 1
2.	Dryer - 2
3.	Dish Washer - 3


# General Communication between Server and Home Appliance.

MQTT Client is the Python program uses paho.mqtt.client library which acts as an MQTT broker for the mosquito broker (we are using).
The communcation betweet server and Home Appliances happens through following programs.
MQTT Client
Protocol Encoder
Server
Protocol Decoder
Washing Machine

######### 		CONTRIBUTORS          ################################

Ashwini <abiradar9@googlemail.com>
Femy  <femyanish@gmail.com>
Padma  <padmavathi.vempadi@gmail.com>
Varsha  <varshanijampure@gmail.com>
