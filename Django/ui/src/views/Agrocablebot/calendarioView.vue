<template>
    
    <div class="">
        <navbar_monitoreo />
    </div>
      <!--   titulo control manual   -->
    <section>
        <listaTareasProgramadas/>
    </section>
    <section>
        <ejecucionTareas/>
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
        <vistaCalendario/>
    </section>
    


    <section>
        <footer_imacuna />
    </section>



</template>


<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'
import vistaCalendario from '/src/components/agrocablebot/calendario/vistaCalendario.vue'
import listaTareasProgramadas from '/src/components/agrocablebot/calendario/listaTareasProgramadas.vue'
import ejecucionTareas from '/src/components/agrocablebot/calendario/ejecucionTareas.vue'

export default{
    components:{
        navbar_monitoreo,
        footer_imacuna,
        vistaCalendario,
        listaTareasProgramadas,
        ejecucionTareas,
       
    }
}
</script>