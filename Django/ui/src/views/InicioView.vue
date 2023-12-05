<template>

<nav class="navbar navbar-expand-md bg-body">
    <div class="container-fluid"><button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navcol-1"><span class="visually-hidden">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
        <div id="navcol-1" class="collapse navbar-collapse text-center" style="width: initial;"><img class="img-fluid" src="@/assets/logos/imacuna.png" width="171" height="76" loading="auto" style="margin-left: 60px;" />
            <ul class="navbar-nav mx-auto">
                <li class="nav-item"><a class="nav-link active" href="#">Inicio</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Quienes somos</a></li>
                <li class="nav-item"><a class="nav-link" href="#">productos</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Contactanos</a></li>
            </ul><button class="btn btn-primary" type="button" style="border-radius: 10;border-style: solid;margin-left: 2px;margin-right: 102px;">Ingresar</button>
        </div>
    </div>
</nav>

 <!--  SECCION DE QUIENES  -->
<section>
    <h1 style="position: static;text-align: left;margin: 40px;">¿Quiénes somos?</h1>
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-xl-3"><img width="214" height="202" src="@/assets/media/iconos/Introduccion_robot.png" style="width: 200 px;padding-top: 0px;margin-top: 38px;" /></div>
            <div class="col-md-6 col-xl-8">
                <p style="color: var(--bs-emphasis-color);text-align: center;transform: perspective(0px);margin-top: 19px;margin-left: 19px;margin-right: -1px;padding-left: 4px;font-size: 30px;">Somos el semillero de investigación IMACUNA, un grupo de ingenieros entusiastas por impulsar la innovación y la modernización de la agricultura, en beneficio de productores y consumidores.<br />“Somos el futuro agrícola”.</p>
            </div>
        </div>
    </div>
</section>

<br>
<br>
 <!--  SECCION DE LINEAS DE INVESTIGACIÓN -->
<section>
    <div>
        <div class="container">
          <h1>Líneas de investigación</h1>
        </div>
        <div class="container py-4 py-xl-5">  
          <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3 row-cols-xl-4">
            <div class="col" v-for ="lineas_investigacion in Lineas_investigacion" :key="lineas_investigacion.id" >
              <div class="text-center d-flex flex-column align-items-center align-items-xl-center">
                <div class="bs-icon-lg bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-3 bs-icon lg"><img src="@/assets/logo.png" height="100" width="100"  alt=""> </div>
                <div class="px-1">
                    <h4 style="text-align:center; font-size: 18px;" > {{lineas_investigacion.nombre}} </h4>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</section>
 <!--  SECCION DE SERVICIOS -->
<section>
    <div>
        <div class="container">
            <h1>Servicios</h1>
        </div>
        <div class="container py-4 py-xl-5">  
          <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3 row-cols-xl-4">
            <div class="col" v-for ="lineas_investigacion in Lineas_investigacion" :key="lineas_investigacion.id" >
              <div class="text-center d-flex flex-column align-items-center align-items-xl-center">
                <div class="bs-icon-lg bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-3 bs-icon lg"><img src="@/assets/logo.png" height="100" width="100"  alt=""> </div>
                <div class="px-3">
                    <h4 style="text-align:center; font-size: 18px;" > {{lineas_investigacion.nombre}} </h4>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</section>
 <!--  SECCION DE MISISION  -->

<section>
    <h1 style="position: static;text-align: left;margin: 40px;">MISIÓN</h1>
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-xl-3"><img width="214" height="202" src="@/assets/media/iconos/Introduccion_robot.png" style="width: 200 px;padding-top: 0px;margin-top: 38px;" /></div>
            <div class="col-md-6 col-xl-8">
                <p style="color: var(--bs-emphasis-color);text-align: center;transform: perspective(0px);margin-top: 19px;margin-left: 19px;margin-right: -1px;padding-left: 4px;font-size: 30px;">Somos el semillero de investigación IMACUNA, un grupo de ingenieros entusiastas por impulsar la innovación y la modernización de la agricultura, en beneficio de productores y consumidores.<br />“Somos el futuro agrícola”.</p>
            </div>
        </div>
    </div>
</section>

 <!--  SECCION DE VISIÓN  -->
<section>
    <h1 style="position: static;text-align: left;margin: 40px;">MISIÓN</h1>
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-xl-3"><img width="214" height="202" src="@/assets/media/iconos/Introduccion_robot.png" style="width: 200 px;padding-top: 0px;margin-top: 38px;" /></div>
            <div class="col-md-6 col-xl-8">
                <p style="color: var(--bs-emphasis-color);text-align: center;transform: perspective(0px);margin-top: 19px;margin-left: 19px;margin-right: -1px;padding-left: 4px;font-size: 30px;">Somos el semillero de investigación IMACUNA, un grupo de ingenieros entusiastas por impulsar la innovación y la modernización de la agricultura, en beneficio de productores y consumidores.<br />“Somos el futuro agrícola”.</p>
            </div>
        </div>
    </div>
