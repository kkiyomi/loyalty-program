import user from '../../apis/user'

export default {
    state: () => ({
        maker: null,
    }),

    getters: {
        promos(state) {
            return state.maker.promos
        }
    },

    mutations: {
        SET_MAKER(state, payload) {
            state.maker = payload
        },
    },

    actions: {
        async getMaker({ commit }) {
            await user.makerInfo().then(response => {
                const maker = response.data
                commit('SET_MAKER', maker)
            })
        },
        delMaker({ commit }) {
            commit('SET_MAKER', null)
        },

    },
}
