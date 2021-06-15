#E/16/267

import sys
import paho.mqtt.client as mqtt
import json
import uuid

global tasks
tasks={}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("CO324/TaskAPI/E16267/#")
   
#Callback function
def on_message(client, userdata, msg):
    
	#for ADD operation
    if(msg.topic=="CO324/TaskAPI/E16267/ADD"):
        	
        task=json.loads(msg.payload) 
        tasks[task["id"]]=task
       
    
    #for DELETE operation
    if(msg.topic=="CO324/TaskAPI/E16267/DELETE"):
        print(msg.topic+" "+str(msg.payload))
        del_id=msg.payload.decode('UTF-8')
        if del_id in tasks.keys():
            tasks.pop(del_id)
               
        
    
    #for EDIT operation
    if(msg.topic=="CO324/TaskAPI/E16267/EDIT"):
        print(msg.topic+" "+str(msg.payload))
        task=json.loads(msg.payload) 
        
        if task["id"] in tasks.keys():
            current_state=tasks[task["id"]]["state"]
            next_state=task["state"]
			#calling check state function
            if(checkFSM(current_state,next_state)):
                tasks[task["id"]]["state"]=next_state
    print('\nCurrent Task List\n')
    print(tasks)
    print('\n')
    print("Enter the topic: ")
          
        
        

#FSM	
def checkFSM(current_state,next_state):
        if(current_state== 'OPEN') and (next_state== 'ASSIGNED'):
            return True
        elif(current_state== 'OPEN') and (next_state== 'CANCELLED'):
            return True
        elif(current_state=='ASSIGNED') and (next_state== 'PROGRESSING'):
            return True
        elif(current_state=='PROGRESSING') and (next_state== 'CANCELLED'):
            return True
        elif(current_state== 'PROGRESSING') and (next_state=='DONE'):
            return True
        elif(current_state==next_state):
            return True
        else:
            return False
  
def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()

while(1):
    
    
    topic=input()
    
	#publishing add 
    if(topic=="CO324/TaskAPI/E16267/ADD"):
        
        description=input("Enter the task(description): ")
        #generating unique id(UUID)
        id=str(uuid.uuid1())
        #default state
        state="OPEN"
        task_des={"id":id, "state":state, "description": description}
        message=json.dumps(task_des)
        infot = client.publish(topic, message, qos=2,retain=True)
        infot.wait_for_publish()
        
        print(task_des)
     
    #publihsing DELETE	 
    if(topic=="CO324/TaskAPI/E16267/DELETE"):
        
        id=input("Enter the task id: ")
        message=id
        infot = client.publish(topic, message, qos=1,retain=False)
        infot.wait_for_publish()
        
     #publihsing DELETE	EDIT
    if(topic=="CO324/TaskAPI/E16267/EDIT"):
       
        id=input("Enter the task id: ")
        state=input("Enter the task state: ")
        task_des={"id":id, "state":state, "description":""}
        task_e=json.dumps(task_des)
        message=task_e
        infot = client.publish(topic, message, qos=2,retain=False)
        infot.wait_for_publish()
              
        
    
    
client.connect("mqtt.eclipse.org", 1883, 60)




