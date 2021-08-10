import Cookies from 'js-cookie'
import user from '../../apis/user'

export default {
    state: () => ({
        user: null,
        token: null,
    }),

    getters: {
        headers(state) {
            return {
                headers: {
                    Authorization: 'Token ' + state.token
                }
            }
        }
    },

    mutations: {
        SET_USER(state, payload) {
            state.user = payload
        },
        SET_TOKEN(state, payload) {
            state.token = payload
        },
    },

    actions: {
        reset({ commit }) {
            commit('SET_USER', null)
            commit('SET_TOKEN', null)
        },
        UserSignout({ commit }) {
            commit('SET_USER', null)
            commit('SET_TOKEN', null)
        },
        async UserLogin({ commit, dispatch }, data) {
            // just to make it clear what data is sent
            const request_data = {
                email: data.email,
                password: data.password,
            }
            await user.login(request_data).then(response => {
                const token = response.data.key
                commit('SET_TOKEN', token)
                dispatch('UserInfo')
            })
        },
        async UserRegister({ commit }, data) {
            const request_data = {
                email: data.email,
                password1: data.password1,
                password2: data.password2,
            }
            await user.register(request_data).then(response => {
                const token = response.data.key
                commit('SET_TOKEN', token)
            })
        },
        async UserInfo({ commit }) {
            await user.info().then(response => {
                const userA = response.data
                commit('SET_USER', userA)
            })
        },

        alreadyLogged({ dispatch }) {
            dispatch('UserInfo')
        },

        UserTokenLogin({ commit, dispatch }, token) {
            commit('SET_TOKEN', token)
            dispatch('UserInfo')
        },
    },
}
