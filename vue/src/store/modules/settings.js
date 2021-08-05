export default {
    state: () => ({
        signupIsOpen: false,
        signinIsOpen: false,
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
    },

    actions: {
    },
}
