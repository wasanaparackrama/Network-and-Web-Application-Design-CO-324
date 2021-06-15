"""TODO:
    * Implement error handling in TaskapiImpl methods
    * Implement saveTasks, loadTasks
    * Implement TaskapiImpl.editTask (ignoring write conflicts)
    * Fix data race in TaskapiImpl.addTask
"""
#E/16/267


from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging
from pprint import pformat
from typing import Mapping, Sequence, Tuple
import threading

from google.protobuf import (
    any_pb2,
    api_pb2,
    duration_pb2,
    empty_pb2,
    field_mask_pb2,
    source_context_pb2,
    struct_pb2,
    timestamp_pb2,
    type_pb2,
    wrappers_pb2,
)
import grpc
from grpc import server, StatusCode
import task_pb2, task_pb2_grpc


class TaskapiImpl:
    def __init__(self, taskfile: str):
        self.taskfile = taskfile
        self.task_id = 0
        self.mutex=threading.Lock()
        

    def __enter__(self):
        """Load tasks from self.taskfile"""
        with open(self.taskfile, mode="rb") as t:
            tasklist = task_pb2.Tasks()
            tasklist.ParseFromString(t.read())
            logging.info(f"Loaded data from {self.taskfile}")
            self.tasks: Mapping[int, task_pb2.Task] = {t.id: t for t in tasklist.pending}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Save tasks to self.taskfile"""
        with open(self.taskfile, mode="wb") as t:
            tasks = task_pb2.Tasks(pending=self.tasks.values())
            t.write(tasks.SerializeToString())
            logging.info(f"Saved data to {self.taskfile}")

    #Impose a critical section in your implementation of addTask to ensure proper mutual exclusion.
    def addTask(self, request: wrappers_pb2.StringValue, context) -> task_pb2.Task:
        if len(request.value)<=1024:
            with self.mutex as l:
                logging.debug(f"addTask parameters {pformat(request)}")
                t = task_pb2.Task(id=self.task_id, description=request.value)
                self.tasks[self.task_id] = t
                self.task_id += 1
                return t
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.details('FAILED')
        t=task_pb2.Task()
        return t
        

    #Handeling Erros
    def delTask(self, request: wrappers_pb2.UInt64Value, context) -> task_pb2.Task:
        if(self.tasks.has_key(request.value)):
            logging.debug(f"delTask parameters {pformat(request)}")
            return self.tasks.pop(request.value)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.details('FAILED')
        t=task_pb2.Task()		
        return t
		
    def listTasks(self, request: empty_pb2.Empty, context) -> task_pb2.Tasks:
        logging.debug(f"listTasks parameters {pformat(request)}")
        return task_pb2.Tasks(pending=self.tasks.values())
		
	#Handeling Erros	
    def editTask(self, request: task_pb2.Task, context) -> task_pb2.Task:
        if(self.tasks.has_key(request.id)):
            logging.debug(f"editTask parameters {pformat(request)}")
            self.tasks[request.id]=request
            return self.tasks[request.id]
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.details('FAILED')
        t=task_pb2.Task()		
        return t

    #using Dictionary
    def nondestructive_editTask(self, request: task_pb2.Task, context) -> task_pb2.Tasks:
        #check for invalid id
        if request.id not in self.tasks:
             context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
             context.details('FAILED:Invalid id')
             t=task_pb2.Task()		
             return t
        #check exceeding maximum task description length
        if (len(request.description)>=1024): 
             context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
             context.details('FAILED:Task descriptions must be less than 1024')
             t=task_pb2.Task()		
             return t

        logging.debug(f" nondestructive editTask parameters {pformat(request)}")
        task = task_pb2.Task(id = request.id , description = request.description)
        #modify the task description
        self.tasks[request.id].append(task) 
        #return the modified task	
        return task 
		
    
            			
       
	#using list	
    def nondestructive_editTask2(self, request: task_pb2.Task, context) -> task_pb2.Tasks:
	    #check id is in self.tasks dict
        if(self.tasks.has_key(request.id)):
            logging.debug(f" nondestructive editTask parameters {pformat(request)}")
            self.edit_log.append(task_pb2(id=request.id,description=request.description))
			
            self.tasks[request.id].description=request.description
            return self.tasks[request.id]
        if (len(request.description)>=1024): 
             context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
             context.details('FAILED:Task descriptions must be less than 1024')
             t=task_pb2.Task()		
             return t
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.details('FAILED::Invalid id')
        t=task_pb2.Task()		
        return t
		
		
	    
	
	
    def destructive_editTask(self, request: wrappers_pb2.UInt64Value, context) -> task_pb2.Task:
	    #check id is in self.tasks dict
        if(self.tasks.has_key(request.id)):
            logging.debug(f"destructive_editTask parameters {pformat(request)}")
			#del the current task according to the id
            self.delTask(wrappers_pb2.UInt64Value(value=request.id), context) 
            return self.addTask(wrappers_pb2.StringValue(value=request.description), context)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.details('FAILED:Invalid id')
        t=task_pb2.Task()		
        return t   
	

TASKFILE = "tasklist.protobuf"
if __name__ == "__main__":
    Path(TASKFILE).touch()
    logging.basicConfig(level=logging.DEBUG)

    with ThreadPoolExecutor(max_workers=1) as pool, TaskapiImpl(
        TASKFILE
    ) as taskapiImpl:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(taskapiImpl, taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
