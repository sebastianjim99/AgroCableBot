<template>
  <!-- Estructura de la interfaz de usuario -->
  <div style="padding-top: 56px;">
    <div class="container">
      <!-- Encabezado de la interfaz -->
      <div class="row">
        <div class="col-md-4">
          <!-- Título de la lista de cultivos -->
          <h2 style="width: 343px;">Lista de cultivo</h2>
        </div>
        <div class="col-md-4 d-flex justify-content-end align-self-start">
          <!-- Botón para agregar un nuevo cultivo -->
          <button class="btn btn-primary d-flex align-items-center align-self-center" type="button" style="height: 38px;text-align: center;background: rgb(4,221,156);" @click="showForm = true">
            Agregar <i class="fa fa-plus-circle"></i>
          </button>
        </div>
        <div class="col-md-4 d-flex justify-content-center align-items-center">
          <!-- Campo de búsqueda -->
          <i class="fas fa-search d-xl-flex justify-content-xl-center align-items-xl-center"></i>
          <input id="search-field" class="border rounded d-xl-flex justify-content-xl-center align-items-xl-center search-field" type="search" style="background-color: #eaeaea;width: 80%;height: 38px;padding: 0px;margin-left: 17px;" name="search" />
        </div>
      </div>
      <!-- Tabla para mostrar los cultivos -->
      <div class="row">
        <div class="col-md-12">
          <table id="example" class="table table-striped table-bordered" cellspacing="0" width="100%">
            <thead>
              <tr>
                <th>Cultivo</th>
                <th>Fecha de siembra</th>
                <th>Responsable</th>
                <th>Cantidad</th>
                <th>Estimado de cosecha</th>
                <th>Estado</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <!-- Iteración sobre la lista de cultivos -->
              <tr v-for="cultivo in cultivos" :key="cultivo.id">
                <!-- Datos de cada cultivo -->
                <td>{{ cultivo.nombre }}</td>
                <td>{{ cultivo.fechaSiembra }}</td>
                <td>{{ cultivo.responsable }}</td>
                <td>{{ cultivo.cantidad }}</td>
                <td>Dec 1, 2022</td>
                <td>A tiempo</td>
                <td>
                  <!-- Botones para editar y eliminar cada cultivo -->
                  <button class="btn btn-warning" type="button" @click="editarCultivo(cultivo)">
                    <i class="fas fa-pencil-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                      <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                      <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                    </svg>
                  </button>

                  <button class="btn btn-danger" style="width: 30px ;height: 30px;" type="button" @click="eliminarCultivo(cultivo.id)">
                    <i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
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
    <!-- Formulario para agregar o editar un cultivo -->
    <div v-if="showForm">
      <form @submit.prevent="submitForm">
        <!-- Campos del formulario -->
        <input type="text" v-model="nombre" placeholder="Nombre del cultivo" required>
        <input type="number" v-model="cantidad" placeholder="Cantidad de plantas" required>
        <input type="file" @change="onFileChange" accept="image/*" required>
        <input type="text" v-model="responsable" placeholder="Responsable" required>
        <input type="email" v-model="correo" placeholder="Correo Electrónico" required>
        <input type="date" v-model="fechaSiembra" placeholder="Fecha de siembra" required>
        <select v-model="selectedTipo" required>
          <!-- Opciones para seleccionar el tipo de cultivo -->
          <option v-for="tipo in listaDeTipos" :key="tipo.id" :value="tipo.id">{{ tipo.nombre }}</option>
        </select>
        <!-- Selección de sensores -->
        <div v-for="sensor in listaDeSensores" :key="sensor.id">
          <input type="checkbox" v-model="selectedSensores" :value="sensor.id" placeholder="Sensores" >{{ sensor.nombre }}
        </div>
        <!-- Botones para cancelar o enviar el formulario -->
        <button @click="cancelarFormulario" class="btn btn-danger">Cancelar</button>
        <button type="submit" class="btn btn-success">{{ editingCultivoId ? 'Actualizar' : 'Guardar' }}</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      // Datos del componente
      showForm: false,        // muestra formularios
      nombre: '',
      cantidad: null,
      iconosPlantas: null,
      responsable: '',
      correo: '',
      fechaSiembra: '',
      selectedTipo: null,     // Almacena el tipo de cultivo seleccionado
      selectedSensores: [],   // Almacena los sensores seleccionados
      cultivos: [],
      listaDeTipos: [],       // Nueva lista para tipos de cultivo
      listaDeSensores: [],    // Nueva lista para sensores
      editingCultivoId: null  // Lleva la relacion para el cultivo a editar
    };
  },
  mounted() {
    // Llamadas a funciones al cargar el componente
    this.getCultivos();
    this.getTiposDeCultivo();
    this.getSensores();
  },
  methods: {
    // Métodos para interactuar con la API --------------- CRUD -------------------
    getCultivos() {
      // Realiza una solicitud GET al servidor para obtener la lista de cultivos
      axios.get('http://localhost:8000/api/cultivo')
        .then(response => {
          // Almacena la lista de cultivos obtenida del servidor en la variable 'cultivos'
          this.cultivos = response.data;
        })
        .catch(error => {
          // Maneja los errores de la solicitud GET y los muestra en la consola
          console.log(error);
        });
    },
    getTiposDeCultivo() {
      // Realiza una solicitud GET al servidor para obtener la lista de tipos de cultivo
      axios.get('http://localhost:8000/api/tipoCultivo')
        .then(response => {
          //console.log('tipos de cultivo get',response.data)
          this.listaDeTipos = response.data; // Almacena la lista de tipos de cultivo obtenida del servidor en la variable 'listaDeTipos'
        })
        .catch(error => {
          console.log(error);
        });
    },
    getSensores() {
      // Realiza una solicitud GET al servidor para obtener la lista de sensores
      axios.get('http://localhost:8000/api/sensor')
        .then(response => {
          this.listaDeSensores = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    onFileChange(e) {
      this.iconosPlantas = e.target.files[0];
    },
    
   
    submitForm() {
      // Lógica para enviar el formulario
      let formData = new FormData();   // Crea un objeto FormData para empaquetar los datos del formulario
      // Agrega los campos del formulario al objeto FormData
      formData.append('nombre', this.nombre);
      formData.append('cantidad', this.cantidad);
      formData.append('responsable', this.responsable);
      formData.append('correo', this.correo);
      formData.append('fechaSiembra', this.fechaSiembra);
      formData.append('tipoCultivo', this.selectedTipo); 
      

      // Verifica si se han seleccionado sensores y los agrega al FormData
      if (this.selectedSensores.length > 0) {
        // Convierte los IDs de los sensores seleccionados a una lista de strings
        const selectedSensoresIds = this.selectedSensores.map(sensor => sensor.toString());

        // Agrega los IDs de los sensores seleccionados al formData
        for (const sensorId of selectedSensoresIds) {
          formData.append('sensores', sensorId);
        }
      } else {
        // Si no se seleccionó ningún sensor, establece el campo sensores en null
        formData.append('sensores', null);
      }

     
      // Agrega el archivo de iconosPlantas al FormData si está presente
      if (this.iconosPlantas) {
        formData.append('iconosPlantas', this.iconosPlantas);
      }

      // Determina si la solicitud es para actualizar o crear un nuevo cultivo
      let requestMethod = this.editingCultivoId ? 'patch' : 'post';
      // Construye la URL de la solicitud en función de si se está editando o creando un cultivo
      let requestUrl = this.editingCultivoId ? `http://localhost:8000/api/cultivo/${this.editingCultivoId}/` : 'http://localhost:8000/api/cultivo/';

      // Muestra por consola los datos que se enviarán al servidor
      /*console.log('Datos a enviar:', {
        nombre: this.nombre,
        cantidad: this.cantidad,
        responsable: this.responsable,
        correo: this.correo,
        fechaSiembra: this.fechaSiembra,
        tipoCultivo: this.selectedTipo, 
        sensor: this.selectedSensores,
        
      });*/

      // Realiza la solicitud HTTP al servidor utilizando axios
      axios[requestMethod](requestUrl, formData)
        .then(() => {
          // Muestra una alerta de éxito al usuario utilizando SweetAlert2
          Swal.fire({
            // Manejo de éxito
            icon: 'success',
            title: '¡Éxito!',
            text: this.editingCultivoId ? 'Cultivo actualizado correctamente' : 'Cultivo creado correctamente'
          }).then(() => {
            // Oculta el formulario después de enviar los datos exitosamente
            this.showForm = false;
            this.editingCultivoId = null;
            this.getCultivos();
          });
        })
        .catch(error => {
           // Maneja los errores de la solicitud HTTP y muestra una alerta de error al usuario
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: this.editingCultivoId ? 'Ocurrió un error al actualizar el cultivo' : 'Ocurrió un error al crear el cultivo',
          });
        });
    },
    editarCultivo(cultivo) {
      // Lógica para editar un cultivo
      this.nombre = cultivo.nombre;
      this.cantidad = cultivo.cantidad;
      this.responsable = cultivo.responsable;
      this.correo = cultivo.correo;
      this.fechaSiembra = cultivo.fechaSiembra;
      this.selectedTipo = cultivo.tipoCultivo; 
      // Asegúrate de que cultivo.sensor sea una lista (si es un ManyToManyField)
      if (Array.isArray(cultivo.sensor)) {
        this.selectedSensores = cultivo.sensor.map(sensor => sensor.toString());
      } else {
        this.selectedSensores = [];
      }

      this.editingCultivoId = cultivo.id;
      this.showForm = true;
    },
    cancelarFormulario() {
      // Lógica para cancelar el formulario
      this.showForm = false;
    },
    eliminarCultivo(cultivoId) {
      // Lógica para eliminar un cultivo
      // Muestra una confirmación al usuario antes de eliminar el cultivo
      Swal.fire({
        icon: 'warning',
        title: '¿Estás seguro?',
        text: 'Una vez eliminado, ¡no podrás recuperar este cultivo!',
        showCancelButton: true,
        confirmButtonText: 'Sí, eliminarlo',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        // Si el usuario confirma la eliminación
        if (result.isConfirmed) {
          // Realiza una solicitud DELETE al servidor para eliminar el cultivo
          axios.delete(`http://localhost:8000/api/cultivo/${cultivoId}/`)
            .then(() => {
              // Muestra una alerta de éxito al usuario
              Swal.fire(
                '¡Eliminado!',
                'El cultivo ha sido eliminado.',
                'success'
              ).then(() => {
                // Actualiza la lista de cultivos mostrada en la interfaz de usuario después de eliminar el cultivo
                this.getCultivos();
              });
            })
            .catch(error => {
              // Maneja los errores de la solicitud DELETE y muestra una alerta de error al usuario
              console.error(error);
              Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al eliminar el cultivo',
              });
            });
        }
      });
    }
  }
};
</script>
