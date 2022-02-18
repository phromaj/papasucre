import { defineStore } from "pinia";
import axios from 'axios';


export const userFeedStore = defineStore({
  id: "userFeed",
  state: () => ({
    userList: [],
  }),

  actions: {
    async getUserList(user) {
      let result = await axios.get('http://127.0.0.1:8000/users/sex/' + user.sex)
      result.data.forEach(element => {
        this.userList.push(element)
      });

    },
  },
});
