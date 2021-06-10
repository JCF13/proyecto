import Vue from 'vue'
import axios from 'axios'
import router from 'src/router'

export default async ({Vue, router}) => {
    axios.interceptors.request.use(function(config) {
        return config;
    }, function(error) {
        return Promise.reject(error);
    })
    
    Vue.prototype.$axios = axios
}


