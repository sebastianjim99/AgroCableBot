
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
      axios.get('http://localhost:8000/api/calendarios') // Endpoint para obtener las tareas
        .then(response => {
          const eventos = this.parsearEventos(response.data);
          this.calendarOptions.events = eventos; // Actualiza la lista de eventos del calendario
        })
        .catch(error => {
          console.error(error);
        });
    },
    parsearEventos(tareas) {
      return tareas.flatMap(tarea => {
        const eventos = [];
        const intervalo = tarea.intervalo || 1;
        const horasRepeticion = [tarea.hora_repeticion_1, tarea.hora_repeticion_2, tarea.hora_repeticion_3].filter(hora => hora !== "00:00:00");
        
        let fechaInicio = new Date(tarea.fecha_inicio);
        let fechaFin = new Date(tarea.fecha_fin);
        let fecha = new Date(fechaInicio);
        switch (tarea.repeticion) {
          case 'D':
            while (fecha <= fechaFin) {
              horasRepeticion.forEach(hora => {
                eventos.push({
                  title: tarea.nombre,
                  start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                  allDay: false
                });
              });
              fecha.setDate(fecha.getDate() + intervalo);
            }
            break;
          case 'S':
            while (fecha <= fechaFin) {
              horasRepeticion.forEach(hora => {
                eventos.push({
                  title: tarea.nombre,
                  start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                  allDay: false
                });
              });
              fecha.setDate(fecha.getDate() + (intervalo * 7));
            }
            break;
          case 'M':
            while (fecha <= fechaFin) {
              horasRepeticion.forEach(hora => {
                eventos.push({
                  title: tarea.nombre,
                  start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                  allDay: false
                });
              });
              fecha.setMonth(fecha.getMonth() + intervalo);
            }
            break;
        }
        return eventos;
      });
    }
  }
}
</script>
<style scoped>
.calendario-container {
  margin: 60px ; /* Ajusta el margen según tus preferencias */
  background-color: #f0f0f0; /* Cambia el color de fondo según tus preferencias */ 
  
}
.fc-header-toolbar-title {
  color: #000; /* Color del texto del título de la barra de herramientas */
  /* Personaliza el fondo y el color del texto de la barra de herramientas del encabezado */
}
</style>

<template>
  <div class="calendario-container fc-header-toolbar-title">
    <h1>Calendario de Tareas</h1>
    <FullCalendar :options='calendarOptions'>
      <template v-slot:eventContent='arg'>
        <b>{{ arg.timeText }}</b>
        <i>{{ arg.event.title }}</i>
      </template>
    </FullCalendar>
  </div>
</template>
