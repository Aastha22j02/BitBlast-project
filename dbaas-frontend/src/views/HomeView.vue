<template>
   <leftSidebar />

   <div class="main p-4 sm:ml-64 mt-20 ">
      <div class="box-border h-96 w-2/3 border-2 border-red-400 rounded-md shadow-md shadow-red-400/50">
         <div class="text-center">
            <h1 class="pt-20 text-4xl font-bold">Hello {{ Username }} !</h1>
            <h2 class="pt-5 text-xl font-medium">Let's create a cluster</h2>
            <div class="pt-5">
               <router-link to="/clusterCreate" class="bg-blue-900 w-96 
                p-3 h-10 text-center text-white rounded-md">
                  Create New Cluster
               </router-link>
            </div>
         </div>
      </div>
   </div>
   <div class="mt-56 ">
      <fooTer />
   </div>
   
</template>

<script>
import leftSidebar from '@/components/leftSidebar.vue';
import fooTer from '@/components/fooTer.vue';

export default {
   components: {
      leftSidebar,
      fooTer,
   },
   data(){
      return{
         Username: ''
      }
   },
   created(){
      this.Username = sessionStorage.getItem("username");
   }

}
</script>

