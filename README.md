# CSC423-Final-Project
This database final project was assigned in CSC 423 by [Vanessa Aguiar-Pulido](https://vaguiarpulido.github.io/). Three projects were given and each student was tasked with doing one. I was assigned Case Study 2

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

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/651fad71-074a-418b-9230-b145882efd3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T095750Z&X-Amz-Expires=86400&X-Amz-Signature=8c07af72e1c816e9b24ddd3f80883e3206a7ac3d9b45349aecdcf4371abaf4b8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## Cardinality Constraints

- **Client requires Service**
    - A client requires a services (1..*)
    - A service is required by one client (1..1)
- **Service determines Equipment**
    - A service determines the amount of equiment used (1..*)
    - If needed, a special equipment is required for services (0..*)
- **Employees performs a Service**
    - An Employee perform multiple services (1..*)
    - A service is performed by mutliple employees (1..*)

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6f2e8833-df9f-456d-8ca9-76e198cfb3fd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T095958Z&X-Amz-Expires=86400&X-Amz-Signature=833840ab87a6291da22a4d7ca6f9cccfe594bff2756dffb66ba39f3690a3cafb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9035e752-c400-413b-929e-e9046464b094/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T100035Z&X-Amz-Expires=86400&X-Amz-Signature=7df3f52ddbbbcf7db2d11aecb72cdfb1a2016395e2b105eeadaea70b3ef3985f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## Attributes

***Implementation***

- Client requires Service
    - Client (**client number**, first name, last name, address,  telephone number)
    - Service (**client identifier**, client name, start day, end day, start time, end time)
- Service determines Equipment
    - Service  (**serviceNo**, start day, end day, start time, end time)
    - Equipment (**equipment identifier**, description, usage, cost)
- Employees performs Service
    - Employee (**staff number**, first name, last name, address, salary, and telephone number)
    - Service  (**serviceNo**, start day, end day, start time, end time)

***Assumptions***

- Equipments are special and may or may not be determined for a given service
- Services do not require Equipment hence any attempt to use the logic of Service requires Equipment or vice versa will render the multiplicities innaccurate

## Candidate and Primary Keys

- Client (**client number**, first name, last name, address, telephone number)
    - Primary key: client number
    - Candidate key: client number, telephone number
- Employee (**staff number**, first name, last name, address, salary, and telephone number)
    - Primary key: staff number
    - Candidate key: staff number, telephone number
- Equipment (**equipment identifier**, description, usage, cost)
    - Primary key: equipment identifier
    - Candidate key: equipment identifier, description

    (Equipment are assumed to perform unique roles for efficiency)

- Service  (**serviceNo**, start day, end day, start time, end time)
    - Primary key: serviceNo
    - Candidate key: serviceNo

---

# Logical Data Model

## Derived relations from the conceptual model.

We give each attribute a unique name to prevent data from being misplaced. Additionally, for adjacent one-to-many relationships or zero-to-many relationships we will draw tables for the relations involved. These relations will include the parent keys from adjacent entities.

## Normalization

- **1NF (Flattening the UNF Table)**

    Since tables were determined in the conceptual model, we can represent them in 1NF form

    - Clients(**clientNo**, cFirstName, cLastName, cAddress, cTeleNum)
    - Employees(**empNo ,**eFirstName, eLastName, eAddress, salary, eTeleNum)
    - Equipment(**eqID** ,desc, usage, cost)
    - Service (**serviceNo**,startDay, endDay, startTime, endTime)
    - Perfoms (**serviceNo, empNo**, hours)
    - Determines (**serviceNo, eqID**, lastUseDate, lastServiceDate)

    **Functional Dependencies**

    **clientNo** > cFirstName, cLastName, cAddress, cTeleNum

    **empNo**> eFirstName, eLastName, eAddress, salary, eTeleNum 

    **eqID** >  desc, usage, cost 

    **serviceNo** > startDay, endDay, numHours 

    **serviceNo, empNo >** hours

    **serviceNo, eqID >** lastUseDate, lastServiceDate

- **2NF (Make new tables based on the partial dependencies identified)**

    No partial dependencies were identified so no new tables are made. 

    - Clients(**clientNo**, cFirstName, cLastName, cAddress, cTeleNum)
    - Employees(**empNo ,**eFirstName, eLastName, eAddress, salary, eTeleNum)
    - Equipment(**eqID** ,desc, usage, cost)
    - Service (**serviceNo**,startDay, endDay, startTime, endTime)
    - Perfoms (**serviceNo, empNo**, hours)
    - Determines (**serviceNo, eqID**, lastUseDate, lastServiceDate)
- 3NF (Removal of Transitive Dependencies, Putting those dependencies in individual table)

    No transitive dependencies were identified so no new tables are made. 

    - Clients(**clientNo**, cFirstName, cLastName, cAddress, cTeleNum )
    - Employees(**empNo ,**eFirstName, eLastName, eAddress, salary, eTeleNum)
    - Equipment(**eqID** ,desc, usage, cost)
    - Service (**serviceNo**,startDay, endDay, startTime, endTime)
    - Perfoms (**serviceNo, empNo**, hours)
    - Determines (**serviceNo, eqID**, lastUseDate, lastServiceDate)

    **Since Services table has a one to many relationship with Client it will have one foreign key**

    - Service (**serviceNo**,startDay, endDay, startTime, endTime, clientNo)

    The relationship tables help to manage entity relationship since they contain the primary keys of their adjacent tables

    From the above, we can conlude that our table is already in 3NF form hence we can proceed to the implementation phase of the project

## Validating Against User Transactions
Reference the Busy Bee PDF
## Constraints

**Integrity constraints**

i.	**Primary key constraints.**

- Primary keys for each entity cannot be null and must be unique for each value

ii.     **Referential integrity/Foreign key constraints.**

- If a foreign key contains a value, that value must refer to an existing tuple in the parent relation

iii.	**Alternate key constraints (if any).**

- No alternate keys were determined as of this implementation

iv.	**General constraints (if any).**

- Services must start and end in the future, not in the past
- A service can only be stated by one client
- The end day must be greater than start day for Services.
- The end time must be greater than the start time
- Equipment description and usage are unique values for the purpose of efficiency
- Company names will occupy the First Name column and the word "Company" will occupy the last in situations where a company is the known client
- Telephone number must be less than 16 digits long
- Cleaning services are not offerred on weekends
- Days of the week are represented as letters

## Final Implementation

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b7086a86-0113-4e8b-9909-3439df62f1c6/ER_Diagrams-ER_Diagrams_2_%28Landscape%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T101437Z&X-Amz-Expires=86400&X-Amz-Signature=1ff4ebf07f990c262656f46b6709a7d1131d7db4ed8681187735a30ca197c801&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22ER_Diagrams-ER_Diagrams_2_%28Landscape%29.jpg%22)

