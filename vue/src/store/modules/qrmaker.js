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
        async AddPromo({ dispatch, state }, data) {
            const maker_uid = state.maker.uid
            await user.addPromo(maker_uid, data).then(() => {
                dispatch('getMaker')
            })
        },
        async DeletePromo({ dispatch, state }, promo_uid) {
            const maker_uid = state.maker.uid
            await user.deletePromo(maker_uid, promo_uid).then(() => {
                dispatch('getMaker')
            })
        },
        async PatchPromo({ dispatch, state }, data) {
            const maker_uid = state.maker.uid
            await user.patchPromo(maker_uid, data).then(() => {
                dispatch('getMaker')
            })
        },

    },
}
