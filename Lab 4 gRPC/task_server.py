#author-E/16/267
#CO224_lab4:server
#here the ids are generated randomly

import logging
from concurrent.futures import ThreadPoolExecutor
from grpc import server
import task_pb2, task_pb2_grpc
from random import randint 


class TaskapiImpl:
    """'Implementation of the Taskapi service"""

    def __init__(self):
        # TODO: initialise attributes to store our tasks.
        self.tasks = task_pb2.Tasks()
		#list to keep the id values
        self.id_list=[0]
        pass

    def addTask(self, request, context):
        logging.info(f"adding task {request.description}")
		# TODO: implement this!
        id_number=0
		#check whether id already exit
        while(id_number in self.id_list):
			#Ids are generated randomly
            id_number=randint(0,1000)
        self.id_list.append(id_number)
        #add to the task list
        self.tasks.tasks.append(task_pb2.Task(id= id_number,description =request.description))
		#return id_number to the client from the server
        return task_pb2.Id(id= id_number)
		
		

    def delTask(self, request, context):
        logging.info(f"deleting task {request.id}")
        # TODO: implement this!
        for t in  self.tasks.tasks:
            if t.id == request.id:
				#remove id from the list
                self.tasks.tasks.remove(t)
				#return the deleted tasks
                return t
            return 'Invalid'
			

    def listTasks(self, request, context):
        logging.info("returning task list")
        # TODO: implement this!
        return self.tasks


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with ThreadPoolExecutor(max_workers=1) as pool:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(TaskapiImpl(), taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