# Oracle DBMS Implementation

`BusyBee.sql`

```sql
--Uncomment Drop tables if tables already exist
--DROP TABLE DETERMINES;
--DROP TABLE PERFORMS;
--DROP TABLE EQUIPMENT;
--DROP TABLE SERVICE;
--DROP TABLE EMPLOYEE;
--DROP TABLE CLIENT;

--Client Table
CREATE TABLE Client
 (
  clientNo INT,
  cFirstName VARCHAR(100) ,
	cLastName VARCHAR(100),
  cAddress VARCHAR(100),
	cTeleNum INT CHECK (LENGTH(cTeleNum) < 16),
  PRIMARY KEY(clientNo)
);

-- Employee Table
CREATE TABLE Employee
 (
  empNo INT,
  eFirstName VARCHAR(100) ,
	eLastName VARCHAR(100),
  eAddress VARCHAR(100),
	salary INT ,
	eTeleNum VARCHAR(100) CHECK (LENGTH(eTeleNum) < 16),
  PRIMARY KEY(empNo)
);

--Service Table
CREATE TABLE Service
 (
	serviceNo INT,
  startDay VARCHAR(100) CHECK(startDay IN ('M', 'T', 'W','TH', 'F')),
	endDay VARCHAR(100) CHECK(endDay IN ('M', 'T', 'W','TH', 'F')),
  startTime DATE,
	endTime DATE,
	clientNo INT,
  empNo INT,
  PRIMARY KEY(serviceNo),
	CONSTRAINT SVAL CHECK (endTime > startTime),
	FOREIGN KEY (clientNo) REFERENCES Client(clientNo) ON DELETE SET NULL
);

-- Equipment Table
CREATE TABLE Equipment
 (
  eqID INT,
	descp VARCHAR(300),
	usage INT,
	cost INT,
  serviceNo INT,
PRIMARY KEY(eqID)
);

-- Performs Table
CREATE TABLE Performs
(
serviceNo INT,
empNo INT,
hours INT,
PRIMARY KEY(serviceNo, empNo),
FOREIGN KEY (serviceNo) REFERENCES Service(serviceNo) ON DELETE SET NULL,
FOREIGN KEY (empNo) REFERENCES Employee(empNo) ON DELETE SET NULL
);

-- Determines Table
CREATE TABLE Determines
(
serviceNo INT,
eqID INT,
lastUseDate DATE,
lastServiceDate DATE,
PRIMARY KEY(serviceNo, eqID),
FOREIGN KEY (serviceNo) REFERENCES Service(serviceNo) ON DELETE SET NULL,
FOREIGN KEY (eqID) REFERENCES Equipment(eqID) ON DELETE SET NULL
);

```

