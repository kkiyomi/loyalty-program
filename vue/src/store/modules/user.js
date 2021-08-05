import Cookies from 'js-cookie'
import user from '../../apis/user'

export default {
    state: () => ({
        darkMode: true,
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
        SET_DARKMODE(state, payload) {
            state.darkMode = payload
        },
        SET_USER(state, payload) {
            state.user = payload
        },
        SET_TOKEN(state, payload) {
            state.token = payload
        },
    },

    actions: {

        setDarkmode({ commit, dispatch }, dark) {
            commit('SET_DARKMODE', dark)
            let theme = 'light'
            if (dark) {
                theme = 'dark'
            }
            dispatch('setThemeCookie', theme)
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
                dispatch('setUserCookie', token)
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
                dispatch('setUserCookie', token)
            })
        },
        async UserInfo({ commit }) {
            await user.info().then(response => {
                const userA = response.data
                commit('SET_USER', userA)
            })
        },
        UserSignout({ commit, dispatch }) {
            commit('SET_USER', null)
            commit('SET_TOKEN', null)
            dispatch('delUserCookie')
        },
        setUserCookie({ }, token) {
            Cookies.set('at', token, { secure: true })
        },
        delUserCookie({ }) {
            Cookies.remove('at')
        },
        getUserCookie({ commit, dispatch }) {
            const token = Cookies.get('at')
            if (token != undefined) {
                commit('SET_TOKEN', token)
                dispatch('alreadyLogged')
            }
        },
        alreadyLogged({ dispatch }) {
            dispatch('UserInfo')
        },
        setThemeCookie({ }, data) {
            Cookies.set('theme', data, { secure: true })
        },
        getThemeCookie({ commit }) {
            const theme = Cookies.get('theme')
            if (theme != undefined) {
                commit('SET_DARKMODE', theme == 'dark' ? true : false)
            }
        },
        getCookies({ dispatch }) {
            dispatch('getThemeCookie')
            dispatch('getUserCookie')
        },
        UserTokenLogin({ commit, dispatch }, token) {
            commit('SET_TOKEN', token)
            dispatch('setUserCookie', token)
            dispatch('UserInfo')
        },

    },
}
