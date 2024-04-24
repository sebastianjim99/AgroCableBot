<template>
    <!-- CSS de Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" >

    <div id="app">    
        <video v-if="showIntroVideo" autoplay muted @ended="hideIntroVideo" class="intro-video">
            <source src="@/assets/logos/intro.mp4" type="video/mp4">
            Tu navegador no admite la reproducción de video.
        </video>
    </div>

    <nav class="navbar navbar-expand-md bg-body py-3">
            <div class="container">
                <img src="@/assets/logos/imacuna.png" width="140" height="60" style="text-align: left;position: static;display: flex;" />
                <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navcol-3">
                    <span class="visually-hidden">Toggle navigation</span>
                    <span class="navbar-toggler-icon"> 
                    </span>
                </button>
                <div id="navcol-3" class="collapse navbar-collapse text-center">
                    <ul class="navbar-nav mx-auto justify-content-center">
                        <li class="nav-item"><a class="nav-link active" href="#">Inicio</a></li>
                        <li class="nav-item"><a class="nav-link" href="#Quienes_somos">Quienes somos</a></li>
                        <li class="nav-item"><a class="nav-link" href="#proyectos">Productos</a></li>
                        <li class="nav-item"><a class="nav-link" href="#Contacto">Contáctanos</a></li>
                    </ul>
                    <a class="btn" type="button" href="loginView" style="background-color: #FB6542; color: white">Ingresar</a>
                </div>
            </div>
            </nav>

            <!-- Seccion presentacion de la pagina web -->
        <section>
            <div id="videoContainer" class="mobile-background">
                <div class="container-fluid d-flex justify-content-center align-items-center align-content-center video-parallax-container">
                    <div class="row">
                    </div>
                </div>
            </div>
        </section>

        <!--  SECCION DE QUIENES  -->
        <section id="Quienes_somos" >
            <div class="container" style=" padding: 10px; justify-content: center; display: flex; " >
                <h1 class="somos-title"  > ¿Quiénes somos?</h1>
            </div> 
            
            <div class="container">
                <div class="row" style="position: static; text-align: center; margin: 10px " >
                    <div class="col-md-6 col-xl-3"><img width="150" height="150" src="@/assets/logos/Introduccion_robot.png" style="width: 200 px;padding-top: 0px;margin-top: 10px;" /></div>
                    <div class="col-md-6 col-xl-8">
                        <p class="text-somos" >Somos el semillero de investigación IMACUNA, un grupo de ingenieros entusiastas por impulsar la innovación y la modernización de la agricultura, en beneficio de productores y consumidores.<br /><strong>“Somos el futuro agrícola”</strong>.</p>
                    </div>
                </div>
            </div>
        </section>

        <br>
        <br>

        <div class="Lineas">
            <Lineas />
        </div>

        <div class="servicios">
            <Servicios />
        </div>

        <br>
        <br>

        <!--  SECCION DE MISION  -->
        <section>
            <div class="container" style=" padding-bottom: 20px; display: flex; justify-content: center; "  >
                <h1 class="mision-tittle" > Misión</h1>
            </div>
            
            <div class="container">
                <div class="row d-flex justify-content-around ">
                    <div class="col-md-6 col-xl-3"> 
                        <img width="170" height="170" src="@/assets/logos/mision.png" style="height: 100vh,  " />
                    </div>
                    
                    <div class="col-md-6 col-xl-8">
                        <p class="text-mis-vis">Fortalecer las habilidades investigativas de los estudiantes de Ingeniería Mecánica, Electrónica, Industrial y Sistemas de la Universidad de Ibagué en la Ingeniería Aplicada, siendo un grupo proactivo en todos sus campos de acción, brindando soluciones a las problemáticas del entorno académico e industrial y mejorando de esta forma la calidad de los profesionales de Ingeniería durante el transcurso de su formación universitaria.</p>
                    </div>
                </div>
            </div>
        </section>

        <!--  SECCION DE VISIÓN  -->
        <section>
            <div class="container" style="padding-bottom: 20px; justify-content: center; display: flex;">
                <h1 class="vision-tittle" >Visión</h1>
            </div>
            
            <div class="container" >
                <div class="row d-flex justify-content-around " >
                    <div class="col-md-6 col-xl-6">
                        <p class="text-mis-vis" >Ser un semillero líder en el campo del diseño mecatrónico, reconocido a nivel regional, nacional e internacional por la calidad de sus proyectos de investigación, su constante aporte a la investigación de la universidad y al aporte al conocimiento de sus integrantes.</p>
                    </div>
                    <div class="col-md-6 col-xl-3"> <img width="170" height="170" src="@/assets/logos/vision.png" style="" /></div>
                </div>
            </div>
        </section>

        <!--  SECCION DE PROYECTOS  -->
        <section>
        <div class="proyectos_imacuna" id="proyectos">
            <proyectos_imacuna /> 
            </div>
        </section>

        <!--  SECCION DE INTEGRANTES  -->
        <section class="py-4 py-xl-5" id="Integrantes">
        <div class="integrantes">
            <Integrantes /> 
            </div>
        </section>


        <div class="">
            <contacto_soporte />
        </div>

        <section id="Contacto">
            <footer_imacuna />
        </section>

</template>

<script> 
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';


import Lineas from '../components/imacuna/Lineas.vue'
import Servicios from '../components/imacuna/Servicios.vue'
import proyectos_imacuna from '@/components/imacuna/proyectos_imacuna.vue'
import Integrantes from '../components/imacuna/Integrantes.vue'
import footer_imacuna from '../components/footer.vue'
import contacto_soporte from '/src/components/agrocablebot/soporte/contactoSoporte.vue'


export default{
  name: "imacuna_inicio",
  components:{
        Lineas, 
        Servicios,
        proyectos_imacuna,
        Integrantes,
        footer_imacuna,
        contacto_soporte,
    },

    data() {
        return {
            showIntroVideo: true
        };
    },
    methods: {
        hideIntroVideo() {
            this.showIntroVideo = false;
        }
    },
}
</script>

<style>
   

</style>

