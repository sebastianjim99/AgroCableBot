import { createStore } from 'vuex'

const store =  createStore({

    state:{
        token:"",
        user_id:"",
        IsAuthenticated: false
    },
    getters:{

    },
    mutations:{
        initializeStore(state){
            if (localStorage.getItem('token')){
                console.log("Configurando Token", state.user_id);
                state.token = localStorage.getItem('token');
                state.user_id = localStorage.getItem('user_id');
                state.IsAuthenticated = true;
            }else{
                state.IsAuthenticated = false;
            }

        },
        setToken(state, data){
            state.token = data.token;
            state.user_id = data.user_id;
            localStorage.setItem('token', data.token);
            localStorage.setItem('user_id', data.user_id);
            state.IsAuthenticated = true
        },
        removeToken(state){
            state.token = '';
            state.user_id = '';
            localStorage.removeItem('token');
            localStorage.removeItem('user_id');
            state.IsAuthenticated = false; 
        }

    },
    actions:{

    },
    modules:{

    },


})

export default store