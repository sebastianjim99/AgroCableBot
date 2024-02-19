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
        let fechaInicio = new Date(tarea.fecha_inicio);
        let fechaFin = new Date(tarea.fecha_fin);
        let fecha = new Date(fechaInicio);
        switch (tarea.repeticion) {
          case 'D':
            while (fecha <= fechaFin) {
              eventos.push({
                title: tarea.nombre,
                start: new Date(fecha),
                end: new Date(fecha),
                allDay: false
              });
              fecha.setDate(fecha.getDate() + intervalo);
            }
            break;
          case 'S':
            while (fecha <= fechaFin) {
              eventos.push({
                title: tarea.nombre,
                start: new Date(fecha),
                end: new Date(fecha),
                allDay: false
              });
              fecha.setDate(fecha.getDate() + (intervalo * 7));
            }
            break;
          case 'M':
            while (fecha <= fechaFin) {
              eventos.push({
                title: tarea.nombre,
                start: new Date(fecha),
                end: new Date(fecha),
                allDay: false
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
  margin: px; /* Ajusta el margen según tus preferencias */
}
</style>

<template>
  <div class="calendario-container">
    <h1>Calendario de Tareas</h1>
    <FullCalendar :options='calendarOptions'>
      <template v-slot:eventContent='arg'>
        <b>{{ arg.timeText }}</b>
        <i>{{ arg.event.title }}</i>
      </template>
    </FullCalendar>
  </div>
</template>