</section>

 <!--  SECCION DE PROYECTOS  -->

<div class="container">
  <div>
    <h1>PROEYECTOS</h1>
  </div>
      <div class="row">
        <div class="col-md-4">
          <div class="card mb-4 box-shadow">
            <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22208%22%20height%3D%22225%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20208%20225%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_18c3692fba8%20text%20%7B%20fill%3A%23eceeef%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A11pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_18c3692fba8%22%3E%3Crect%20width%3D%22208%22%20height%3D%22225%22%20fill%3D%22%2355595c%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2266.9453125%22%20y%3D%22117.3%22%3EThumbnail%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" data-holder-rendered="true" style="height: 225px; width: 100%; display: block;">
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-4 box-shadow">
            <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22208%22%20height%3D%22225%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20208%20225%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_18c3692fba9%20text%20%7B%20fill%3A%23eceeef%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A11pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_18c3692fba9%22%3E%3Crect%20width%3D%22208%22%20height%3D%22225%22%20fill%3D%22%2355595c%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2266.9453125%22%20y%3D%22117.3%22%3EThumbnail%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" data-holder-rendered="true" style="height: 225px; width: 100%; display: block;">
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card mb-4 box-shadow">
            <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22208%22%20height%3D%22225%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20208%20225%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_18c3692fbaa%20text%20%7B%20fill%3A%23eceeef%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A11pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_18c3692fbaa%22%3E%3Crect%20width%3D%22208%22%20height%3D%22225%22%20fill%3D%22%2355595c%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2266.9453125%22%20y%3D%22117.3%22%3EThumbnail%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" data-holder-rendered="true" style="height: 225px; width: 100%; display: block;">
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-4 box-shadow">
            <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22208%22%20height%3D%22225%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20208%20225%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_18c3692fbab%20text%20%7B%20fill%3A%23eceeef%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A11pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_18c3692fbab%22%3E%3Crect%20width%3D%22208%22%20height%3D%22225%22%20fill%3D%22%2355595c%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2266.9453125%22%20y%3D%22117.3%22%3EThumbnail%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" data-holder-rendered="true" style="height: 225px; width: 100%; display: block;">
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-4 box-shadow">
            <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22208%22%20height%3D%22225%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20208%20225%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_18c3692fbab%20text%20%7B%20fill%3A%23eceeef%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A11pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_18c3692fbab%22%3E%3Crect%20width%3D%22208%22%20height%3D%22225%22%20fill%3D%22%2355595c%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2266.9453125%22%20y%3D%22117.3%22%3EThumbnail%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" data-holder-rendered="true" style="height: 225px; width: 100%; display: block;">
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>

      
        <div class="col-md-4">
          <div class="card mb-4 box-shadow">
            <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22208%22%20height%3D%22225%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20208%20225%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_18c3692fbac%20text%20%7B%20fill%3A%23eceeef%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A11pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_18c3692fbac%22%3E%3Crect%20width%3D%22208%22%20height%3D%22225%22%20fill%3D%22%2355595c%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2266.9453125%22%20y%3D%22117.3%22%3EThumbnail%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" data-holder-rendered="true" style="height: 225px; width: 100%; display: block;">
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

<!--  SECCION DE integrantes  -->

<section class="py-4 py-xl-5">
    <div class="container">
      <div>
        <h1>INTEGRANTES</h1>
      </div>
        <div class="row">
            <div class="col-sm-6 col-lg-4 mb-4 text-center"><img class="rounded-circle img-fluid d-block mx-auto" src="@/assets/media/perfiles/perfil.jpeg" />
                <h3 class="m-0">John Smith</h3>
                <h5 class="my-1">Job Title</h5>
                <p>What does this team member to? Keep it short! This is also a great spot for social links!</p>
            </div>
            <div class="col-sm-6 col-lg-4 mb-4 text-center"><img class="rounded-circle img-fluid d-block mx-auto" src="@/assets/media/perfiles/perfil.jpeg" />
                <h3 class="m-0">John Doe</h3>
                <h5 class="my-1">Job Title</h5>
                <p>What does this team member to? Keep it short! This is also a great spot for social links!</p>
            </div>
            <div class="col-sm-6 col-lg-4 mb-4 text-center"><img class="rounded-circle img-fluid d-block mx-auto" src="@/assets/media/perfiles/perfil.jpeg" />
                <h3 class="m-0">Jane Doe</h3>
                <h5 class="my-1">Job Title</h5>
                <p>What does this team member to? Keep it short! This is also a great spot for social links!</p>
            </div>
          </div>
          
      <div class="container"></div>
    <div class="bg-dark border rounded border-0 border-dark overflow-hidden"></div>
  </div>
