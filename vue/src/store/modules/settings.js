export default {
    state: () => ({
        signupIsOpen: false,
        signinIsOpen: false,
        codeIsOpen: '',
        promoEditing: '',
        notiIsOpen: false,
    }),

    getters: {
    },

    mutations: {
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

    },

    actions: {
        reset({ commit }) {
            commit('SET_SIGNUP_DIALOG', false)
            commit('SET_SIGNIN_DIALOG', false)
            commit('SET_NOTI_DIALOG', false)
            commit('SET_CODE_DIALOG', null)
            commit('SET_PROMO_EDITING', null)
        },
        setToast({ commit }, payload) {
            commit('SET_NOTI_DIALOG', payload)
        }
    },
}