```sql
INSERT INTO CLIENT VALUES(1,'Patrick','Nutall','1230 Hemingway Avenue',3067894328);
INSERT INTO CLIENT VALUES(2,'The Cardboard Box','Company','114 Stanford Heights',2134874680);
INSERT INTO CLIENT VALUES(3,'Jerry','Jones','698 South Parkway',2067204328);
INSERT INTO CLIENT VALUES(4,'Dantey','Tope','1621 Dawn Terrace',3094328234);
INSERT INTO CLIENT VALUES(5,'Pogba','Paul','1230 Hemingway Avenue',3054986903);
INSERT INTO CLIENT VALUES(6,'Terry','Nero','1615 Schlimgen Crossing',4302099078);
-----------------------------
INSERT INTO EMPLOYEE VALUES(1,'Chadwick','Pollett','8696 Victoria Court',286.67,9167046280);
INSERT INTO EMPLOYEE VALUES(2,'Alexandros','Antunes','9 Alpine Crossing',418.07,8745093029);
INSERT INTO EMPLOYEE VALUES(3,'Averill','Tomblett','34 Shopko Park',48.05,2269440178);
INSERT INTO EMPLOYEE VALUES(4,'Bernard','Pretswell','647 Sauthoff Court',5359.80,6142641343);
INSERT INTO EMPLOYEE VALUES(5,'Claudetta','Caherny','1 Carberry Court',9113.12,9555627427);
INSERT INTO EMPLOYEE VALUES(6,'Richmond','Molesworth','1294 Pawling Place',277.38,4493208964);
-----------------------------
INSERT INTO SERVICE VALUES(1,'M','F',TO_DATE('2020-12-07','YYYY-MM-DD'),TO_DATE('2020-12-11','YYYY-MM-DD'),1,1);
--INSERT INTO SERVICE VALUES(2,'T','Th',TO_DATE('2020-12-08','YYYY-MM-DD'),TO_DATE('2020-12-10','YYYY-MM-DD'),1,2);
INSERT INTO SERVICE VALUES(3,'W','F',TO_DATE('2020-12-09','YYYY-MM-DD'),TO_DATE('2020-12-11','YYYY-MM-DD'),2,2);
INSERT INTO SERVICE VALUES(4,'TH','M',TO_DATE('2020-12-10','YYYY-MM-DD'),TO_DATE('2020-12-13','YYYY-MM-DD'),3,3);
INSERT INTO SERVICE VALUES(5,'F','T',TO_DATE('2020-12-11','YYYY-MM-DD'),TO_DATE('2020-12-15','YYYY-MM-DD'),4,4);
--INSERT INTO SERVICE VALUES(6,'W','Th',TO_DATE('2020-12-16','YYYY-MM-DD'),TO_DATE('2020-12-18','YYYY-MM-DD'),1,2);
INSERT INTO SERVICE VALUES(7,'T','F',TO_DATE('2020-12-22','YYYY-MM-DD'),TO_DATE('2020-12-25','YYYY-MM-DD'),1,1);
--INSERT INTO SERVICE VALUES(8,'F','S',TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'),1,5);
-----------------------------
INSERT INTO EQUIPMENT VALUES(1,'Carpet Cleaner',3,20,1);
INSERT INTO EQUIPMENT VALUES(2,'Mop',2,40,6);
INSERT INTO EQUIPMENT VALUES(3,'Stone Waxer',1,79,6);
INSERT INTO EQUIPMENT VALUES(4,'Buffer',2,89,2);
INSERT INTO EQUIPMENT VALUES(5,'Sulphuric Acid',3,24,2);
INSERT INTO EQUIPMENT VALUES(6,'Oil',3,90,3);
INSERT INTO EQUIPMENT VALUES(7,'Polish',2,89,2);
-----------------------------
INSERT INTO PERFORMS VALUES(1,1,4);
--INSERT INTO PERFORMS VALUES(2,2,4);
INSERT INTO PERFORMS VALUES(3,3,4);
INSERT INTO PERFORMS VALUES(1,2,5);
INSERT INTO PERFORMS VALUES(4,4,3);
INSERT INTO PERFORMS VALUES(5,5,3);
-----------------------------
INSERT INTO DETERMINES VALUES(1,1,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
--INSERT INTO DETERMINES VALUES(2,2,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
INSERT INTO DETERMINES VALUES(3,3,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
INSERT INTO DETERMINES VALUES(5,5,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
INSERT INTO DETERMINES VALUES(1,3,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
INSERT INTO DETERMINES VALUES(1,2,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
--INSERT INTO DETERMINES VALUES(1,2,TO_DATE('2020-12-25','YYYY-MM-DD'),TO_DATE('2020-12-26','YYYY-MM-DD'));
```

