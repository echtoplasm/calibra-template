import axios from 'axios';

class TaskDataService {
  getAll(){
    return axios.get('http://localhost:8000/api/tasks/');
   } 
  
  createTask(data){
    return axios.post('http://localhost:8000/api/tasks/', data);
  }

  updateTask(data){
    return axios.put('http://localhost:8000/api/tasks/${id}', data);
}

  deleteTask(id){
    return axios.delete('http://localhost:8000/api/tasks/${id}');
  }

  completeTask(id){
    return axios.put('http://localhost:8000/api/tasks/${id}/complete');
  }

  login(data){
    return axios.post('http://localhost:8000/login', data);
  }

  signup(data){
    return axios.post('http://localhost:8000/signup', data);
  }

}

export default TaskDataService;


