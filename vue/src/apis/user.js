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
}