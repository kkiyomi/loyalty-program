import { createStore } from 'vuex'
import user from '../store/modules/user'
import qrmaker from '../store/modules/qrmaker'

const store = createStore({
    modules: {
        user,
        qrmaker,
    },
})

export default store
