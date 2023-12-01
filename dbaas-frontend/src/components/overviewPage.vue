<template>
  <div>
    <leftSidebar />
    <div class="cluster p-4 sm:ml-64 mt-40 flex">
      <div class="text-black font-semibold text-4xl">
        Clusters
      </div>
      <div class="ml-auto">
        <router-link to="/clusterCreate" class="bg-blue-900 w-96 p-3 h-10 t
        ext-center  rounded-md text-white">
          Create New Cluster
        </router-link>
       
      </div>
    </div>
    <div class="w-full h-15 border-b-2 p-4 sm:ml-64 border-solid mt-10 flex items-center">
      <ul class="flex space-x-10 mx-10">
        <li>
          <a href="#" class="link-style text-2xl" :class="{ 'link-style-default': isActive }"
            @mouseenter="isActive = true" @mouseleave="isActive = false">
            Active Database
          </a>
        </li>
        <!-- <li>
          <a href="#" class="link-style text-2xl" :class="{ 'link-style-default': isDeleted }"
            @mouseenter="isDeleted = true" @mouseleave="isDeleted = false">
            Deleted
          </a>
        </li> -->
      </ul>

      <!-- Search Bar -->
      <!-- <div class="relative ml-4">
        <input
          type="text"
          class="pl-8 pr-3 py-2 border rounded-lg w-48 bg-white border-gray-400 focus:border-primary-500 focus:ring-primary-500"
          placeholder="Search"
        />
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg
            class="w-5 h-5 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-5.2-5.2M15 10.5a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z"></path>
          </svg>
        </div>
      </div> -->
      <div class="ml-4">
        <!-- Project Dropdown -->
        <select v-model="selectedProject" @change="fetchClustersByProject">
          <option value="">All Projects</option>
          <option v-for="project in projects" :key="project.id" :value="project.id">{{ project.project_name }}</option>
        </select>
      </div>
    </div>
   
    <div class="w-full h-auto p-4 sm:ml-64 border-solid mt-4 ml-64 items-center">
      <div class="" v-if="clusters.length === 0">
        <span class="text-gray-400 mb-2 text-2xl ml-96 ">No Cluster found in the Selected Project</span>
      </div>



      <div class="relative  shadow-md sm:rounded-lg" v-else>
        <table class="w-4/5 text-sm text-left rtl:text-right text-gray-500 dark:text-gray-500">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-50 dark:text-gray-700">
            <tr>
              <th scope="col" class="px-6 py-3">
                Database id
              </th>
              <th scope="col" class="px-6 py-3">
                Database Name
              </th>
              <th scope="col" class="px-6 py-3">
                Database Type
              </th>
              <th scope="col" class="px-6 py-3">
                Provider
              </th>
              <th scope="col" class="px-6 py-3">
                Database Version
              </th>
              <th scope="col" class="px-6 py-3">
                Created on
              </th>
              <th scope="col" class="px-6 py-3">
                Actions
              </th>

              <!-- <th scope="col" class="px-6 py-3">
                Action
            </th> -->
            </tr>
          </thead>
          <tbody v-for="(cluster, index) in clusters" :key="index">
            <tr class="bg-white border-b dark:bg-white dark:border-gray-700">
              <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-gray-900">
                {{ cluster.id }}
              </th>
              <td class="px-6 py-4">
                {{ cluster.cluster_name }}
              </td>
              <td class="px-6 py-4">
                {{ cluster.cluster_type }}
              </td>
              <td class="px-6 py-4">
                {{ cluster.provider }}
              </td>
              <td class="px-6 py-4">
                PostgreSQL {{ cluster.database_version }}
              </td>
              <td class="px-6 py-4">
                {{ formatTimeAgo(cluster.created_date) }}
              </td>
              <td class="px-6 py-4">
                <button @click="toggleModal(cluster.cluster_name)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">
                  View</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div v-if="clusters.length ==0" class="mt-72  ">

  </div>
  <fooTer />


  <div v-show="isModalVisible"  tabindex="-1" class="fixed top-0 left-0 right-0 bottom-0
      z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
