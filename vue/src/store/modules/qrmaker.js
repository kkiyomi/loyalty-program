import user from '../../apis/user'

export default {
    state: () => ({
        maker: null,
        promos: [],
        instanceList: [],
        transactionList: [],
    }),

    getters: {
        promos(state) {
            return state.promos
        },
        promo: (state) => (uid) => {
            return state.promos.find((element) => element.uid == uid)
        },
    },

    mutations: {
        SET_MAKER(state, payload) {
            state.maker = payload
        },
        SET_PROMOS(state, payload) {
            state.promos = payload
        },
        SET_INSTANCE_LIST(state, payload) {
            state.instanceList = payload
        },
        SET_TRANSACTION_LIST(state, payload) {
            state.transactionList = payload
        },
    },

    actions: {
        async getMaker({ commit }) {
            await user.makerInfo().then(response => {
                const maker = response.data
                commit('SET_MAKER', maker)
                commit('SET_PROMOS', maker.promos)
            })
        },
        delMaker({ commit }) {
            commit('SET_MAKER', null)
        },
        async AddPromo({ dispatch }, data) {
            await user.addPromo(data).then(() => {
                dispatch('getMaker')
            })
        },
        async DeletePromo({ dispatch }, promo_uid) {
            await user.deletePromo(promo_uid).then(() => {
                dispatch('getMaker')
            })
        },
        async PatchPromo({ dispatch }, data) {
            await user.patchPromo(data).then(() => {
                dispatch('getMaker')
            })
        },
        async getInstanceList({ commit }, promo_uid) {
            await user.instanceList(promo_uid).then((response) => {
                commit('SET_INSTANCE_LIST', response.data)
            })
        },
        async getTransactionList({ commit }, promo_uid) {
            await user.transactionList(promo_uid).then((response) => {
                commit('SET_TRANSACTION_LIST', response.data)
            })
        },

    },
}
