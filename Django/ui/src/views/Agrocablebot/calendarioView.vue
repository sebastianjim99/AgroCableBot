<template>
    
    <div class="">
        <navbar_monitoreo />
    </div>
      <!--   titulo control manual   -->
    <section>
        <div>
            <div class="container">
                <div class="row">
                    <div class="col-md-8" style="text-align: center;">
                        <h2 class="divider-style">
                            <span>Tareas programas </span>
                        </h2>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <button class="btn btn-primary d-flex align-items-center align-self-center" type="button" style="height: 38px; background-color: rgb(21,221,4);">Agregar Tarea<svg class="bi bi-plus-circle-fill" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 29px;">
                                <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"></path>
                            </svg></button></div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <table id="example" class="table table-striped table-bordered" cellspacing="0" width="100%">
                            <thead>
                                <tr>
                                    <th>Id</th>
                                    <th>Nombre</th>
                                    <th>Recurrencia</th>
                                    <th>hora</th>
                                    <th>fecha</th>
                                    <th>eliminar</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>01</td>
                                    <td>Regar</td>
                                    <td>Una vez</td>
                                    <td>12:00</td>
                                    <td>01/03/2024</td>
                                    <td>
                                        <button class="btn btn-danger" type="button"><svg class="bi bi-trash" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 20px; ">
                                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"></path>
                                        <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"></path>
                                        </svg>
                                            
                                            
                                            <i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </section>

<!-- 
    <section>
        <div style="text-align: center;">
            <h2 class="divider-style">
                <span> Calendario </span>
            </h2>
        </div>
        <div class="bootstrap_calendar">
            <div class="container py-5">
                <div class="calendar shadow bg-white p-5">
                    <div class="d-flex align-items-center"><i class="fa fa-calendar fa-3x mr-3"></i>
                        <h2 class="month font-weight-bold mb-0 text-uppercase">Febrero 2024</h2>
                    </div>
                    <ol class="day-names list-unstyled">
                        <li class="font-weight-bold text-uppercase">Dom</li>
                        <li class="font-weight-bold text-uppercase">Lun</li>
                        <li class="font-weight-bold text-uppercase">Mar</li>
                        <li class="font-weight-bold text-uppercase">Mie</li>
                        <li class="font-weight-bold text-uppercase">Juv</li>
                        <li class="font-weight-bold text-uppercase">Vie</li>
                        <li class="font-weight-bold text-uppercase">Sab</li>
                    </ol>
                    <ol class="days list-unstyled">
                        <li>
                            <div class="date">1</div>
                            <div class="event bg-success">Regar plantas</div>
                        </li>
                        <li>
                            <div class="date">2</div>
                        </li>
                        <li>
                            <div class="date">3</div>
                        </li>
                        <li>
                            <div class="date">4</div>
                        </li>
                        <li>
                            <div class="date">5</div>
                        </li>
                        <li>
                            <div class="date">6</div>
                        </li>
                        <li>
                            <div class="date">7</div>
                        </li>
                        <li>
                            <div class="date">8</div>
                        </li>
                        <li>
                            <div class="date">9</div>
                        </li>
                        <li>
                            <div class="date">10</div>
                        </li>
                        <li>
                            <div class="date">11</div>
                        </li>
                        <li>
                            <div class="date">12</div>
                        </li>
                        <li>
                            <div class="date">13</div>
                            <div class="event all-day begin span-2 bg-warning">Event Name</div>
                        </li>
                        <li>
                            <div class="date">14</div>
                        </li>
                        <li>
                            <div class="date">15</div>
                            <div class="event all-day end bg-success">Event Name</div>
                        </li>
                        <li>
                            <div class="date">16</div>
                        </li>
                        <li>
                            <div class="date">17</div>
                        </li>
                        <li>
                            <div class="date">18</div>
                        </li>
                        <li>
                            <div class="date">19</div>
                        </li>
                        <li>
                            <div class="date">20</div>
                        </li>
                        <li>
                            <div class="date">21</div>
                            <div class="event bg-primary">Event Name</div>
                            <div class="event bg-success">Event Name</div>
                        </li>
                        <li>
                            <div class="date">22</div>
                            <div class="event bg-info">Event with Longer Name</div>
                        </li>
                        <li>
                            <div class="date">23</div>
                        </li>
                        <li>
                            <div class="date">24</div>
                        </li>
                        <li>
                            <div class="date">25</div>
                        </li>
                        <li>
                            <div class="date">26</div>
                        </li>
                        <li>
                            <div class="date">27</div>
                        </li>
                        <li>
                            <div class="date">28</div>
                        </li>
                        <li>
                            <div class="date">29</div>
                        </li>
                        <li>
                            <div class="date">30</div>
                        </li>
                        <li>
                            <div class="date">31</div>
                        </li>
                        <li class="outside">
                            <div class="date">1</div>
                        </li>
                        <li class="outside">
                            <div class="date">2</div>
                        </li>
                        <li class="outside">
                            <div class="date">3</div>
                        </li>
                        <li class="outside">
                            <div class="date">4</div>
                        </li>
                    </ol>
                </div>
            </div>
        </div>
    </section> -->


    <section>
        
    </section>
    


    <section>
        <footer_imacuna />
    </section>



</template>


<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'

export default{
    components:{
        navbar_monitoreo,
        footer_imacuna,
       
    }
}
</script>