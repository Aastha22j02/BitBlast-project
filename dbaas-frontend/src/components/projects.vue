<template>
  <leftSidebar />
 
  <div class="container sm:ml-72">
    <div class="mt-20 p-4 w-full bg-gray-100 flex">
      <div class="text-black font-semibold text-4xl">Projects</div>
    </div>
    <div class="px-4 mt-10">
      <div class="mb-6">
        <label for="projectname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Project Name</label>
        <input type="text" id="projetname" v-model="project.project_name"
        :class="{ 'error': input1Error, 'shake': shakingInput === 'project.project_name' }"
 
          class="w-[300px] bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Project Name" required>
      </div>
    
 
      <div v-if="error" class="text-red-500 ">{{ error }}</div>
      <div class="mt-10">
        <button  
        class="bg-blue-900 p-3 h-10 text-center text-white rounded-md"
          @click="saveProject">
          Create New Project
      </button>
      </div>
    </div>
    <div class="w-full h-15 border-b-2 p-4 border-solid mt-20 flex items-center">
      <div class="text-2xl font-semibold">Project List</div>
 
      <!-- Search option will hide here -->
      <!-- <div class="relative ml-4">
        <input type="text"
          class="pl-8 pr-3 py-2 border rounded-lg w-48 bg-white border-gray-400 focus:border-primary-500 focus:ring-primary-500"
          placeholder="Search" />
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M21 21l-5.2-5.2M15 10.5a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z"></path>
          </svg>
        </div>
      </div> -->
    </div>
    <div class="relative  shadow-md sm:rounded-lg" >
  <table class="w-4/5 text-sm text-left rtl:text-right text-gray-500 dark:text-gray-500">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-50 dark:text-gray-700">
          <tr>
              <th scope="col" class="px-6 py-3">
                  Project id
              </th>
              <th scope="col" class="px-6 py-3">
                  Project  Name
              </th>
              <th scope="col" class="px-6 py-3">
                  Created on
              </th>
              <th scope="col" class="px-6 py-3">
                Action
            </th>
          </tr>
      </thead>
      <tbody v-for="(project, index) in projects" :key="index">
          <tr class="bg-white border-b dark:bg-white dark:border-gray-700">
              <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-gray-900">
                  {{ project.id}}
              </th>
              <td class="px-6 py-4">
                {{ project.project_name}}
              </td>
              <td class="px-6 py-4">
                {{ formatTimeAgo(project.created_date) }}
              </td>
              <td class="px-6 py-4">
                  <button type="button" style="cursor: not-allowed; opacity: 0.7" class=" font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</button>
              </td>
          </tr>
  
      </tbody>
  </table>
</div>
  </div>
 
 
  <footer />
</template>
<script>
import leftSidebar from '@/components/leftSidebar.vue';
import fooTer from '@/components/fooTer.vue';
import axios from 'axios';
 
export default {
  components: {
    leftSidebar,
    fooTer,
  },
  data() {
    return {
      isActive: false,
      isDeleted: false,
      projects: [],
      error: '',
      user_id : null,
      project_name: '',
      input1Error: false,
      shakingInput: null,
      project: {
        project_name: '',
        user: '',
      }
 
    };
  },
  methods: {
    saveProject() {
      this.input1Error = this.project.project_name === '';
      if(this.input1Error){
        this.shakingInput = 'project.project_name'
        setTimeout(()=>{
        this.shakingInput = null;
      },500);
      }
     else {
    
      axios.post("http://127.0.0.1:8000/api/v2/project/", this.project)
        .then(response => {
          this.fetchProject()
          window.location.reload()
        })
        .catch(error => {
            this.error = error.response.data.error;
            setTimeout(() => {
              this.error = '';
            }, 3000);
          });
      }      
    },
    fetchProject() {
      const user_id = this.project.user
      axios.get(`http://127.0.0.1:8000/api/v2/project/user/${user_id}/`)
        .then(response => {
          this.projects = response.data;
          console.log(this.projects);        
        })
    },
    formatTimeAgo(createdAt) {
      const createdTime = new Date(createdAt)
      const currentTime = new Date()
      const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000)
 
      if (timeDifferenceInSeconds < 60) {
        return `${timeDifferenceInSeconds} sec ago`
      } else if (timeDifferenceInSeconds < 3600) {
        const minutes = Math.floor(timeDifferenceInSeconds / 60)
        return `${minutes} min ago`
      } else if (timeDifferenceInSeconds < 86400) {
        const hours = Math.floor(timeDifferenceInSeconds / 3600)
        return `${hours} hour ago`
      } else {
        const days = Math.floor(timeDifferenceInSeconds / 86400)
        return `${days} days ago`
      }
    },
  },
  created() {
    this.project.user = sessionStorage.getItem('user_id');
    this.fetchProject()
  },
  resetError(fieldName) {
      if (fieldName === 'project_name') {
        this.input1Error = false;
      } else if (fieldName === 'input2') {
        this.input2Error = false;
      }
    },
 
};
</script>
 
<style scoped>
.error {
  border: 2px solid red;
}
 
.shake {
  animation: shake 0.5s ease-in-out 8 alternate;
}
 
@keyframes shake {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(10px, 0);
  }
}
</style>