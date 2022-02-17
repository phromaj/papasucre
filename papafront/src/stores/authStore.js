import { defineStore } from "pinia";
import axios from 'axios'

export const useAuthStore = defineStore({
    id: "authStore",
    state: () => ({
        user: {
            email: "",
            password: "",
        },
        token: '',
        isAuthenticated : false,
    }),

    actions: {
        async login() {
            let result = await axios.post('http://127.0.0.1:8000/user-login', {
                email: this.user.email,
                password: this.user.password
            })
            this.token = result['data']['token']
          
        },
        async authenticate(){
            let response = await axios.get('http://127.0.0.1:8000/protected', {
                headers: {
                    Authorization: `Bearer ${this.token}`
                }
            })
            if(response.status == 200){
                this.isAuthenticated = true
            }
            else {
                this.isAuthenticated = false
            }
        }
    },
});