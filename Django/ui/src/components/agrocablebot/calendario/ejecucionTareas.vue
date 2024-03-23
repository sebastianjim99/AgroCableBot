<!-- 
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        events: [], // Las tareas se cargarán dinámicamente más adelante
        // eventCheckInterval: null, // Variable para almacenar el intervalo de comprobación de eventos
        // intervalDuration: 120000, // Duración del intervalo en milisegundos (2 minutos)
      };
    },
    mounted() {
      this.obtenerTareas(); // Llama a la función para obtener las tareas al montar el componente
      // this.eventCheckInterval = setInterval(this.ejecutarEventos, this.intervalDuration); // Iniciar intervalo de comprobación de eventos
      
    },

    // beforeUnmount() {
    //   clearInterval(this.eventCheckInterval); // Limpiar intervalo al destruir el componente para evitar fugas de memoria
    // },

    methods: {
       // Método para eliminar todos los eventos antiguos del modelo eventosCalendarios
       eliminarEventosAntiguos() {
        return axios.get('http://localhost:8000/api/eventosCalendarios/')
          .then(response => {
            const eventos = response.data;
            const deletePromises = eventos.map(evento => {
              return axios.delete(`http://localhost:8000/api/eventosCalendarios/${evento.id}`);
            });
            // Ejecutar todas las solicitudes DELETE en paralelo
            return Promise.all(deletePromises);
          })
          .then(() => {
            console.log('Todos los eventos antiguos han sido eliminados exitosamente.');
          })
          .catch(error => {
            console.error('Error al eliminar eventos antiguos:', error);
            throw error; // Lanzar error para que pueda ser manejado en la promesa encadenada
          });
      },
      guardarEvento(evento) {
        axios.post('http://localhost:8000/api/eventosCalendarios/', evento)
          // .then(response => {
          //   console.log('Evento guardado exitosamente:', response.data);
          // })
          .catch(error => {
            console.error('Error al guardar evento:', error);
          });
      },


      obtenerTareas() {
        this.eliminarEventosAntiguos() // Llama al método para eliminar eventos antiguos
          .then(() => {
            axios.get('http://localhost:8000/api/calendarios') // Endpoint para obtener las tareas
              .then(response => {
                const eventos = this.parsearEventos(response.data);
                this.events = eventos; // Almacena los eventos obtenidos
                // console.log("Eventos", eventos);
              })
              .catch(error => {
                console.error('Error al obtener tareas:', error);
              });
          })
          .catch(error => {
            console.error('Error al eliminar eventos antiguos:', error);
          });
      },

      // ParsearEventos -> lo que hace es tomar una Lista de tareas con una logica repeticion e intervalo y
      // lo lleva a un array de eventos donde se secciona todos los eventos que quieren ejecutar 
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
                  const evento = {
                    title: tarea.nombre,
                    start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
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
                  const evento = {
                    title: tarea.nombre,
                    start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
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
                  const evento = {
                    title: tarea.nombre,
                    start: new Date(fecha.setHours(hora.substring(0, 2), hora.substring(3, 5))),
                    calendario: tarea.id,
                    allDay: false
                  };
                  this.guardarEvento(evento);
                });
                fecha.setMonth(fecha.getMonth() + intervalo);
              }
              break;
          }
          return eventos;
        });
      },
      // ejecutarEventos() {
      //   const ahora = new Date();
      //   const margen = 1; // Margen de 2 minutos
      //   //console.log("Ahora",ahora)
      //   this.events.forEach(evento => {
      //     const eventoFecha = new Date(evento.start);
      //     const diferenciaTiempo = Math.abs(ahora - eventoFecha) / (1000 * 60); // Diferencia en minutos
      //     // console.log("Ahora",ahora)
      //     // console.log("Evento Fecha",eventoFecha)
      //     // console.log("Diferencia",diferenciaTiempo)

      //     if (diferenciaTiempo <= margen) {
      //       console.log('Ejecutando evento: --------', evento.title);
      //       // Llama a la acción asociada al evento
      //       // (aquí puedes agregar tu lógica específica)
      //     }
      //     //else{console.log("no entro al if")}
          
      //   });
      // },


    }
  };
</script>
  
  <style scoped>
  /* Estilos CSS específicos para este componente */
  </style>
   -->