## Output

### Client

![alt-text](notion://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5dcb3951-fa5d-4d55-9025-941e0cdaa7ae%2FUntitled.png?table=block&id=9682f2fc-b4f4-44bf-af89-c7d5f9b472d9&width=3070&userId=7bc3442b-f692-408b-8d64-926dcb89e061&cache=v2)

### Employee

![alt-text](notion://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F804bb1b1-c7db-41da-95e7-9da0cbe2718c%2FUntitled.png?table=block&id=0e995c12-669a-4d07-a27e-33ecc715dc18&width=1070&userId=7bc3442b-f692-408b-8d64-926dcb89e061&cache=v2)

### Service

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5c1401d1-3199-4643-ad04-1b4dc4f1fb1c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T101654Z&X-Amz-Expires=86400&X-Amz-Signature=06dc692486f7eac86b636b0e5ddedafdc26df42a15fde1b9669c4ecf6cf9cf15&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### Equipment

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2d87d6c0-2589-4260-a9c6-44e49f8fbf2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T101813Z&X-Amz-Expires=86400&X-Amz-Signature=d10c099a0b1dcd9c16339ab1eafe390d60d0a4ed5e9b46ccca8366d44d9b575e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### Performs

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c4498843-ce16-49ad-871f-f4196b114d8d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T101849Z&X-Amz-Expires=86400&X-Amz-Signature=6d1ee4e4b4165d27dae608f62f741cdfd9057771c924fe2f6cd6dcae6ec0cbda&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### Determines

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/22bea6ce-a3c6-4d3e-bcdb-84291b65aef2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T101955Z&X-Amz-Expires=86400&X-Amz-Signature=261a85bae779139a10ab95b7c1426b3c275d36b168be49e6f701df37663d209e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## Embedded SQL

`connect_oracle.py`

These queries were implemented in Python

```sql
-- Print all Employees
SELECT * FROM EMPLOYEE;

--Print all Clients
SELECT * FROM CLIENT;

--Print all Equipments
SELECT * FROM EQUIPMENT;

-- Print all Services
SELECT * FROM SERVICE;

-- Print Master Table
SELECT *
FROM CLIENT c, SERVICE s, EQUIPMENT e, Determines d 
WHERE(c.clientNo = s.clientNo AND s.serviceNo = d.serviceNo AND d.eqID = e.eqID);
```

Run `connect_oracle.py`  to enjoy the experience

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/39e6afac-82bf-4440-b67e-94b4894f14cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T102025Z&X-Amz-Expires=86400&X-Amz-Signature=e14747cac356a145994055f84566953f936147f053445ba15315164aa752cfe2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

`Sample Test`

![alt-text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f876ba4e-d8fc-48db-acfc-ee251d407ec1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201204T102201Z&X-Amz-Expires=86400&X-Amz-Signature=f9402febcda991c44beba2d703d03ff461a72754607d31a6f7365bf0bd02598f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### Acknowledgements

The above code was implemented and designed by [Isaac Kofi Attuah.](https://isaacattuah.com/)