<div class="relative w-2/4">
    <div  class="relative bg-white rounded-lg shadow dark:bg-gray-100">
        <button @click="toggleModal" type="button" class="absolute top-3
        right-2.5 text-gray-400 bg-transparent hover:bg-gray-200
         hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex
         justify-center items-center dark:hover:bg-gray-600
          dark:hover:text-white" data-modal-hide="popup-modal">
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
            <span class="sr-only">Close modal</span>
        </button>
        <div class="p-6 ">
            <h3 class="mb-5 text-lg font-normal text-black dark:text-gray-400">
              {{ selectedCluster }}
            </h3>
            
          <!-- Input fields for provider -->
          <div class="px-4 mt-10">
            <div >
              <p v-if="contentList.length > 1" v-html="addLineBreaks(contentList[1].content)"></p>
              <p v-else class="mb-10">Loading.......</p>
            </div>
          <div v-if="error" class="text-red-500 text-center mb-4">{{ error }}</div>    
        </div>


          <button @click="toggleModal" type="button" class="py-2.5 px-4 text-xs font-medium 
          text-center text-white bg-gray-800 rounded-lg focus:ring-4 
          focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
            Close
        </button>
        </div>
    </div>
</div>
</div>
</template>

<script>
import leftSidebar from "@/components/leftSidebar.vue";
import fooTer from "@/components/fooTer.vue";
import axios from "axios";

export default {
  components: {
    leftSidebar,
    fooTer,
  },
  data() {
    return {
      isModalVisible: false, 
      selectedCluster: '',
      contentList: [],
      error:'',
      isActive: false,
      isDeleted: false,
      user_id: null,
      projects: [],
      selectedProject: "",
      clusters: [],
     


    };
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.fetchProjects();
    this.fetchClusters();
  },
  methods: {
    toggleDarkMode() {
      this.toggleDark();
    },
    toggleModal(selectedCluster) {
        this.selectedCluster = selectedCluster
        this.isModalVisible = !this.isModalVisible;
        this.getClusterDetails();
     },
    
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    projectToggle() {
      this.ProjectToggle = !this.ProjectToggle;
    },
    userToggle() {
      this.UserToggle = !this.UserToggle;
    },
    logout() {
     
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      window.location.reload();
    },
    addLineBreaks(text) {
      // Replace '\n' with '<br>' for rendering line breaks in HTML
      return text.replace(/\n/g, '<br>');
    },

    getClusterDetails(){
      axios.get(`http://127.0.0.1:8000/api/v2/result/content/${this.selectedCluster}/`)
      .then(response => {
        this.contentList = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    },

    getFirstLetter(username) {
      return username.charAt(0, 1).toUpperCase();
    },
    fetchProjects() {
      axios.get(`http://127.0.0.1:8000/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects = response.data;

        });
    },
    fetchClusters() {
      axios.get(`http://127.0.0.1:8000/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusters = response.data;
          console.log(this.clusters);
        });
    },
    fetchClustersByProject() {
      if (this.selectedProject) {
        axios.get(`http://127.0.0.1:8000/api/v2/cluster/project/${this.selectedProject}/`)
          .then(response => {
            this.clusters = response.data;
          });
      } else {
        this.fetchClusters();
      }
    },
    formatTimeAgo(createdAt) {
      const createdTime = new Date(createdAt);
      const currentTime = new Date();
      const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000);

      if (timeDifferenceInSeconds < 60) {
        return `${timeDifferenceInSeconds} sec ago`;
      } else if (timeDifferenceInSeconds < 3600) {
        const minutes = Math.floor(timeDifferenceInSeconds / 60);
        return `${minutes} min ago`;
      } else if (timeDifferenceInSeconds < 86400) {
        const hours = Math.floor(timeDifferenceInSeconds / 3600);
        return `${hours} hour ago`;
      } else {
        const days = Math.floor(timeDifferenceInSeconds / 86400);
        return `${days} days ago`;
      }
    },
  },

  

};
</script>

<style scoped>
.link-style {
  text-decoration: none;
  color: black;
  font-weight: 600;
  transition: color 0.2s, border-bottom-color 0.2s;
}

.link-style-default {
  color: #ff007f;
  border-bottom: 2px solid #ff007f;
}


.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text {
  font-size: 20px;
  font-weight: bold;
  text-align: left;
  line-height: 30px;
}

.subtext {
  font-size: 16px;
  text-align: left;
  margin-top: 5px;
  line-height: 24px;
}

.delete-button {
  display: inline-block;
  vertical-align: middle;

  margin-left: 20px;
}

.progress-bar {
  width: 1800px;
  /* or any other desired width */
}
</style>
