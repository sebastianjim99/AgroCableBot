<template>

  <div class="login-card">
        <img class="profile-img-card" src="@/assets/logos/imacuna.png" width="200" height="100" />
        <p class="profile-name-card"> </p>
        <!-- joal, -->
        <form @submit.prevent="submitForm" class="form-signin"><span class="reauth-email"> </span>

            <div v-if="errors.wrong_credentials " class="form-group my-2 text-start">
                <small class="text-danger"> {{errors.wrong_credentials}} </small>
            </div>

            <input id="username" class="form-control"   type="username" placeholder="Correo" name= "username" v-model="username" />
            <small v-if="errors.username" class="text-danger">{{errors.username}} </small>
            <br> 
            <input id="password" class="form-control"   type="password"  placeholder="Contraseña" name="password" v-model="password"/>
            <small v-if="errors.password" class="text-danger">{{errors.password}} </small>
            <br> 
            <input id="password2" class="form-control"   type="password"  placeholder="confirmar contraseña" name="password2" v-model="password2"/>
            <small v-if="errors.password" class="text-danger">{{errors.password}} </small>
            <br>
            <button class="btn btn-primary btn-lg d-block btn-signin w-100" type="submit">Registrarse</button>
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
            password2: "",
            errors:{
                username: "",
                password: "",
                password2: "",
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
            if(this.password && this.password2 && this.password != this.password2 ){
                this.errors.password = "Las contraseñas no coinciden";
            }else{
                this.errors.password="";
            }
            if(this.errors.username || this.errors.password || this.errors.password2){
                valid = false;
            }
            return valid;

        },
        submitForm(){
            if (this.isVaidForm()){
                const url = '/auth/users/';
                axios.post(this.api + url, {username: this.username, password: this.password})
                .then(Response=> {
                    console.log(Response.data);
                    this.username = "";
                    this.password = "";
                    this.password2 = "";
                    console.log("Usuario creado correctamente")
                    this.$router.push('/loginview')
                })
                .catch(error  => { 
                    console.log(error.response.data)
                    if (error.response.data.username){
                        this.errors.username = "Un usuario con ese nombre ya existe."
                    }else{
                         this.errors.username = "";
                         this.$router.push('/loginview')
                    }
                })
            }else{
                console.log('form no valid');
                console.log(this.errors);
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