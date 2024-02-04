<template>

  <div class="login-card">
        <img class="profile-img-card" src="@/assets/logos/imacuna.png" width="200" height="100" />
        <p class="profile-name-card"> </p>
        <!-- joal, -->
        <form @submit.prevent="submitForm" class="form-signin"><span class="reauth-email"> </span>

            <div v-if="errors.wrong_credentials " class="form-group my-2 text-start">
                <small class="text-danger"> {{errors.wrong_credentials}} </small>
            </div>

            <input id="username" class="form-control"  autocomplete="current-username" type="username" placeholder="Correo" name= "username" v-model="username" />
            <small v-if="errors.username" class="text-danger">{{errors.username}} </small>
            <br> 
            <input id="password" class="form-control"  autocomplete="current-password" type="password"  placeholder="Contraseña" name="password" v-model="password"/>
            <small v-if="errors.password" class="text-danger">{{errors.password}} </small>
            <br>
            <button class="btn btn-primary btn-lg d-block btn-signin w-100" type="submit">Ingresar</button>
        </form>
    </div> 

</template>

<script>
import axios from 'axios';

export default{
    name: 'loginView',
    data(){
        return{
            'api' : 'http://localhost:8000',
            username: "",
            password: "",
            errors:{
                username: "",
                password: "",
                wrong_credentials:""
            }
        }
    },
    methods: {
        isVaidForm(){
            let valid = true;
            if (!this.username){
                this.errors.username = "No puedes dejar en blanco";
            }else{
                this.errors.password = "";
            }
            if(!this.password){
                this.errors.password = "No puedes dejar en blanco";
            }else{
                this.errors.password="";
            }
            if(this.errors.username || this.errors.password){
                valid = false;
            }
            return valid;

        },
        submitForm(){
            //console.log(this.username, this.password);
            if (this.isVaidForm()){
                const url = '/loginView/';
                axios.post(this.api + url, {username: this.username, password: this.password})
                .then(Response=> {
                    //console.log(Response.data);
                    this.$store.commit('setToken', Response.data);
                    this.username = "";
                    this.password = "";
                    this.$router.push('/monitoreo')
                })
                .catch(error  => { 
                    console.log(error)
                    const statusCode = error.response.status;
                    if(statusCode){
                        console.log("Usuario o contraseña incorrecta" + "" + statusCode)
                        this.errors.wrong_credentials = "Usuario o contraseña incorrecta";
                    }else{
                        this.errors.wrong_credentials = "";
                    }
                })
            }else{
                console.log('form no valid')
            }
        },
    },

}

</script>

<style scoped>
    .login-card {
        max-width: 350px;
        padding: 40px 40px;
        background-color: #F7F7F7;
        margin: 0 auto 25px;
        margin-top: 50px;
        border-radius: 2px;
        box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
        }


</style>