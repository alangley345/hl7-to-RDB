#Any result mirroring a real person is strictly random chance
from datetime import date, datetime, timedelta
import uuid
import random
import string

#dictionaries to pull data from for messages
   #might be moved later on to a db or separate files 
sex = {'M','F'}
marital = {'M','S',}
last_names = {'Muir','Smith','Adams','Garland','Meade','Fitzgerald','White','Weir','Johnson','Dalton','Reed','Black','Greene','Nedemyer'}
male_names = {'Fred','Jim','Gary','John','Steve','Wilbur','Aurthur','Mike','Shawn','Richard','William','Bill','Tim'}
female_names = {'Mary','Sabrina','Tracy','Sheena','Miranda','Eileen','Tracy','Katie','Penny','Shauna','Yolanda','Yvonne','Carrie'}
race = {'AI','NH','B','U','W','A','O'}
street = {'Ford St.','Sunshine Lane','Seasame St.','Main St.','Delphi Cres.', 'Miller Ln.', 'Younge St.', 'Main Rd.', 'First Ave', 'Oak St.'}
city = {'Smithville','Culver City','Johnstown','Blundersburg','New City','Smallsville','Cedar Springs','Dogwood','Spring Valley','Pine Hill'}
state= {'CA','OR','WA','ID','NV','MN','AZ','NM','WY','CO'}
relation = {'Grandchild', 'Second Cousin', 'Sibling', 'Parent'}
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

   return(print("MSH" + MSH_string))

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

"""
function ran.scrubPID(PID)
   PID[3][1][1] = math.random(9999999)
   ran.NameAndSex(PID)
   PID[5][1][1][1] = ran.lastName()
   PID[7][1] = ran.Date()
   PID[10][1][1] = ran.choose(ran.Race)
   PID[18][1] = ran.AcctNo()
   PID[11][1][3], PID[11][1][4] = ran.location()
   PID[11][1][5] = math.random(99999)
   PID[11][1][1][1] = math.random(999)..
      ' '..ran.choose(ran.Street)
   PID[19] = ran.SSN()
   PID:S()
end
 
function ran.PV1(PV1)
   PV1[8][1][2][1] = ran.lastName()
   PV1[8][1][3] = ran.firstName()
   PV1[8][1][4] = 'F'
   PV1[19][1] = math.random(9999999)
   PV1[44][1] = ran.TimeStamp()
   PV1:S()
end
 
function ran.NK1(NK1)
   for i = 1, math.random(6) do
      NK1[i][1] = i
      ran.Kin(NK1[i])
   end
end
 
function ran.Kin(NK1)
   NK1[2][1][1][1] = ran.lastName()  
   NK1[2][1][2] = ran.firstName()
   NK1[3][1] = ran.choose(ran.Relation)
end
 

 
function ran.lastName() return ran.choose(ran.LastNames) end
 
function ran.choose(T)
   return T[math.random(#T)]
end
 
function ran.NameAndSex(PID)
   if math.random(2) == 1 then
      PID[8] = 'M'
      PID[5][1][2] = ran.choose(ran.MaleNames)
   else   
      PID[8] = 'F'
      PID[5][1][2] = ran.choose(ran.FemaleNames)      
   end
end
 
function ran.firstName()
   if math.random(2) == 1 then
      return ran.choose(ran.MaleNames)
   else   
      return ran.choose(ran.FemaleNames)      
   end
end
 
function ran.Date()
   local T = os.date('*t')
  
   local newDate = '19'..rand(T.year,99,2)..
   rand(T.month,12,2)..
   rand(T.day,29,2)
   
   return newDate
end
 
function ran.TimeStamp()
   local T = os.date('*t')
   
   local newDate = '20'..rand(T.year,tostring(T.year):sub(-2),2)..
   rand(T.month,12,2)..
   rand(T.day,29,2)..
   rand(T.hour,12,2)..
   rand(T.min,60,2)..
   rand(T.sec,60,2)
   
   return newDate
end
 
function ran.AcctNo()
   return math.random(99)..'-'..math.random(999)..'-'..math.random(999)
end
 
ran.Locations = { {'Chicago', 'IL'}, {'Toronto', 'ON'}, {'ST. LOUIS', 'MO'}, {'LA', 'CA'} }
 
function ran.location()
   local R = ran.choose(ran.Locations)
   return R[1], R[2]
end
 
function ran.SSN()
   return math.random(999)..'-'
          ..math.random(999)..'-'
          ..math.random(999)
end
 
function ran.addWeight(Out)
   local OBX = Out.OBX[#Out.OBX+1]
   OBX[3][1] = 'WT'
   OBX[3][2] = 'WEIGHT'
   OBX[5][1][1] = math.random(100) + 30
   OBX[6][1] = 'pounds'
   return OBX
end
   
function ran.addHeight(Out)
   local OBX = Out.OBX[#Out.OBX+1]
   OBX[3][1] = 'HT'
   OBX[3][2] = 'HEIGHT'
   OBX[5][1][1] = math.random(100) + 20
   OBX[6][1] = 'cm'
   return OBX
end
 
function ran.RandomMessage()
   local Out = hl7.message{vmd='example/demo.vmd', name='ADT'} 
   ran.scrubMSH(Out.MSH)
   ran.scrubEVN(Out.EVN)
   ran.scrubPID(Out.PID)
   ran.PV1(Out.PV1)
   ran.NK1(Out.NK1)
   ran.addWeight(Out)
   ran.addHeight(Out)
   return Out:S()   
end
 
function rand(In, Max, Size)
   
   local Result = tostring((In + math.random(Max)) % Max)
   if '0' == Result then
      Result = '1'
   end
   
   while Size > Result:len() do
      Result = '0'..Result
   end
   
   return Result
end
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

#call functions to print the segments
createMSH(message_event,message_time,message_application)
createEVN(message_event,message_time,message_reason,event_time,message_clerk,event_facility
)
createPID(patient_sex,patient_last,patient_first,patient_middle,patient_dob,patient_race,patient_address,patient_phone,patient_marital
)