import Vue from 'vue'
import axios from 'axios'
import router from 'src/router'

export default async ({Vue, router}) => {    
    axios.interceptors.request.use(function(config) {
        
        if (!config.url.includes('login') && !config.url.includes('register')) {
            localStorage.setItem('url', config.url);
            localStorage.setItem('method', config.method);
       
            if (config.method !== 'get') {
                localStorage.setItem('data', JSON.stringify(config.data));
            }
        }


        return config;
    }, function(error) {
        return Promise.reject(error);
    })

    axios.interceptors.response.use(function(response) {
        return response;
    }, async function(error) {
        if (error.response.data.error.error_type === 28) {
            const method = localStorage.getItem('method');
            const url = localStorage.getItem('url');
            const body = JSON.parse(localStorage.getItem('data'));

            const refreshFetch = await axios.get('https://localhost:5000/auth/login',
            {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('refresh_token')
                }
            });

            const refresh = refreshFetch.data;
            
            localStorage.setItem('access_token', refresh.your_auth.access_token);
            localStorage.setItem('refresh_token', refresh.your_auth.refresh_token);

            if (method === 'get') {
                return axios.get(url, 
                    {
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                        }
                    })
            }

            if (method === 'post') {
                return axios.post(url, JSON.stringify(body), 
                    {
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                            'Content-type': 'application/json'
                        }
                    });
            }

            if (method === 'patch') {
                return axios.patch(url, JSON.stringify(body), 
                    {
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                            'Content-type': 'application/json'
                        }
                    });
            }
        }
    })
    
    Vue.prototype.$axios = axios
}


