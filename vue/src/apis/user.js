import Api from './Api'
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
    addPromo(maker_uid, data) {
        return Api.post(`qr/maker/${maker_uid}/promo/`, data, store.getters.headers)
    },
    deletePromo(maker_uid, promo_uid) {
        return Api.delete(`qr/promo/${maker_uid}/${promo_uid}/`, store.getters.headers)
    },
    patchPromo(maker_uid, vdata) {
        const promo_uid = vdata.kwargs
        const data = vdata.data
        return Api.patch(`qr/promo/${maker_uid}/${promo_uid}/`, data, store.getters.headers)
    },
}