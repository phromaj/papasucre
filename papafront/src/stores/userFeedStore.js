import { defineStore } from "pinia";
import axios from 'axios';


export const userFeedStore = defineStore({
  id: "userFeed",
  state: () => ({
    userList: [],
  }),

  actions: {
    async getUserList(user) {
      let result = await axios.get('https://papasucre.herokuapp.com/users/sex/' + user.sex)
      result.data.forEach(element => {
        this.userList.push(element)
      });

    },
  },
});
