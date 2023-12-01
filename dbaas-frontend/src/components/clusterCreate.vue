<template>
   <leftSidebar />

   <div class="mt-20 w-auto ">
      <div class="w-full h-15 border-b-2 border-solid text-center">
         <div class="font-4xl text-semibold">Create Cluster</div>
      </div>
   </div>

   <div>
      <ul class="flex justify-center space-x-10 mt-10 mx-10"> <!-- Adjust mx-10 for the desired left space -->
         <li><router-link to="/clusterCreate">Cluster Info</router-link></li>
         <li><button @click.prevent="Next(selectedProvider)" to="/cluster-setting">Cluster Settings</button></li>
         <li><a href="#" class="link-style cursor-not-allowed">DB Configuration</a></li>
         <li><a href="#" class="link-style cursor-not-allowed">Additional Settings</a></li>
      </ul>
   </div>
   <div class="flex sm:ml-64 ">
      <div>
         <h1 class="ml-[40px] mt-10 py-4 text-gray-900 text-xl font-semibold">Select the type of cluster you want to use
         </h1>
         <div class="ml-[40px]">
            <div class="col-span-2 mb-5">
               <div>
                  <h1 class="py-4 text-gray-900 text-xl font-semibold">Cluster Type</h1>
               </div>
               <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                  <div class="h-72 w-72 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedType == 'single' }">

                     <label for="single">
                        <input type="radio" id="single" class="hidden" value="single" v-model="selectedType"
                           @change="updateType">
                        <h1 class="pt-2 text-gray-900 font-semibold">Single cluster</h1>
                        <p class="pt-8 px-5 text-gray-500 text-sm">A Single Node Cluster refers to a cluster configuration in a distributed computing environment where all cluster components, such as databases, services, or applications, run on a single node or machine.</p>
                     </label>
                  </div>

                  <div class="h-72 w-72 ml-12 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedType == 'multiple' }">

                     <label for="multiple">
                        <input type="radio" id="multiple" class="hidden" value="multiple" v-model="selectedType"
                           @change="updateType">
                        <h1 class="pt-2 text-gray-900 font-semibold">Primary/Standby High Availability</h1>
                        <p class="pt-2 px-5 text-gray-500 text-sm">A Primary/Standby High Availability (HA) Cluster refers to a configuration in a distributed computing environment where two nodes (or more) operate in tandem to provide fault tolerance and redundancy.</p>
                     </label>
                  </div>
               </div>

               <!-- Providers Type -->
               <div class="mt-5">
                  <h1 class="py-4 text-gray-900 text-xl font-semibold"> Providers </h1>
               </div>
               <div class="grid grid-cols-2 gap-4 w-2/3 ">
                  <div class="h-72 w-72 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedProvider == 'Cloudstack' }">
                     <label>
                        <input type="radio" class="hidden" value="Cloudstack" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain h-72 w-72 max-w-full rounded-lg" src="@/assets/static/cloudstack.png">

                     </label>
                  </div>

                  <div class="h-72 w-72 ml-12 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedProvider == 'vmware' }">

                     <label>
                        <input type="radio" class="hidden" value="vmware" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain h-72 w-72 max-w-full rounded-lg" src="@/assets/static/vmware.png"
                           alt="">

                     </label>
                  </div>

                  <div class="h-72 w-72  bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedProvider == 'Harvester' }">

                     <label>
                        <input type="radio" class="hidden" value="Harvester" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain h-72 w-72 max-w-full rounded-lg"
                         src="@/assets/static/harvester-logo.png"
                           alt="providerlogo">

                     </label>
                  </div>

                  <div class="h-72 w-72 ml-12 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedProvider == 'Openstack' }">

                     <label>
                        <input type="radio" class="hidden" value="Openstack" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain h-72 w-72 max-w-full rounded-lg" 
                        src="@/assets/static/Openstack.png"
                           alt="">

                     </label>
                  </div>
               </div>
               <p class="text-red-500" v-if="this.error">This  Provider is not connected to connect
                  <router-link to="/providers" class="text-red-900"> Click here</router-link></p>

               <div class="pt-10">
                  <button @click.prevent="Next(this.selectedProvider)"
                     class="bg-blue-900 w-24 p-3 h-10 text-center text-white rounded-md">
                     Next
                  </button>

               </div>
            </div>
         </div>
      </div>

      <clusterSum />
   </div>

   <!-- Cluster summary -->


   <fooTer />
</template>

<script>

import leftSidebar from '@/components/leftSidebar.vue';
import fooTer from '@/components/fooTer.vue';
import clusterSum from '@/components/clusterSummary.vue';

import { useInputStore } from '@/stores/clusterStore';
import axios from 'axios';

export default {
   components: {
      leftSidebar,
      fooTer, clusterSum
   },
   data() {
      return {
         selectedType: 'single',
         selectedValue: 'Bit-Blast',
         selectedProvider: 'Cloudstack',

         user_id: '',
         provider_info: [],
         error: ''
         // options: [
         //    { value: 'single', label: 'single' },
         //    { value: 'multiple', label: 'multiple' },
         // ],
      };
   },
   created() {
      this.user_id = sessionStorage.getItem('user_id');
      this.getAllProviderData();

   },
   methods: {
      updateType() {
         this.selectedType = this.selectedType
      },
      updateValue() {
         this.selectedValue = this.selectedValue
      },
      updateProvider() {
         this.selectedProvider = this.selectedProvider
      },

      Next(providerName) {
         console.log("Next mtd cal");
         if (
            this.provider_info.some(
               (provider) =>
                  provider.provider_name.toLowerCase() === providerName.toLowerCase() &&
                  provider.is_connected
            )
         ) {

            console.log(`${providerName} is connected!`);
            const store = useInputStore();
            store.setType(this.selectedType);
            store.setProvider(this.selectedProvider);
            this.$router.push('/cluster-setting');
         } else {

            this.error = "providerError"
            setTimeout(() => {
          this.error = '';
        }, 5000);
      } 
   },

      getAllProviderData() {
         axios.get(`http://127.0.0.1:8000/api/v3/providers/`)
            .then((response) => {
               this.provider_info = response.data
               console.log(response.data);
            })
      },

   },
};
</script>


<style > table,
 th,
 td {
    border: none;
    border-collapse: separate;
 }

 th,
 td {
    padding: 5px 10px;
 }

 table {
    width: 100%;
 }

 .link-style {
    text-decoration: none;
    /* Remove the default underline */
    /* Set the dfault text color */
    font-weight: 600;
    /* Set the default font weight to make it bold */
    transition: color 0.2s, border-bottom-color 0.2s;
    /* Add a smooth transition effect */
 }

 .selected {
    color: rgb(229 231 235);
    box-shadow: grey;
    border-color: rgb(30 41 59);
 }
</style> 