SHOW DATABASES;
CREATE DATABASE PETPALS;
SHOW DATABASES;
USE PETPALS;

CREATE TABLE PETS(PetID INT PRIMARY KEY, Name VARCHAR(20), Age INT, Breed VARCHAR(20),Type VARCHAR(20),
AvailableForAdoption bit(1));
DESC PETS;

CREATE TABLE SHELTERS(ShelterID INT PRIMARY KEY, Name VARCHAR(20), Location VARCHAR(30));
DESC SHELTERS;

CREATE TABLE DONATIONS(DonationID INT PRIMARY KEY, DonorName VARCHAR(20), DonorType VARCHAR(20),
DonationAmount DECIMAL(10,2),DonationItem VARCHAR(20), DonationDate date);
DESC DONATIONS;

CREATE TABLE AdoptionEvents(EventID INT PRIMARY KEY, EventName VARCHAR(20),EventDate datetime,
Location VARCHAR(30));
DESC ADOPTIONEVENTS;

CREATE TABLE PARTICIPANTS(ParticipantID INT PRIMARY KEY, ParticipantName VARCHAR(20),
ParticipantType VARCHAR(20), EventID int, foreign key(EventID) references AdoptionEvents(EventID));
DESC PARTICIPANTS;

INSERT INTO PETS VALUES(1,"Molly",2,"German Shephard","Dog",1),(2,"Jolly",1,"Labrador","Dog",0),
(3,"Olivia",2,"cat breed 1","cat",1),(4,"Rox",2,"breed1","Turtle",1),
(5,"Benson",2,"cat breed 2","cat",0);
select * from pets;

INSERT INTO SHELTERS VALUES(1,"SHELTER 1","California"),(2,"SHELTER 2","LA"),
(3,"SHELTER 3","New Mexico"),(4,"SHELTER 4","New York"),(5,"SHELTER 5","Miami");
select * from shelters;

INSERT INTO donations values(1,"Alex","Cash",1200,"cash","2023-12-5");
INSERT INTO donations values(2,"hanma","Item",1500,"clothes","2023-12-6");
INSERT INTO donations values(3,"Kumar","Cash",1100,"cash","2023-12-7");
INSERT INTO donations values(4,"Singh","Item",1200,"medicines","2023-12-8");
INSERT INTO donations values(5,"Richard","Cash",1800,"cash","2023-12-9");
select * from donations;

INSERT INTO Adoptionevents VALUES(1,"Event 1","2023-12-6","LA"),(2,"Event 2","2023-12-7","California"),
(3,"Event 3","2023-12-8","NewYork"),(4,"Event 4","2023-12-9","LA"),(5,"Event 5","2023-12-10","NewMexico");
select * from adoptionevents;

INSERT INTO Participants values(1,"Alex","Shelter",1),(2,"Hanma","Adopter",2),(3,"Tom","Shelter",3),
(4,"Hanks","Adopter",4),(5,"Steve","Shelter",5);
select * from participants;

/* 5 */
select * from pets where AvailableForAdoption=1;

/*6*/
SET @EventID = 5; 
SET @EventID = 2; 
SELECT P.ParticipantName, P.ParticipantType
FROM PARTICIPANTS P
INNER JOIN AdoptionEvents AE ON P.EventID = AE.EventID
WHERE P.EventID = @EventID;

/* 7*/
UPDATE shelters SET Name = "5 Shelter", location="India" WHERE ShelterID = 5;
select * from shelters;

/*7*/
create procedure updateshelterInfo(
IN shelterIDparam INT,
IN newName VARCHAR(100),
IN newLocation varchar(255),
out resultmessage varchar(255))
begin declare shelterexists int 
select count(*) into  shelterexists from shelters where shelterid=shelterIDparam;
if shelterexists=0 then 
set resultmessage = 'Invalid shelter ID. shelter does not exist.'
else
 begin update shelters
 set name = newName,location=newLocation
 where shelterID = shelterIDparam;
 set resultmessage='shelter information updated successfully';
 end;
 end if;
 end


/* 8 */
select s.name as shelter_name, d.DonationAmount as Amount
from shelters s, donations d;

/* 9 */
select Name as Pet_name, Participants.name as owner_name
 from pets, participants;
 
/*10*/
SELECT MonthYear, SUM(DonationAmount) AS TotalDonationAmount
FROM (SELECT DATE_FORMAT(DonationDate, "12-2023") AS MonthYear, DonationAmount
FROM DONATIONS) AS MonthYearDonations
GROUP BY MonthYear
ORDER BY MIN(DonationDate);

/*11*/
SELECT DISTINCT breed
FROM pets
WHERE (age BETWEEN 1 AND 3) OR (age > 5);

/*12*/
SELECT p.pet_name, p.breed, s.shelter_name
FROM pets p
JOIN shelters s ON p.shelter_id = s.shelter_id
WHERE p.AvailabilityForAdoption = 'available';

/*13*/
SELECT COUNT(ep.participant_id) AS total_participants
FROM events e
JOIN shelters s ON e.shelter_id = s.shelter_id
JOIN event_participants ep ON e.event_id = ep.event_id
WHERE s.city = 'Bhopal';

/*14*/
SELECT DISTINCT breed
FROM pets
WHERE (age BETWEEN 1 AND 5);

/*15*/
select * from pets where AvailableForAdoption=0;

/*16*/
SELECT P.Name AS PetName, PA.ParticipantName AS AdopterName
FROM PETS P
INNER JOIN PARTICIPANTS PA ON P.AvailableForAdoption = 0
AND P.PetID = PA.EventID;

/*17*/
SELECT S.Name AS ShelterName, COUNT(P.PetID) AS PetsAvailableForAdoption
FROM SHELTERS S
LEFT JOIN PETS P ON S.ShelterID = P.AvailableForAdoption
WHERE P.AvailableForAdoption = 1 OR P.AvailableForAdoption IS NULL
GROUP BY S.ShelterID, S.Name;

/*18*/
SELECT p1.PetID AS PetID1,p1.Name AS Name1,p1.Breed AS Breed,
p1.Type AS Type, p1.AvailableForAdoption AS AvailableForAdoption1, p2.PetID AS PetID2,p2.Name AS Name2,
p2.Type AS Type2,p2.AvailableForAdoption AS AvailableForAdoption2,s.Name AS ShelterName
FROM PETS p1
INNER JOIN PETS p2 ON p1.Breed = p2.Breed
AND p1.PetID < p2.PetID 
INNER JOIN SHELTERS s ON p1.AvailableForAdoption = p2.AvailableForAdoption
AND p1.ShelterID = s.ShelterID
WHERE p1.ShelterID = p2.ShelterID
AND p1.PetID != p2.PetID
ORDER BY s.Name, p1.Breed, p1.PetID, p2.PetID;

/*19*/
SELECT S.ShelterID AS ShelterID,S.Name AS ShelterName,
AE.EventID AS EventID,AE.EventName AS EventName
FROM SHELTERS S
CROSS JOIN ADOPTIONEVENTS AE
ORDER BY S.ShelterID, AE.EventID;

/*20*/
SELECT S.ShelterID,S.Name AS ShelterName,COUNT(P.PetID) AS AdoptedPetsCount
FROM SHELTERS S
LEFT JOIN PETS P ON S.ShelterID = P.AvailableForAdoption
WHERE P.AvailableForAdoption = 1
GROUP BY S.ShelterID, S.Name
ORDER BY AdoptedPetsCount DESC
LIMIT 1;
















