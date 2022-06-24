#Any result mirroring a real person is strictly random chance
from datetime import date, datetime, timedelta
import uuid
import random
import string

#dictionaries to pull data from for messages
   #might be moved later on to a db or separate files
################################################################################
sex = {'M','F'}
marital = {'M','S',}
last_names = {'Muir','Smith','Adams','Garland','Meade','Fitzgerald','White','Weir','Johnson','Dalton','Reed','Black','Greene','Nedemyer'}
male_names = {'Fred','Jim','Gary','John','Steve','Wilbur','Aurthur','Mike','Shawn','Richard','William','Bill','Tim'}
female_names = {'Mary','Sabrina','Tracy','Sheena','Miranda','Eileen','Tracy','Katie','Penny','Shauna','Yolanda','Yvonne','Carrie'}
race = {'AI','NH','B','U','W','A','O'}
street = {'Ford St.','Sunshine Lane','Seasame St.','Main St.','Delphi Cres.', 'Miller Ln.', 'Younge St.', 'Main Rd.', 'First Ave', 'Oak St.'}
city = {'Smithville','Culver City','Johnstown','Blundersburg','New City','Smallsville','Cedar Springs','Dogwood','Spring Valley','Pine Hill'}
state= {'CA','OR','WA','ID','NV','MN','AZ','NM','WY','CO'}
relation = {'Grandchild','Second Cousin','First Cousin','Sibling','Parent','Guardian','Uncle','Aunt','Spouse'}
adt_event = {'A01', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08'}
facility = {'Lab','ER','Clinic','Oncology','MedSurg','ICU'}
application = {'Epic', 'Allscripts', 'Cerner','Expanse','Magic','CPSI','eCW'}
event_reason = {'01','02','03','O','U'}
clerk_id = {'0341','4321','4564','3478','0199','0002','4532','2341'}
################################################################################

#creates MSH segment
def createMSH(event,time,application):
   MSH=[]
   MSH_string=""
   MSH.insert(1,"")
   MSH.insert(2,"^~\&")
   MSH.insert(3,"adt-gen")
   MSH.insert(4,"%s"%(application))
   MSH.insert(5,"HL7 ETL")
   MSH.insert(6,'hl7-rdb')
   MSH.insert(7,time)
   MSH.insert(8,"")
   MSH.insert(9,"ADT^%s"%(event))
   MSH.insert(10,str(uuid.uuid4())[:8])
   MSH.insert(11,str(uuid.uuid1())[:4])
   MSH.insert(12,'2.5')
   
   for x in range(1,len(MSH)):
      MSH_string += (MSH[x] + "|")

   return(print("MSH|" + MSH_string))

#create EVN segment
def createEVN(event,time,reason, id, event_time, event_facility):
   EVN=[]
   EVN_string=""
   EVN.insert(1,event)
   EVN.insert(2,time)
   EVN.insert(3,time)
   EVN.insert(4,"%s"%(reason))
   EVN.insert(5,id)
   EVN.insert(6,event_time)
   EVN.insert(7,event_facility)
   
   for x in range(1,len(EVN)):
      EVN_string += (EVN[x] + "|")

   return(print("EVN|" + EVN_string))

#creates PID segment
def createPID(sex,last,first,middle,dob,race,address,phone,marital):
   PID=[]
   PID_string=""
   PID.insert(1,"1")
   PID.insert(2,"")
   PID.insert(3,str(random.randint(pow(10, 7-1), pow(10, 7) - 1)))
   PID.insert(4,"")
   PID.insert(5,"%s^%s^%s"%(last,first,middle))
   PID.insert(6,"")
   PID.insert(7,dob)
   PID.insert(8,sex)
   PID.insert(9,"")
   PID.insert(10,race)
   PID.insert(11,address)
   PID.insert(12,"US")
   PID.insert(13,phone)
   PID.insert(14,"")
   PID.insert(15,"")
   PID.insert(16,marital)
   PID.insert(17,"")
   PID.insert(18,"")
   PID.insert(19,"")
   PID.insert(20,"")
   
   for x in range(1,len(PID)):
      PID_string += (PID[x] + "|")

   return(print("PID" + PID_string))

#creates NK1 segment
def createNK1(last,first,middle,relation,address,phone):
   NK1=[]
   NK1_string=""
   NK1.insert(1,"1")
   NK1.insert(2,"%s^%s^%s"%(last,first,middle))
   NK1.insert(3,relation)
   NK1.insert(4,address)
   NK1.insert(5,phone)
   NK1.insert(6,"")
   NK1.insert(7,"")
   NK1.insert(8,"")
   NK1.insert(9,"")
   
   for x in range(1,len(NK1)):
      NK1_string += (NK1[x] + "|")

   return(print("NK1|" + NK1_string))
"""
PV1|1|E|ER^^^.|EM|||1396088571^SMITH^JOHN^^^^MD|||||||EME||Y|||35001346|MCR|||||||||||||||||||.|||||202206232008||||||||1649274275^SMITH^JOHN^^^^DO
"""

#segemnt function inputs
message_event = random.choice(tuple(adt_event))
message_time = str(datetime.now().strftime("%Y%m%d%H%M%S"))
message_reason = random.choice(tuple(event_reason))
message_clerk = random.choice(tuple(clerk_id))
message_application=random.choice(tuple(application))
event_facility = random.choice(tuple(facility))
event_time = str(
   (datetime.now()-timedelta(minutes = random.randrange(1,999,1))).strftime("%Y%m%d%H%M%S")
)

#creates cohesive patient data so it is cohesive across params
def createPatient():
   patient_sex=random.choice(tuple(sex))
   patient_last=random.choice(tuple(last_names))

   if patient_sex == 'M':
      patient_first=random.choice(tuple(male_names))
   else:
      patient_first=random.choice(tuple(female_names))
   
   patient_middle=random.choice(string.ascii_uppercase)
   patient_dob=str((date.today()-timedelta(days = random.randrange(300,29950,1)
      )).strftime("%Y%m%d")
   )
   patient_race=random.choice(tuple(race))

   #patient_address components
   patient_street=str(
      random.randrange(1,9999,1)) + " " +random.choice(tuple(street)
   )#not returned
   patient_city=random.choice(tuple(city))#not returned
   patient_state=random.choice(tuple(state))#not returned
   patient_zip=str(random.randrange(10000,99999,1))#not returned
   patient_address="%s^^%s^%s^%s"%(
      patient_street,patient_city,patient_state,patient_zip
   )
   patient_phone="(" +str(random.randrange(100,999,1))+")555-"+str(random.randrange(1000,9999,1))
   patient_marital=random.choice(tuple(marital))


   return patient_sex,patient_last,patient_first,patient_middle,patient_dob, patient_race,patient_address,patient_phone,patient_marital

#create patient details
patient_sex,patient_last,patient_first,patient_middle,patient_dob,patient_race,patient_address,patient_phone,patient_marital = createPatient()

#create cohesive nk data in line with patient
def createNextofKin(patient_last):
   nk_street=str(
      random.randrange(1,9999,1)) + " " +random.choice(tuple(street)
   )#not returned
   nk_city=random.choice(tuple(city))#not returned
   nk_state=random.choice(tuple(state))#not returned
   nk_zip=str(random.randrange(10000,99999,1))#not returned
   nk_address="%s^^%s^%s^%s"%(
      nk_street,nk_city,nk_state,nk_zip
   )
   nk_sex = random.choice(tuple(sex))#not returned
   nk_last=patient_last

   if nk_sex == 'M':
      nk_first=random.choice(tuple(male_names))
   else:
      nk_first=random.choice(tuple(female_names))
   
   nk_middle=random.choice(string.ascii_uppercase)
   nk_relation=random.choice(tuple(relation))
   nk_phone="(" +str(random.randrange(100,999,1))+")555-"+str(random.randrange(1000,9999,1))

   return nk_address,nk_first,nk_last,nk_middle,nk_relation,nk_phone

#create nk details
nk_address,nk_first,nk_last,nk_middle,nk_relation,nk_phone = createNextofKin(patient_last)

#call functions to print the segments
createMSH(message_event,message_time,message_application)
createEVN(message_event,message_time,message_reason,event_time,message_clerk,event_facility
)
createPID(patient_sex,patient_last,patient_first,patient_middle,patient_dob,patient_race,patient_address,patient_phone,patient_marital
)
createNK1(nk_last,nk_first,nk_middle,nk_relation,nk_address,nk_phone)