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
                <div class="bs-icon-lg bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-3 bs-icon lg"><img :src="lineas_investigacion.imagen" height="100" width="100"  alt=""> </div>
                <div class="px-3">
                    <h4 style="text-align:center; font-size: 18px;" > {{lineas_investigacion.nombre}} </h4>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</section>
 <!--  SECCION DE MISION  -->

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

<!--  SECCION DE INTEGRANTES  -->

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


<!--  SECCION DE CONTACTO  -->
<section class="position-relative py-4 py-xl-5">
    <div class="container position-relative">
        <div class="row mb-5">
            <div class="col-md-8 col-xl-6 text-center mx-auto">
                <h2>Contact us</h2>
                <p class="w-lg-50">Curae hendrerit donec commodo hendrerit egestas tempus, turpis facilisis nostra nunc. Vestibulum dui eget ultrices.</p>
            </div>
        </div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-6 col-lg-4 col-xl-4">
                <div class="d-flex flex-column justify-content-center align-items-start h-100">
                    <div class="d-flex align-items-center p-3">
                        <div class="bs-icon-md bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block bs-icon"><svg class="bi bi-telephone" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"></path>
                            </svg></div>
                        <div class="px-2">
                            <h6 class="mb-0">Phone</h6>
                            <p class="mb-0">+123456789</p>
                        </div>
                    </div>
                    <div class="d-flex align-items-center p-3">
                        <div class="bs-icon-md bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block bs-icon"><svg class="bi bi-envelope" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"></path>
                            </svg></div>
                        <div class="px-2">
                            <h6 class="mb-0">Email</h6>
                            <p class="mb-0">info@example.com</p>
                        </div>
                    </div>
                    <div class="d-flex align-items-center p-3">
                        <div class="bs-icon-md bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block bs-icon"><svg class="bi bi-pin" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M4.146.146A.5.5 0 0 1 4.5 0h7a.5.5 0 0 1 .5.5c0 .68-.342 1.174-.646 1.479-.126.125-.25.224-.354.298v4.431l.078.048c.203.127.476.314.751.555C12.36 7.775 13 8.527 13 9.5a.5.5 0 0 1-.5.5h-4v4.5c0 .276-.224 1.5-.5 1.5s-.5-1.224-.5-1.5V10h-4a.5.5 0 0 1-.5-.5c0-.973.64-1.725 1.17-2.189A5.921 5.921 0 0 1 5 6.708V2.277a2.77 2.77 0 0 1-.354-.298C4.342 1.674 4 1.179 4 .5a.5.5 0 0 1 .146-.354zm1.58 1.408-.002-.001.002.001zm-.002-.001.002.001A.5.5 0 0 1 6 2v5a.5.5 0 0 1-.276.447h-.002l-.012.007-.054.03a4.922 4.922 0 0 0-.827.58c-.318.278-.585.596-.725.936h7.792c-.14-.34-.407-.658-.725-.936a4.915 4.915 0 0 0-.881-.61l-.012-.006h-.002A.5.5 0 0 1 10 7V2a.5.5 0 0 1 .295-.458 1.775 1.775 0 0 0 .351-.271c.08-.08.155-.17.214-.271H5.14c.06.1.133.191.214.271a1.78 1.78 0 0 0 .37.282z"></path>
                            </svg></div>
                        <div class="px-2">
                            <h6 class="mb-0">Location</h6>
                            <p class="mb-0">12 Example Street</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-5 col-xl-4">
                <div>
                    <form class="p-3 p-xl-4" method="post">
                        <div class="mb-3"><input id="name-1" class="form-control" type="text" name="name" placeholder="Name" /></div>
                        <div class="mb-3"><input id="email-1" class="form-control" type="email" name="email" placeholder="Email" /></div>
                        <div class="mb-3"><textarea id="message-1" class="form-control" name="message" rows="6" placeholder="Message"></textarea></div>
                        <div><button class="btn btn-primary d-block w-100" type="submit">Send </button></div>
                    </form>
                </div>
            </div>
        </div>
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
    </div>    
    <div class="col-md-5">
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
    

 <!----  seccion Contacto  ---->
                 


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

},
    
      //----------------section Servicios----------------
  }


</script>