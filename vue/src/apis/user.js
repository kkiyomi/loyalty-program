import Api from './api'
import store from '../store'

const END_POINT = 'user/auth'

export default {
    info() {
        return Api.get('user/', store.getters.headers)
    },
    register(data) {
        return Api.post(`${END_POINT}/registration/`, data)
    },
    login(data) {
        return Api.post(`${END_POINT}/login/`, data)
    },
    makerInfo() {
        return Api.get('qr/maker/', store.getters.headers)
    },

    getPromo(promo_uid) {
        return Api.get(`qr/promo/${promo_uid}/`, store.getters.headers)
    },
    addPromo(data) {
        return Api.post(`qr/promo/`, data, store.getters.headers)
    },
    deletePromo(promo_uid) {
        return Api.delete(`qr/promo/${promo_uid}/`, store.getters.headers)
    },
    patchPromo(f_data) {
        const promo_uid = f_data.kwargs
        const data = f_data.data
        return Api.patch(`qr/promo/${promo_uid}/`, data, store.getters.headers)
    },

    addPromoInstance(promo_suid) {
        return Api.post(`qr/code/${promo_suid}/`, {})
    },
    getInstance(pinstance_uid) {
        return Api.get(`qr/instance/${pinstance_uid}/`)
    },
    instanceList(promo_uid) {
        return Api.get(`qr/instances/${promo_uid}/`, store.getters.headers)
    },

    transactionList(promo_uid) {
        return Api.get(`qr/transactions/${promo_uid}/`, store.getters.headers)
    },
}