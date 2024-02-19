<template>
  <!-- Estructura del componente en HTML -->
  <div>
    <div class="container">
      <div class="row">
         <!-- Encabezado de la página -->
        <div class="col-md-8" style="text-align: center;">
          <h2 class="divider-style">
            <span>Tareas programadas</span>
          </h2>
        </div>
        <!-- Botón para abrir el modal de agregar tarea -->
        <div class="col-md-4 d-flex justify-content-center align-items-center">
          <button class="btn btn-primary d-flex align-items-center align-self-center" type="button" style="height: 38px; background-color: rgb(21,221,4);" @click="abrirModal">Agregar Tarea
            <!-- Icono de "más" -->
            <svg class="bi bi-plus-circle-fill" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 29px;">
              <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"></path>
            </svg>
          </button>
        </div>
      </div>
      <!-- Tabla para mostrar las tareas programadas -->
      <div class="row">
        <div class="col-md-12">
          <table id="example" class="table table-striped table-bordered" cellspacing="0" width="100%">
            <thead>
              <!-- Cabeceras de la tabla -->
              <tr>
                <th>Id</th>
                <th>Nombre</th>
                <th>Recurrencia</th>
                <th>Hora</th>
                <th>Fecha</th>
                <th>Eliminar</th>
              </tr>
            </thead>
            <tbody>
              <!-- Filas de la tabla generadas dinámicamente con v-for -->
              <tr v-for="(calendario, index) in calendarios" :key="index">
                <td>{{ calendario.id }}</td>
                <td>{{ calendario.nombre }}</td>
                <td>{{ calendario.repeticion }}</td>
                <td>{{ calendario.hora_repeticion_1 }}</td>
                <td>{{ calendario.fecha_inicio }}</td>
                <td>
                  <!-- Botones para editar y eliminar tareas -->
                  <button class="btn btn-warning" type="button" @click="editarCalendario(calendario)">
                    <i class="fas fa-pencil-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
                    <!-- Icono de lápiz -->
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                      <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                      <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                    </svg>
                  </button>
                  <button class="btn btn-danger" type="button" @click="eliminarCalendario(calendario.id)">
                    <i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
                    <!-- Icono de papelera -->
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                      <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                      <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                    </svg>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Ventana emergente para agregar tarea -->
    <div v-if="mostrarModal" class="modal">
      <!-- Contenedor del modal -->
      <div class="modal-dialog">
        <!-- Contenido del modal -->
        <div class="modal-content">
          <!-- Botón para cerrar la ventana emergente -->
          <span class="cerrar" @click="cerrarModal">&times;</span>
          <!-- Título de la ventana emergente -->
          <h2>Agregar Tarea</h2>
          <!-- Formulario para agregar una nueva tarea -->
          <form @submit.prevent="agregarTarea">
            <!-- Campos del formulario -->
            <label for="nombre">Nombre:</label><br><input type="text" v-model="nombre" required><br>
            <label for="acciones">Acciones:</label><br>
            <!-- Campo para seleccionar accion relacionada con la tarea -->
            <select v-model="selectedAcciones" multiple>
              <option v-for="accion in acciones" :key="accion.id" :value="accion.id">{{ accion.nombre }}</option>
            </select><br>
            <label for="fecha_inicio">Fecha de inicio:</label><br><input type="date" v-model="fecha_inicio" required><br>
            <label for="fecha_fin">Fecha de fin:</label><br><input type="date" v-model="fecha_fin" required><br>
            <label for="repeticion">Repeticion:</label>
            <!-- Campo para seleccionar repeticion relacionada con la tarea -->
            <select v-model="repeticion" required>
              <option value="D">Diaria</option>
              <option value="S">Semanal</option>
              <option value="M">Mensual</option>
            </select><br>
            <label for="intervalo">Intervalo:</label><input type="number" v-model="intervalo" required><br>
            <label for="todoCultivo">Todo Cultivo:</label>
            <select v-model="todoCultivo" required>
              <option value="S">Sí</option>
              <option value="N">No</option>
            </select><br>
            <label for="hora_repeticion_1">Hora de repetición 1:</label><br><input type="time" v-model="hora_repeticion_1" required><br>
            <label for="hora_repeticion_2">Hora de repetición 2:</label><br><input type="time" v-model="hora_repeticion_2"><br>
            <label for="hora_repeticion_3">Hora de repetición 3:</label><br><input type="time" v-model="hora_repeticion_3"><br>
            <label for="cultivos">Cultivos:</label><br>
            <!-- Campo para seleccionar el cultivo relacionado con la tarea -->
            <select multiple v-model="selectedCultivos"  required @change="seleccionarPlantasPorCultivo">
              <option v-for="cultivo in cultivos" :key="cultivo.id" :value="cultivo.id">{{ cultivo.nombre }}</option>
            </select><br>
            <label for="plantas">Plantas:</label><br>
            <!-- Campo para seleccionar las plantas relacionadas con la tarea -->
            <select multiple v-model="selectedPlantas" required>
              <option v-for="planta in plantas" :key="planta.id" :value="planta.id" >{{ planta.nombre }}</option>
            </select><br>
            <!-- Botón para guardar la tarea -->
            <button type="submit" >Guardar </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Importación de librerías y configuraciones necesarias
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  // Datos del componente
  data() {
    return {
      // Variables para controlar el modal y los campos del formulario
      mostrarModal: false,
      nombre: "",
      selectedAcciones: [],
      fecha_inicio: null,
      fecha_fin: null,
      repeticion: "",
      intervalo: null,
      todoCultivo: "",
      hora_repeticion_1: null,
      hora_repeticion_2: null,
      hora_repeticion_3: null,
      cultivos: [],
      selectedPlantas: [],
      calendarios: [],
      acciones: [],
      selectedCultivos: [],
      editingCalendarioId: null,
    };
  },
  // Método ejecutado al cargar el componente
  mounted() {
    this.obtenerCalendarios();
    this.obtenerAcciones();
    this.obtenerCultivos();
    this.obtenerPlantas();
  },

  // Watcher para todoCultivo
  watch: {
    todoCultivo(newValue) {
      if (newValue === "S") {
        // Seleccionar todos los cultivos
        this.selectedCultivos = this.cultivos.map(cultivo => cultivo.id);
        // Seleccionar todas las plantas
        this.selectedPlantas = this.plantas.map(planta => planta.id);
      } else {
        // Si se selecciona "No", restablecer los selects
        this.selectedCultivos = [];
        this.selectedPlantas = [];
      }
    }
  },
  // Métodos del componente
  methods: {
    // Método para abrir el modal de agregar tarea
    abrirModal() {
      this.resetForm();           // Reiniciar valores del formulario
      this.mostrarModal = true;   // Mostrar el modal
    },
    // Método para cerrar el modal de agregar tarea
    cerrarModal() {
      this.mostrarModal = false;  // Ocultar el modal
    },
    // Método para obtener las tareas programadas desde el servidor
    obtenerCalendarios() {
      axios.get('http://localhost:8000/api/calendarios')
        .then(response => {
          this.calendarios = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Método para obtener las acciones desde el servidor
    obtenerAcciones() {
      axios.get('http://localhost:8000/api/acciones')
        .then(response => {
          this.acciones = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Método para obtener los cultivos desde el servidor
    obtenerCultivos() {
      axios.get('http://localhost:8000/api/cultivo')
        .then(response => {
          this.cultivos = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Método para obtener las plantas desde el servidor
    obtenerPlantas() {
      axios.get('http://localhost:8000/api/plantas')
        .then(response => {
          this.plantas = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Método para agregar una nueva tarea
    agregarTarea() {
      
      // Validar y asignar valores predeterminados para los campos de hora
      if (!this.hora_repeticion_1) {
        this.hora_repeticion_1 = "00:00:00";
      }
      if (!this.hora_repeticion_2) {
        this.hora_repeticion_2 = "00:00:00";
      }
      if (!this.hora_repeticion_3) {
        this.hora_repeticion_3 = "00:00:00";
      }
  
      // Crear objeto FormData para enviar datos del formulario
      let formData = new FormData();
      formData.append('nombre', this.nombre);
      formData.append('acciones', this.selectedAcciones);
      formData.append('fecha_inicio', this.fecha_inicio);
      formData.append('fecha_fin', this.fecha_fin);
      formData.append('repeticion', this.repeticion);
      formData.append('intervalo', this.intervalo);
      formData.append('todoCultivo', this.todoCultivo);
      formData.append('hora_repeticion_1', this.hora_repeticion_1);
      formData.append('hora_repeticion_2', this.hora_repeticion_2);
      formData.append('hora_repeticion_3', this.hora_repeticion_3);

      const selectedCultivoIds = this.selectedCultivos.map(cultivo => cultivo.toString());  // Convierte los IDs seleccionados a una lista de strings
      for (const cultivoId of selectedCultivoIds) {
        formData.append('cultivo', cultivoId);    // Agrega los IDs seleccionados al formData
      }
      
      const selectedPlantasIds = this.selectedPlantas.map(plantas => plantas.toString());   // Convierte los IDs seleccionados a una lista de strings 
      for (const plantaId of selectedPlantasIds) {
        formData.append('plantas', plantaId);     // Agrega los IDs seleccionados al formData
      }

      
      //Ver en consola los datos enviados
      /*
      console.log('Datos a enviar:', {
        nombre: this.nombre,
        acciones: this.selectedAcciones,
        fecha_inicio: this.fecha_inicio,
        fecha_fin: this.fecha_fin,
        repeticion: this.repeticion,
        intervalo: this.intervalo, 
        todoCultivo: this.todoCultivo,
        hora_repeticion_1:this.hora_repeticion_1,
        hora_repeticion_2: this.hora_repeticion_2,
        hora_repeticion_3: this.hora_repeticion_3,
        cultivos:this.selectedCultivos,
        plantas:this.selectedPlantas,
        editar: this.editingCalendarioId,
        // Otros campos que desees imprimir
      });*/
      
      // Determina si la solicitud es para actualizar o crear una nueva tarea
      let requestMethod = this.editingCalendarioId ? 'patch' : 'post';
      // Construye la URL de la solicitud en función de si se está editando o creando una tarea
      let requestUrl = this.editingCalendarioId ? `http://localhost:8000/api/calendarios/${this.editingCalendarioId}/` : 'http://localhost:8000/api/calendarios/';

      // Realiza la solicitud HTTP (POST o PATCH) al servidor (determinado la url anteriormente) utilizando axios 
      axios[requestMethod](requestUrl, formData)
        .then(() => {
          // Si la solicitud es exitosa, oculta el modal, muestra un mensaje de éxito y actualiza la lista de tareas
          this.mostrarModal = false;
          
          Swal.fire({
            icon: 'success',
            title: '¡Éxito!',
            text: this.editingCalendarioId ? 'Tarea actualizada correctamente' : 'Tarea creada correctamente',
          });
          this.editingCalendarioId = null;  // Restablece el ID de edición
          this.obtenerCalendarios();        // Actualiza la lista de tareas
          this.resetForm();                 // Restablece el formulario
        })
        .catch(error => {
          // Si hay un error en la solicitud, muestra un mensaje de error y oculta el modal
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ocurrió un error al crear la tarea',
          }).then(() => {
            this.mostrarModal = false;
          });
        });
    },

    seleccionarPlantasPorCultivo() {
      // Verificar si hay algún cultivo seleccionado
      if (this.selectedCultivos.length === 0) {
        // Si no se seleccionó ningún cultivo, establecer selectedPlantas como un array vacío
        this.selectedPlantas = [];
      } else {
        // Obtener el primer cultivo seleccionado
        const nuevoCultivo = this.selectedCultivos[0];
        if (nuevoCultivo) {
          // Obtener el ID del nuevo cultivo seleccionado
          const nuevoCultivoId = nuevoCultivo;
          console.log("GET" , nuevoCultivoId)

          // Limpiar la lista de plantas seleccionadas
          this.selectedPlantas = [];

          // Filtrar las plantas por el ID del cultivo seleccionado
          this.plantas.forEach(planta => {
            if (planta.cultivo.id === nuevoCultivoId) {
              this.selectedPlantas.push(planta.id);
            }
          });
          console.log(this.selectedPlantas)
        }
      }
    },

   

    editarCalendario(calendarios) {
      this.nombre = calendarios.nombre;
      this.selectedAcciones = Array.isArray(calendarios.acciones) ? calendarios.acciones.map(accion => accion.id) : []; //comprueba si es un array para poder iterar
      this.fecha_inicio = calendarios.fecha_inicio;
      this.fecha_fin = calendarios.fecha_fin;
      this.repeticion = calendarios.repeticion;
      this.intervalo = calendarios.intervalo;
      this.todoCultivo = calendarios.todoCultivo;
      this.hora_repeticion_1 = calendarios.hora_repeticion_1;
      this.hora_repeticion_2 = calendarios.hora_repeticion_2;
      this.hora_repeticion_3 = calendarios.hora_repeticion_3;
      this.selectedCultivos = Array.isArray(calendarios.cultivo) ? calendarios.cultivo.map(cultivo => cultivo.id) : []; //comprueba si es un array para poder iterar
      this.selectedPlantas = Array.isArray(calendarios.plantas) ? calendarios.plantas.map(plantas => plantas.id) : [];  //comprueba si es un array para poder iterar
      this.editingCalendarioId=calendarios.id;  

      this.mostrarModal = true;
    },
    // Método para limpiar el formulario
    resetForm() {
      // Reiniciar valores de los campos del formulario
      this.nombre = "";
      this.selectedAcciones = [];
      this.fecha_inicio = null;
      this.fecha_fin = null;
      this.repeticion = "";
      this.intervalo = null;
      this.todoCultivo = "";
      this.hora_repeticion_1 = null;
      this.hora_repeticion_2 = null;
      this.hora_repeticion_3 = null;
      this.selectedCultivos = [];
      this.selectedPlantas = [];
    },

    // Método para eliminar una tarea
    eliminarCalendario(calendarioId) {
      // Muestra una confirmación al usuario antes de eliminar
      Swal.fire({
        icon: 'warning',
        title: '¿Estás seguro?',
        text: 'Una vez eliminado, ¡no podrás recuperar esta tarea!',
        showCancelButton: true,
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        // Si el usuario confirma la eliminación
        if (result.isConfirmed) {
          // Realiza una solicitud DELETE al servidor para eliminar la tarea
          axios.delete(`http://localhost:8000/api/calendarios/${calendarioId}`)
            .then(() => {
              // Muestra una alerta de éxito al usuario
              Swal.fire(
                '¡Eliminado!',
                'La tarea ha sido eliminada.',
                'success'
              ).then(() => {
                // Actualiza la lista de cultivos mostrada en la interfaz de usuario después de eliminar
                this.obtenerCalendarios();
              });
            })
            .catch(error => {
              // Maneja los errores de la solicitud DELETE y muestra una alerta de error al usuario
              console.error(error);
              Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al eliminar la tarea',
              });
            });
        }
      });
    }
  }
};
</script>

<style scoped>
/* Estilos CSS para el componente modal */
.modal {
  /* Contenedor principal del modal */
  display: block; /* Mostrar como bloque */
  position: fixed; /* Fijar la posición en relación con la ventana del navegador */
  z-index: 9999; /* Colocar sobre otros elementos */
  left: 0; /* Posición izquierda */
  top: 0; /* Posición superior */
  width: 100%; /* Ancho completo */
  height: 100%; /* Altura completa */
  overflow: auto; /* Agregar desplazamiento automático si es necesario */
  background-color: rgba(0, 0, 0, 0.4); /* Fondo oscuro semi-transparente */
}

/* Estilos para el contenedor del diálogo modal dentro del modal */
.modal-dialog {
  position: relative; /* Posición relativa para posicionar elementos secundarios */
  margin: auto; /* Centrar horizontalmente dentro del modal */
  padding: 20px; /* Espaciado interno */
  background-color: #fefefe; /* Color de fondo */
  border: 1px solid #888; /* Borde sólido */
  width: 90%; /* Ancho del 90% del contenedor padre */
  max-width: 800px; /* Ancho máximo */
}

/* Estilos para el contenido del diálogo modal dentro del modal */
.modal-content {
  margin: auto; /* Centrar horizontalmente */
}

/* Estilos para el botón de cierre en la esquina superior derecha del modal */
.cerrar {
  color: #aaa; /* Color del icono de cierre */
  float: right; /* Alinear a la derecha */
  font-size: 28px; /* Tamaño de la fuente */
  font-weight: bold; /* Peso de la fuente */
}

/* Estilos para el botón de cierre cuando se pasa el mouse o se enfoca */
.cerrar:hover, .cerrar:focus {
  color: black; /* Cambiar color del texto a negro */
  text-decoration: none; /* Eliminar subrayado */
  cursor: pointer; /* Cambiar cursor */
}
</style>