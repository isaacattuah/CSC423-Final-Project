# CSC423-Final-Project
A database final project based on the BusyBee Cleaning Company

# Case Study 2: BusyBee Cleaning Company

The BusyBee Cleaning Company specializes in providing cleaning services for clients. **Each type of client** has a set of requirements. For example, **The Cardboard Box Company** requires cleaning services from Monday to Friday 7am until 9am and 5pm until 7pm each day, but **P. Nuttall** only requires cleaning services on a Wednesday from 10am until 1pm.

Whenever a new client is taken on, it is determined whether any special equipment is required and when. For example, three industrial floor cleaners may be needed on two out of five occasions for one client. 

Therefore, the following information will be stored for **each equipment**, in addition to the equipment identifier: description, usage, and cost.

For **each employee** the following data will be stored: staff number (uniquely identifies an employee), first and last name, address, salary, and telephone number. For **each client** , the following data will be stored: client number (uniquely identifies a client), first and last name, address, and telephone number.

# Conceptual Model

## **Relations**

- Client (**client number**, first name, last name, address, and telephone number)
- Employee (**staff number**, first name, last name, address, salary, and telephone number)
- Equipment (**equipment identifier**, description, usage, cost)
- Service  (**serviceNo**, start day, end day, start time, end time)

## Relationship Types

- Client requires Service
- Service determines Equipment
- Employees performs a Service

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4597610f-80e7-46fa-ade6-26b340323438/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T095639Z&X-Amz-Expires=86400&X-Amz-Signature=4ac31801b00edaa0ab26c6cdf60ad198be9bc44b0cd42a9e31e28ab4560d9ae5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)
