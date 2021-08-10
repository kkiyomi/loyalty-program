import Cookies from 'js-cookie'

const initState = {
    darkMode: true,
    signupIsOpen: false,
    signinIsOpen: false,
    codeIsOpen: '',
    promoEditing: '',
    notiIsOpen: false,
    promos: {}
}
export default {
    state: () => ({
        darkMode: true,
        signupIsOpen: false,
        signinIsOpen: false,
        codeIsOpen: '',
        promoEditing: '',
        notiIsOpen: false,
        promos: {}
    }),

    getters: {
    },

    mutations: {
        SET_DARKMODE(state, payload) {
            state.darkMode = payload
        },
        SET_SIGNUP_DIALOG(state, payload) {
            state.signupIsOpen = payload
        },
        SET_SIGNIN_DIALOG(state, payload) {
            state.signinIsOpen = payload
        },
        SET_CODE_DIALOG(state, payload) {
            state.codeIsOpen = payload
        },
        SET_NOTI_DIALOG(state, payload) {
            state.notiIsOpen = payload
        },
        SET_PROMO_EDITING(state, payload) {
            state.promoEditing = payload
        },
        ADD_PROMOS(state, payload) {
            state.promos[payload.A] = payload.B
        },
        RESET(state) {
            //
        }

    },

    actions: {
        reset({ commit }) {
            commit('RESET')
        },
        setDarkmode({ commit, dispatch }, dark) {
            commit('SET_DARKMODE', dark)
            let theme = 'light'
            if (dark) {
                theme = 'dark'
            }
            dispatch('setThemeCookie', theme)
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

        setToast({ commit }, payload) {
            commit('SET_NOTI_DIALOG', payload)
        },

        deleteAllCookies({ dispatch }) {
            const all_cookies = Cookies.get()
            for (var key in all_cookies) {
                dispatch('delPromoInstanceCookie', key)
            }
        },
        setToStateAllCookies({ commit }) {
            const all_cookies = Cookies.get()
            for (var key in all_cookies) {
                if (key != 'at' && key != 'theme') {
                    commit('ADD_PROMOS', { A: key, B: all_cookies[key] })
                }
            }
        },
        getCookies({ dispatch }) {
            dispatch('getUserCookie')
            dispatch('getThemeCookie')
        },
        getUserCookie({ commit, dispatch }) {
            const token = Cookies.get('at')
            if (token != undefined) {
                commit('SET_TOKEN', token)
            }
        },
        setUserCookie({ }, token) {
            Cookies.set('at', token, { secure: true })
        },
        delUserCookie({ }) {
            Cookies.remove('at')
        },
        delUserCookie({ }) {
            Cookies.remove('at')
        },

        setPromoInstanceCookie({ }, data) {
            Cookies.set(data.promo_suid, data.pinstance_uid, { secure: true })
        },
        delPromoInstanceCookie({ }, promo_suid) {
            Cookies.remove(promo_suid)
        },
    },
}
