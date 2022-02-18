import { defineStore } from "pinia";
import axios from 'axios'

export const useAuthStore = defineStore({
    id: "authStore",
    state: () => ({
        user: {
         
        },
        token: '',
        isAuthenticated : false,
    }),

    actions: {
        async login(userForm) {
            let result = await axios.post('https://papasucre.herokuapp.com/user-login', {
                email: userForm.email,
                password: userForm.password
            })
            this.token = result['data']['token']
          
        },
        async authenticate(user_mail){
            let response = await axios.get('https://papasucre.herokuapp.com/protected', {
                headers: {
                    Authorization: `Bearer ${this.token}`
                }
            })
            if(response.status == 200){
                this.isAuthenticated = true
                let user_response = await axios.get('https://papasucre.herokuapp.com/users/' + user_mail)
                this.user = user_response.data
                console.log(this.user)
            
            }
            else {
                this.isAuthenticated = false
            }
        }
    },
});