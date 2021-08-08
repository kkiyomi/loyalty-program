import { createStore } from 'vuex'
import user from '../store/modules/user'
import qrmaker from '../store/modules/qrmaker'
import settings from '../store/modules/settings'

const store = createStore({
    modules: {
        settings,
        user,
        qrmaker,
    },
    actions: {
        clearAll({ dispatch }) {
            dispatch("reset")
        },
    }
})

export default store
