<template>
  <div style="padding-top: 56px;">
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <h2 style="width: 343px;">Lista de cultivo</h2>
        </div>
        <div class="col-md-4 d-flex justify-content-end align-self-start">
          <button class="btn btn-primary d-flex align-items-center align-self-center" type="button" style="height: 38px;text-align: center;background: rgb(4,221,156);" @click="showForm = true">
            Agregar <i class="fa fa-plus-circle"></i>
          </button>
        </div>
        <div class="col-md-4 d-flex justify-content-center align-items-center">
          <i class="fas fa-search d-xl-flex justify-content-xl-center align-items-xl-center"></i>
          <input id="search-field" class="border rounded d-xl-flex justify-content-xl-center align-items-xl-center search-field" type="search" style="background-color: #eaeaea;width: 80%;height: 38px;padding: 0px;margin-left: 17px;" name="search" />
        </div>
      </div>
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
              <tr v-for="cultivo in cultivos" :key="cultivo.id">
                <td>{{ cultivo.nombre }}</td>
                <td>{{ cultivo.fechaSiembra }}</td>
                <td>{{ cultivo.responsable }}</td>
                <td>{{ cultivo.cantidad }}</td>
                <td>Dec 1, 2022</td>
                <td>A tiempo</td>
                <td>
                  <button class="btn btn-warning" type="button" @click="editarCultivo(cultivo)">
                    <i class="fas fa-pencil-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
                  </button>
                  <button class="btn btn-danger" type="button" @click="eliminarCultivo(cultivo.id)">
                    <i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div v-if="showForm">
      <form @submit.prevent="submitForm">
        <input type="text" v-model="nombre" placeholder="Nombre del cultivo" required>
        <input type="number" v-model="cantidad" placeholder="Cantidad de plantas" required>
        <input type="file" @change="onFileChange" accept="image/*" required>
        <input type="text" v-model="responsable" placeholder="Responsable" required>
        <input type="email" v-model="correo" placeholder="Correo Electrónico" required>
        <input type="date" v-model="fechaSiembra" placeholder="Fecha de siembra" required>
        <select v-model="selectedTipo" required>
          <option v-for="tipo in listaDeTipos" :key="tipo.id" :value="tipo">{{ tipo.nombre }}</option>
        </select>
        <div v-for="sensor in listaDeSensores" :key="sensor.id">
          <input type="checkbox" v-model="selectedSensores" :value="sensor.id" placeholder="Sensores">{{ sensor.nombre }}
        </div>
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
      showForm: false,
      nombre: '',
      cantidad: null,
      iconosPlantas: null,
      responsable: '',
      correo: '',
      fechaSiembra: '',
      selectedTipo: null, // Almacena el tipo de cultivo seleccionado
      selectedSensores: [], // Almacena los sensores seleccionados
      cultivos: [],
      listaDeTipos: [], // Nueva lista para tipos de cultivo
      listaDeSensores: [], // Nueva lista para sensores
      editingCultivoId: null
    };
  },
  mounted() {
    this.getCultivos();
    this.getTiposDeCultivo();
    this.getSensores();
  },
  methods: {
    getCultivos() {
      axios.get('http://localhost:8000/api/cultivo')
        .then(response => {
          this.cultivos = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getTiposDeCultivo() {
      axios.get('http://localhost:8000/api/tipoCultivo')
        .then(response => {
          console.log('tipos de cultivo get',response.data)
          this.listaDeTipos = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getSensores() {
      axios.get('http://localhost:8000/api/sensor')
        .then(response => {
          this.listaDeSensores = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    onFileChange(e) {
      this.tipoCultivo= e.target.files[0];
      this.iconosPlantas = e.target.files[0];
    },
    submitForm() {
      let formData = new FormData();
      formData.append('nombre', this.nombre);
      formData.append('cantidad', this.cantidad);
      formData.append('responsable', this.responsable);
      formData.append('correo', this.correo);
      formData.append('fechaSiembra', this.fechaSiembra);
      formData.append('tipoCultivo', this.selectedTipo); // Utiliza selectedTipo
      formData.append('sensores', this.selectedSensores); // Utiliza selectedSensores

     

      if (this.iconosPlantas) {
        formData.append('iconosPlantas', this.iconosPlantas);
      }

      let requestMethod = this.editingCultivoId ? 'patch' : 'post';
      let requestUrl = this.editingCultivoId ? `http://localhost:8000/api/cultivo/${this.editingCultivoId}/` : 'http://localhost:8000/api/cultivo/';

      console.log('Datos a enviar:', {
        nombre: this.nombre,
        cantidad: this.cantidad,
        responsable: this.responsable,
        correo: this.correo,
        fechaSiembra: this.fechaSiembra,
        tipoCultivo: this.selectedTipo,
        sensor: this.selectedSensores,
        // Otros campos que desees imprimir
      });

      axios[requestMethod](requestUrl, formData)
        .then(() => {
          Swal.fire({
            icon: 'success',
            title: '¡Éxito!',
            text: this.editingCultivoId ? 'Cultivo actualizado correctamente' : 'Cultivo creado correctamente'
          }).then(() => {
            this.showForm = false;
            this.editingCultivoId = null;
            this.getCultivos();
          });
        })
        .catch(error => {
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: this.editingCultivoId ? 'Ocurrió un error al actualizar el cultivo' : 'Ocurrió un error al crear el cultivo',
          });
        });
    },
    editarCultivo(cultivo) {
      this.nombre = cultivo.nombre;
      this.cantidad = cultivo.cantidad;
      this.responsable = cultivo.responsable;
      this.correo = cultivo.correo;
      this.fechaSiembra = cultivo.fechaSiembra;

      // Asegúrate de que cultivo.sensor sea una lista (si es un ManyToManyField)
      if (Array.isArray(cultivo.sensor)) {
        this.selectedSensores = cultivo.sensor;
      } else {
        this.selectedSensores = [];
      }

      this.editingCultivoId = cultivo.id;
      this.showForm = true;
    },
    cancelarFormulario() {
      this.showForm = false;
    },
    eliminarCultivo(cultivoId) {
      Swal.fire({
        icon: 'warning',
        title: '¿Estás seguro?',
        text: 'Una vez eliminado, ¡no podrás recuperar este cultivo!',
        showCancelButton: true,
        confirmButtonText: 'Sí, eliminarlo',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          axios.delete(`http://localhost:8000/api/cultivo/${cultivoId}/`)
            .then(() => {
              Swal.fire(
                '¡Eliminado!',
                'El cultivo ha sido eliminado.',
                'success'
              ).then(() => {
                this.getCultivos();
              });
            })
            .catch(error => {
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
