<script>
import axios from 'axios';
import { useInputStore } from '@/stores/clusterStore';
import leftSidebar from '@/components/leftSidebar.vue';
import clusterSummary from '@/components/clusterSummary.vue';
import fooTer from '@/components/fooTer.vue';

export default {
  components: {
    leftSidebar,
    fooTer,
    clusterSummary,
  },
  data() {
    return {
      selectedTools: [],
      postgres_version: '',
      cluster_name: '',
      project_id: '',
      user_id: '',
      provider_info: '',
      errorClusterName: '',
      errorDatabaseVersion: '',
      errorClusterNameExists: '',
      errorNoSelectedProject: '',
      backendError: '',
      db_user: '',
      db_password: '',
    };
  },
  created() {
    this.user_id = sessionStorage.getItem('user_id');
    this.project_id = sessionStorage.getItem('project_id');
  },
  methods: {
    Create() {
      const store = useInputStore();
      store.setTools(this.selectedTools);
      this.$router.push('/clusterCreate');
    },
    createCluster() {
      // Reset error messages
      this.errorClusterName = '';
      this.errorDatabaseVersion = '';
      this.errorClusterNameExists = '';
      this.errorNoSelectedProject = '';
      this.backendError = '';

      if (!this.cluster_name) {
        this.errorClusterName = 'Cluster name is required';
        setTimeout(() => {
          this.errorClusterName = '';
        }, 5000);
        return;
      }

      if (!this.postgres_version) {
        this.errorDatabaseVersion = 'Postgres version is required';
        setTimeout(() => {
          this.errorDatabaseVersion = '';
        }, 5000);
        return;
      }

      if (!this.project_id) {
        this.errorNoSelectedProject = 'You have not selected any Project';
        setTimeout(() => {
          this.errorNoSelectedProject = '';
        }, 5000);
        return;
      }

      // Check if cluster name already exists
      axios
        .get(`http://127.0.0.1:8000/api/v2/cluster/?cluster_name=${this.cluster_name}&project=${this.project_id}`)
        .then((response) => {
          if (response.data.length > 0) {
            // Cluster name already exists
            this.errorClusterNameExists = 'Cluster with the same name already exists in the project';
            setTimeout(() => {
              this.errorClusterNameExists = '';
            }, 5000);
          } else {
            // Cluster name doesn't exist, proceed with creating the cluster
            const fromData = {
              db_user: this.db_user,
              db_password: this.db_password,
              user: this.user_id,
              project: this.project_id,
              provider: this.selectedProvider,
              cluster_type: this.selectedType,
              cluster_name: this.cluster_name,
              postgres_version: this.postgres_version,
              provider_endpoint: this.provider_info.provider_url,
              provider_access_token: this.provider_info.access_token,
              provider_secret_key: this.provider_info.secret_key,
            };

            this.$router.push('/result');
            axios
              .post(`http://127.0.0.1:8000/api/v2/cluster/`, fromData)
              .then((response) => {
                // ... (existing success logic) ...
              })
              .catch((error) => {
                // Handle backend errors
                if (error.response && error.response.data) {
                  // ... (existing error handling logic) ...
                }
              });
          }
        })
        .catch((error) => {
          // Handle error in checking cluster name existence
          console.error('Error checking cluster name existence:', error);
        });
    },
  },
  computed: {
    selectedType() {
      return useInputStore().selectedType;
    },
    selectedProvider() {
      return useInputStore().selectedProvider;
    },
  },
};
</script>
