from datetime import date, datetime, timedelta
import uuid
import random

#dictionaries to pull data from for messages
   #might be moved later on to a db or separate files 
sex = {'M', 'F'} 
last_names = {'Muir','Smith','Adams','Garland', 'Meade', 'Fitzgerald', 'WHITE'}
male_names = {'Fred','Jim','Gary','John','Steve','Wilbur','Aurthur','Mike'}
female_names = {'Mary','Sabrina','Tracy','Sheena','Miranda','Eileen'}
race = {'AI', 'EU', 'Mixed', 'Martian', 'Unknown', 'White'}
street = {'Ford St.','Sunshine Lane','Seasame St.','Main St.','Delphi Cres.', 'Miller Lane', 'Yonge St.', 'Main Rd.', 'First Ave'}
relation = {'Grandchild', 'Second Cousin', 'Sibling', 'Parent'}
adt_event = {'A01', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08'}
facility = {'Lab','ER','Clinic','Oncology','MedSurg','ICU'}
application = {'Epic', 'Allscripts', 'Cerner','Expanse','Magic','CPSI','eCW'}
event_reason = {'01','02','03','O','U'}
clerk_id = {'0341','4321','4564','3478','0199','0002','4532','2341'}
################################################################################

#creates MSH segment
def createMSH(event,time):
   MSH=[]
   MSH_string=""

   MSH.insert(0,"")
   MSH.insert(1,"^~\&")
   MSH.insert(2,"adt-gen")
   MSH.insert(3,"%s"%(random.choice(tuple(application))))
   MSH.insert(4,"My Transform Pipeline")
   MSH.insert(5,'hl7-rdb')
   MSH.insert(6,time)
   MSH.insert(7,"")
   MSH.insert(8,"ADT^%s"%(event))
   MSH.insert(9,str(uuid.uuid4())[:8])
   MSH.insert(10,str(uuid.uuid1())[:4])
   MSH.insert(11,'2.5')
   
   for x in range(0,len(MSH)):
      MSH_string += (MSH[x] + "|")

   return(print("MSH" + MSH_string))

#create EVN segment
#EVN|A08|202206230204|202010151442|EDREGCLI|IATRICS^Iatric^Systems|REG CLI|.
def createEVN(event,time,reason, id, event_time, event_facility):
   EVN=[]
   EVN_string=""

   EVN.insert(0,event)
   EVN.insert(1,time)
   EVN.insert(2,time)
   EVN.insert(3,"%s"%(reason))
   EVN.insert(4,id)
   EVN.insert(5,event_time)
   EVN.insert(6,event_facility)
   
   for x in range(0,len(EVN)):
      EVN_string += (EVN[x] + "|")

   return(print("EVN|" + EVN_string))

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
event_facility = random.choice(tuple(facility))
event_time = str(
   (datetime.now()-timedelta(minutes = random.randrange(1,999,1))).strftime("%Y%m%d%H%M%S")
)


createMSH(message_event, message_time)
createEVN(message_event, message_time, message_reason, event_time, message_clerk, event_facility)