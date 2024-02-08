<template>

    <div style="padding-top: 56px;">
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <h2 style="width: 343px;">Lista de cultivo</h2>
            </div>
            <div class="col-md-4 d-flex justify-content-end align-self-start"><button class="btn btn-primary d-flex align-items-center align-self-center" type="button" style="height: 38px;text-align: center;background: rgb(4,221,156);">Agregar <i class="fa fa-plus-circle"></i></button></div>
            <div class="col-md-4 d-flex justify-content-center align-items-center"><i class="fas fa-search d-xl-flex justify-content-xl-center align-items-xl-center"></i><input id="search-field" class="border rounded d-xl-flex justify-content-xl-center align-items-xl-center search-field" type="search" style="background-color: #eaeaea;width: 80%;height: 38px;padding: 0px;margin-left: 17px;" name="search" /></div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <table id="example" class="table table-striped table-bordered" cellspacing="0" width="100%">
                    <thead>
                        <tr>
                            <!-- <th>Id</th> -->
                            <th>Cultivo</th>
                            <th>Fecha de siembra</th>
                            <th>Responsable</th>
                            <th>Cantidad</th>
                            <th>Estimado de cosecha</th>
                            <th>Estado</th>
                            <th>Editar</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for ="cultivos in cultivos" :key="cultivos.id" >
                            <!-- <td>{{ cultivos.id }}</td> -->
                            <td>{{ cultivos.nombre }}</td>
                            <td>{{ cultivos.fechaSiembra }}</td>
                            <td>{{ cultivos.responable }}</td>
                            <td>{{ cultivos.cantidad}}</td>
                            <td>Dec 1, 2022</td>
                            <td>A tiempo</td>
                            <td><button class="btn btn-danger" type="button"><i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i></button><button class="btn btn-warning" type="button"><i class="fas fa-pencil-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i></button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
    
</template>


<script>
      import axios from 'axios'
  export default {
    data(){
      return{
        tipo_cultivo:[],
        cultivos:[],
        plantas:[],
        matriz: [],
        plantaSeleccionada: null,
        cultivoSeleccionado:null
        
      }
    },

    mounted(){
      // Realizar las solicitudes HTTP para obtener datos
      //Lectura tipo de cultivo
      axios.get('http://localhost:8000/api/tipoCultivo')
      .then(response =>{
        this.tipo_cultivo=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de cultivo
      axios.get('http://localhost:8000/api/cultivo')
      .then(response =>{
        console.log("Cultivos")
        console.log(response.data)
        this.cultivos=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de plantas
      axios.get('http://localhost:8000/api/plantas')
      .then(response =>{
        this.plantas=response.data
        this.initializeMatriz()
      })
      .catch(error =>{
        console.log(error)
      })
      
    },

    methods: {
      // Función para inicializar la matriz con los datos de las plantas
      initializeMatriz() {
        for (let i = 0; i < 8; i++) {
          this.matriz.push(new Array(8).fill(null));
        }

        // Asignar las plantas a la matriz según el número de planta asignado
        this.plantas.forEach(planta => {
          const fila = Math.floor((planta.numeroPlanta - 1) / 8);
          const columna = (planta.numeroPlanta - 1) % 8;
          this.matriz[fila][columna] = planta;  
        }); 
      },

      obtenerContadorPosicion(filaIndex, columnaIndex) {
        // Calcula el contador de posición basado en los índices de fila y columna
        return filaIndex * this.matriz[0].length + columnaIndex + 1;
      },
      // Seleccion de la planta mediante click y despliegue de informacion
      seleccionarPlanta(filaIndex, columnaIndex) {
        this.plantaSeleccionada = { fila: filaIndex, columna: columnaIndex };
        const planta = this.matriz[filaIndex][columnaIndex];
        this.cultivoSeleccionado = planta ? planta.cultivo : null;
      }

    }
    
}

</script>