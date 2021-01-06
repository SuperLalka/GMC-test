import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";

export default createStore({
  state: {
    is_Authorize: false
  },
  mutations: {
    CHANGE_AUTH_STATUS: (state) => {
      state.is_Authorize = !state.is_Authorize;
    }
  },
  actions: {
    TOGGLE_AUTH_STATUS({commit}) {
      commit('CHANGE_AUTH_STATUS')
    }
  },
  getters: {
    IS_AUTH_STATE(state) {
      return state.is_Authorize;
    }
  },
  plugins: [createPersistedState()],
})
