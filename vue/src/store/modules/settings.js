export default {
    state: () => ({
        signupIsOpen: false,
        signinIsOpen: false,
        promoEditing: ''
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
        SET_PROMO_EDITING(state, payload) {
            state.promoEditing = payload
        },
    },

    actions: {
    },
}
