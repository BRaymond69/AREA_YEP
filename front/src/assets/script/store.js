import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        user: true,
    },
    mutations: {
        updateUser (state) {
            state.user = !state.user
        },
    }
})

export default store