</section>




    <div class="container-fluid"> 
        <div class="row">
            <div class="col-md-7"> 
              <div class="col">
                <a name="" id="" class="btn btn-primary" href="Crear" role="button"> Agregar </a>
                <h2 class="alert alert-success">Lineas de investigacion</h2>
              </div>
                <table class="table table-bordered mt-4">
                  <thead>
                    <tr>
                      <th scope="col">Nombre</th>
                      <th scope="col">imagen</th>
                      <th scope="col">Accion</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for ="lineas_investigacion in Lineas_investigacion" :key="lineas_investigacion.id" > 
                      <td>{{ lineas_investigacion.nombre }}</td>
                      <td>{{ lineas_investigacion.imagen }}</td>
                      <td> 
                        <a name="edit" id="" class="btn btn-primary" @click="editData(lineas_investigacion.id)" role="button"> Editar </a> 
                        <br> 
                        <a name="delete" id="" class="btn btn-primary" @click="deleteData(lineas_investigacion.id)" role="button"> Borrar</a> 
                      </td>
                      
                    </tr>
                  </tbody>
                </table>

                <div class="col-md-5">
                  </div>
                    <h2 class="alert alert-info">Crear nueva linea</h2>
                
                      <div class="row">
                        <div class="form-group">

                          <label for="chartfieldName">Nombre:</label>
                          <input type="text" id="chartfieldName" v-model="lineas_investigacion.nombre"/>
                        </div>
                      </div>
                      <div class="col">
                        <div class="form-group" >
                          <!-- Input para seleccionar una imagen -->
                          <label for="image">Imagen:</label>
                          <input type="file" @change="handleFileChange" />
                          <button @click="createData">Crear Datos</button>
                        </div>
                      </div>
                  
                  </div>
              </div>
            </div>
                
          <div>        
        </div>      

                 <!----  seccion Servicios   ---->


</template>




<script>

  



import axios from 'axios'
import FormData from 'form-data'

export default{
  data(){
    return{
      Lineas_investigacion:[],
      currentLineas: {},
      'api' : 'http://localhost:8000/api',
      'lineas_investigacion':{
          'nombre': '',
          'imagen': null,
      },
    }
  },
  

  mounted(){
  console.log('DOM rendered')
  this.getLineas_investigacion()
  },

  created(){
  console.log('DOM creadted')
  },

  methods : {

      getLineas_investigacion(){
      axios.get(this.api + /Lineas_investigacion/ ).then(
        Response => {
          console.log(Response.data)
          this.Lineas_investigacion = Response.data;
          const data = Response.data;
          if (this.isURL(data.imagen)) {
            this.lineas_investigacion.imagen = data.imagen;
          } else {
            // Si es un dato base64, puedes asignarlo directamente
            this.lineas_investigacion.imagen = data.imagen;
          }
        }
      ).catch(error =>{
        console.error(error)
      })
      },

      handleFileChange(event) {
      // Obtener el archivo seleccionado
       this.lineas_investigacion.imagen = event.target.files[0];
       this.lineas_investigacion.imagen = URL.createObjectURL(this.fileImage);
      },

      createData() {
      // Crear un objeto FormData para enviar el nombre y la imagen
      const formData = new FormData();

      const requestData = {
      nombre: this.lineas_investigacion.nombre,
      imagen: formData.append("image", this.lineas_investigacion.imagen)
      };

      // Enviar el formulario al backend
      axios.post(this.api + /Lineas_investigacion/, requestData)
        .then(response => {
          console.log("Datos subidos exitosamente", response.data);
          this.getLineas_investigacion()
          this.lineas_investigacion ={}
        })
        .catch(error => {
          console.error("Error al subir los datos", error);
        });
        
    },

    editData(id) {
      // Redirige a la página de edición con el ID del dato
      this.$router.push(`/editar/${id}`);
    },

    deleteData(id) {
      axios.delete(this.api + `/Lineas_investigacion/${id}/`).then(
        response => {
          console.log('Datos eliminados exitosamente', response.data);
          this.getLineas_investigacion(); // Actualiza la lista después de la eliminación
        })
        .catch(error => {
          console.error('Error al eliminar los datos', error);
        });
    },

    isURL(str) {
      // Verifica si la cadena es una URL válida
      const pattern = new RegExp('^(https?:\\/\\/)?' +
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' +
        '((\\d{1,3}\\.){3}\\d{1,3}))' +
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' +
        '(\\?[;&a-z\\d%_.~+=-]*)?' +
        '(\\#[-a-z\\d_]*)?$','i');
      return !!pattern.test(str);
    },

    /**
   * Clients Slider
   */},
    
      //----------------section Servicios----------------
  }


</script>