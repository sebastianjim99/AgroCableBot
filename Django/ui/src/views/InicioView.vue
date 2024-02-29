<template>
    <!-- CSS de Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" >

    <!-- <div id="app">
       
        <video v-if="showIntroVideo" autoplay muted @ended="hideIntroVideo" class="intro-video">
            <source src="@/assets/logos/moviento_robot.mp4" type="video/mp4">
            Tu navegador no admite la reproducción de video.
        </video>

        <div v-else class="content">
        
        </div>
    </div> -->

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
                <li class="nav-item"><a class="nav-link" href="#Integrantes">Quienes somos</a></li>
                <li class="nav-item"><a class="nav-link" href="#proyectos">productos</a></li>
                <li class="nav-item"><a class="nav-link" href="#Contacto">Contactanos</a></li>
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
<section>
    <div class="container" style=" padding: 20px; display: flex;" >
        <h1 class="somos-title" style="color:white; "> ¿Quiénes somos?</h1>
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
    <div class="container" style=" padding-bottom: 20px; display: flex;"  >
        <h1 class="mision-tittle" style="color:white" > Misión</h1>
    </div>
    
    <div class="container">
        <div class="row">
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
    <div class="container" style="padding-bottom: 20px; justify-content: flex-end; display: flex;">
        <h1 class="vision-tittle" style=" color: white;" >Visión</h1>
    </div>
    
    <div class="container" >
        <div class="row" style="justify-content: center;" >
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


<!--  SECCION DE CONTACTO  -->
<section class="position-relative py-4 py-xl-5">
    <div class="container position-relative">
        <div class="col-md-8 col-xl-6 text-center mx-auto">
            <h2>Contactanos</h2>
        </div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-6 col-lg-4 col-xl-4">
                <div class="d-flex flex-column justify-content-center align-items-start h-100">
                    <div class="d-flex align-items-center p-3">
                        <div class="bs-icon-md bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block bs-icon"><svg class="bi bi-telephone" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"></path>
                            </svg></div>
                        <div class="px-2">
                            <h6 class="mb-0">Celular</h6>
                            <p class="mb-0">+57 310 698 9372 </p>
                        </div>
                    </div>
                    <div class="d-flex align-items-center p-3">
                        <div class="bs-icon-md bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block bs-icon"><svg class="bi bi-envelope" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"></path>
                            </svg></div>
                        <div class="px-2">
                            <h6 class="mb-0">Correo</h6>
                            <p class="mb-0">info@example.com</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-5 col-xl-4">
                <div>
                    <form class="p-3 p-xl-4" method="post">
                        <div class="mb-3"><input id="name-1" class="form-control" type="text" name="name" placeholder="Nombre" /></div>
                        <div class="mb-3"><input id="email-1" class="form-control" type="email" name="email" placeholder="Correo" /></div>
                        <div class="mb-3"><textarea id="message-1" class="form-control" name="message" rows="2" placeholder="Mensaje"></textarea></div>
                        <div><button class="btn btn-primary d-block w-100" type="submit"> Enviar </button></div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>


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


export default{
  name: "imacuna_inicio",
  components:{
        Lineas, 
        Servicios,
        proyectos_imacuna,
        Integrantes,
        footer_imacuna,
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

    .intro-video {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 9999; /* Asegúrate de que el video esté en la parte superior */
    }

    .content {
        display: none; /* Oculta el contenido principal mientras se reproduce el video */
    }



    .mobile-background {

        background-image: url("/src/assets/logos/semillero.jpg");
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        background-position: bottom;
    }
    .video-parallax-container {
        height: 50vh;
        overflow: hidden;
    }

    .swiper2 {
        width: 100%;
        height: 400px;
    }
    .swiper1-slide {
        text-align: center;
        font-size: 18px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: url("/src/assets/logos/Presentacion.jpg");
        background-position: center;
    }

    .swiper2-slide {
        text-align: center;
        font-size: 18px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: url("/src/assets/logos/logo-imacuna.png" );
        background-position: center;
    }


    .title-header{
        text-align: center;
        font-size: 18px;
        justify-content: center;
        align-items: center;
    }

    .swiper3-slide {
        text-align: center;
        font-size: 18px;
        position: relative;
    }

    #bg-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 50%;
    height: 50%;
    object-fit: cover; /* Ajusta el tamaño del video para que cubra el contenedor */
    }

    :root {
        --bs-breakpoint-xs: 0;
        --bs-breakpoint-sm: 576px;
        --bs-breakpoint-md: 768px;
        --bs-breakpoint-lg: 992px;
        --bs-breakpoint-xl: 1200px;
        --bs-breakpoint-xxl: 1400px;
    }

    .navbar-light {
    transition: 1000ms ease;
    background: white
    }

    .navbar {
    border: none;
    background-color: white;
}

    

/* Nav bar  */

.bs-icon {
  --bs-icon-size: .75rem;
  display: flex;
  flex-shrink: 0;
  justify-content: center;
  align-items: center;
  font-size: var(--bs-icon-size);
  width: calc(var(--bs-icon-size) * 2);
  height: calc(var(--bs-icon-size) * 2);
  color: var(--bs-primary);
}

.bs-icon-xs {
  --bs-icon-size: 1rem;
  width: calc(var(--bs-icon-size) * 1.5);
  height: calc(var(--bs-icon-size) * 1.5);
}

.bs-icon-sm {
  --bs-icon-size: 1rem;
}

.bs-icon-md {
  --bs-icon-size: 1.5rem;
}

.bs-icon-lg {
  --bs-icon-size: 2rem;
}

.bs-icon-xl {
  --bs-icon-size: 2.5rem;
}

.bs-icon.bs-icon-primary {
  color: var(--bs-white);
  background: var(--bs-primary);
}

.bs-icon.bs-icon-primary-light {
  color: var(--bs-primary);
  background: rgba(var(--bs-primary-rgb), .2);
}

.bs-icon.bs-icon-semi-white {
  color: var(--bs-primary);
  background: rgba(255, 255, 255, .5);
}

.bs-icon.bs-icon-rounded {
  border-radius: .5rem;
}

.bs-icon.bs-icon-circle {
  border-radius: 50%;
}



</style>

