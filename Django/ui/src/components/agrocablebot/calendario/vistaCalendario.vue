<template>
  <div class=" container calendario-container ">
    <div class="row justify-content-center ">
      <div class="col-12">
        <h1 class="fc-header-toolbar-title text-center">Calendario de Tareas</h1>
        <FullCalendar :options='calendarOptions'>
          <template v-slot:eventContent='arg'>
            <b>{{ arg.timeText }}</b>
            <i>{{ arg.event.title }}</i>
          </template>
        </FullCalendar>  
      </div>
    </div>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import axios from 'axios'
export default {
  components: {
    FullCalendar // Hace que la etiqueta <FullCalendar> esté disponible
  },
  name: "vistaCalendario",
  data() {
    return {
      'api' : `${process.env.VUE_APP_API_URL}`,
      calendarOptions: {
        plugins: [
          dayGridPlugin,
          timeGridPlugin,
          interactionPlugin // Necesario para dateClick
        ],
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        initialView: 'timeGridWeek', // Cambia la vista inicial a timeGridWeek
        allDaySlot: true, // Muestra todos los días de la semana en la vista semanal
        slotMinTime: "00:00:00", // Define la hora mínima visible en la vista diaria y semanal
        slotMaxTime: "24:00:00", // Define la hora máxima visible en la vista diaria y semanal
        slotDuration: "00:30:00", // Define la duración de cada intervalo de tiempo
        weekends: true, // Muestra los fines de semana
        events: [] // Las tareas se cargarán dinámicamente más adelante
      }
    }
  },
  mounted() {
    this.obtenerTareas(); // Llama a la función para obtener las tareas al montar el componente
  },
  methods: {
    obtenerTareas() {
      this.eliminarEventosAntiguos() // Llama al método para eliminar eventos antiguos
          .then(() => {
            axios.get(this.api + '/api/calendarios')  // Endpoint para obtener las tareas
              .then(response => {
                const eventos = this.parsearEventos(response.data);
                this.calendarOptions.events = eventos; // Actualiza la lista de eventos del calendario
                this.events = eventos; // Almacena los eventos obtenidos
              })
              .catch(error => {
                console.error(error);
              });
            })
          .catch(error => {
            console.error('Error al eliminar eventos antiguos:', error);
          });
      },

    parsearEventos(tareas) {
      return tareas.flatMap(tarea => {
        const eventos = [];
        const intervalo = tarea.intervalo || 1;
        const horasRepeticion = [tarea.hora_repeticion_1, tarea.hora_repeticion_2, tarea.hora_repeticion_3].filter(hora => hora !== "00:00:00");
        
        let fechaInicio = new Date(tarea.fecha_inicio  + 'T00:00:00');
        // console.log("Fecha de inicio de tarea:", tarea.fecha_inicio);
        // console.log("Fecha de inicio asignada:", fechaInicio);
        let fechaFin = new Date(tarea.fecha_fin + 'T00:00:00');
        // console.log("Fecha de fin asignada:", fechaFin);

        let fecha = new Date(fechaInicio);
        // console.log("fecha",fecha)
        switch (tarea.repeticion) {
          case 'D':
            while (fecha <= fechaFin) {
              horasRepeticion.forEach(hora => {
                eventos.push({
                  title: tarea.nombre,
                  start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                  allDay: false
                });
                const evento = {
                    title: tarea.nombre,
                    start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
              });
              let nuevaFecha = new Date(fecha);
              nuevaFecha.setDate(nuevaFecha.getDate() + intervalo);
              fecha = nuevaFecha;

              // console.log("revisando fecha",  fecha)
              // console.log("revisando fechafin",  fechaFin)
            }
            // Agregar evento para la fecha de fin
            horasRepeticion.forEach(hora => {
                eventos.push({
                    title: tarea.nombre,
                    start: new Date(fechaFin.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    allDay: false
                });
                const evento = {
                    title: tarea.nombre,
                    start: new Date(fechaFin.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
              });
            break;

          case 'S':
            while (fecha <= fechaFin) {
              horasRepeticion.forEach(hora => {
                eventos.push({
                  title: tarea.nombre,
                  start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                  allDay: false
                });
                const evento = {
                    title: tarea.nombre,
                    start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
              });
              let nuevaFecha = new Date(fecha);
              nuevaFecha.setDate(nuevaFecha.getDate() + (intervalo * 7));
              fecha = nuevaFecha;
            }   

            // Agregar evento para la fecha de fin
            horasRepeticion.forEach(hora => {
                eventos.push({
                    title: tarea.nombre,
                    start: new Date(fechaFin.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    allDay: false
                });
                const evento = {
                    title: tarea.nombre,
                    start: new Date(fechaFin.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
            });

            break;
          case 'M':
            while (fecha <= fechaFin) {
              horasRepeticion.forEach(hora => {
                eventos.push({
                  title: tarea.nombre,
                  start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                  allDay: false
                });
                const evento = {
                    title: tarea.nombre,
                    start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
              });
              let nuevaFecha = new Date(fecha);
              nuevaFecha.setMonth(nuevaFecha.getMonth() + intervalo);
              fecha = nuevaFecha;
            }

            // Agregar evento para la fecha de fin
            horasRepeticion.forEach(hora => {
                eventos.push({
                    title: tarea.nombre,
                    start: new Date(fechaFin.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    allDay: false
                });
                const evento = {
                    title: tarea.nombre,
                    start: new Date(fechaFin.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
            });

            break;
        }
        return eventos;
        
      });
    },

    // metodos para la eliminacion y guardado de eventosCalendarios 
    // Método para eliminar todos los eventos antiguos del modelo eventosCalendarios
    eliminarEventosAntiguos() {
        return axios.get(this.api + '/api/eventosCalendarios/')
          .then(response => {
            const eventos = response.data;
            const deletePromises = eventos.map(evento => {
              return axios.delete(`${this.api}/api/eventosCalendarios/${evento.id}`);
            });
            // Ejecutar todas las solicitudes DELETE en paralelo
            return Promise.all(deletePromises);
          })
          // .then(() => {
          //   console.log('Todos los eventos antiguos han sido eliminados exitosamente.');
          // })
          .catch(error => {
            console.error('Error al eliminar eventos antiguos:', error);
            throw error; // Lanzar error para que pueda ser manejado en la promesa encadenada
          });
      },
      guardarEvento(evento) {
        axios.post(this.api + '/api/eventosCalendarios/', evento)
          // .then(response => {
          //   console.log('Evento guardado exitosamente:', response.data);
          // })
          .catch(error => {
            console.error('Error al guardar evento:', error);
          });
      },
  }
}
</script>

<style scoped>
.calendario-container {
  padding: 1rem; /* Usa rems para un espaciado responsivo */
  background-color: #f0f0f0; /* Cambia el color de fondo según tus preferencias */ 
}

.fc-header-toolbar-title {
  color: #000; /* Color del texto del título de la barra de herramientas */
  margin-bottom: 1rem; /* Agrega un espacio debajo del título */
}

@media (max-width: 768px) {
  .calendario-container {
    padding: 0.5rem; /* Espaciado más pequeño para pantallas más pequeñas */
  }
}
</style>


