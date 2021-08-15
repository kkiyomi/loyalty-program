import Cookies from 'js-cookie'
import user from '../../apis/user'


export default {
    state: () => ({
        maker: null,
        instance: null,
        promos: [],
        instanceList: [],
        transactionList: [],
        promo: null,
    }),

    getters: {
        promos(state) {
            return state.promos
        },
        promo: (state) => (uid) => {
            return state.promos.find((element) => element.uid == uid)
        },
        promoInstanceCookie(state) {
            return {
                promo_suid: state.instance.promo.suid,
                pinstance_uid: state.instance.uid,
            }
        }
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
        SET_INSTANCE(state, payload) {
            state.instance = payload
        },
        SET_TRANSACTION_LIST(state, payload) {
            state.transactionList = payload
        },
        SET_PROMO(state, payload) {
            state.promo = payload
        },
    },

    actions: {
        reset({ commit }) {
            commit('SET_MAKER', null)
            commit('SET_PROMOS', [])
            commit('SET_INSTANCE_LIST', [])
            commit('SET_TRANSACTION_LIST', [])
        },


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


        async getPromo({ commit }, promo_uid) {
            await user.getPromo(promo_uid).then((response) => {
                commit('SET_PROMO', response.data)
            })
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


        async getInstance({ commit }, pinstance_uid) {
            await user.getInstance(pinstance_uid).then((response) => {
                commit('SET_INSTANCE', response.data)
            })
        },
        async addPromoInstance({ commit }, promo_suid) {
            await user.addPromoInstance(promo_suid).then(async (response) => {
                commit('SET_INSTANCE', response.data)
            })
        },
        async getPromoInstanceCookie({ dispatch }, promo_suid) {
            const pr_instance = Cookies.get(promo_suid)
            if (pr_instance != undefined) {
                await dispatch('getInstance', pr_instance)
            }
        },
    },
}
