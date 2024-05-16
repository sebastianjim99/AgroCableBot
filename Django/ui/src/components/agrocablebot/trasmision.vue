<template>
    <!-- Seccion de Trasmision en vivo camas -->
    <div class="live-stream-section">
        <div class="container py-4 py-xl-5">
            <div class="text-center mb-5">
                <h1 class="divider-style">
                    <span style="font-family: Questrial; font-weight: 400; font-size: 50px; color: #FB6542;" > 
                        Transmisión en vivo             
                    </span>
                </h1>
                <h2 class="text-primary mb-5" style="font-family: Roboto; font-weight: 300; font-size: 25px;">AgroCableBot</h2>
            </div>
            <div class="row gy-4" >
                <div class=" col h-100 d-flex justify-content-center align-items-center"  >
                    <div class="card ">
                        <img class="card-img-top" :src="videoStreamUrl" alt="Cámara Posicion">
                        <div class="card-body text-center">
                            <p class="card-text">Cámara Posicion</p>
                            <a class="btn btn-primary"  type="submit" @click="captureImage(videoStreamUrl)">Capturar</a>
                            <p v-if="imageUrl" class="mt-3"><a :href="imageUrl" download="captura.png">Haz clic aquí</a> para descargar la imagen</p>
                        </div>
                    </div>
                </div>
                <div class="col h-100 d-flex justify-content-center align-items-center ">
                    <div class="card ">
                        <img class="card-img-top" :src="videoStreamUrl2" alt="Cámara Efector final">
                        <div class="card-body text-center">
                            <p class="card-text">Cámara Efector final</p>
                            <a class="btn btn-primary" type="submit" @click="captureImage(videoStreamUrl2)">Capturar</a>
                            <p v-if="imageUrl" class="mt-3"><a :href="imageUrl" download="captura.png">Haz clic aquí</a> para descargar la imagen</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {

    name:"trasmisionVue", 

    data(){
        return {
            'api' : `${process.env.VUE_APP_API_URL}`,
            videoStreamUrl:  'http://semillero.imacunamqtt.live:7001/aboveCam/',
            videoStreamUrl2: 'http://172.17.91.30:7002/belowCam/',
            imageUrl: ''
        };
    },
    mounted(){
        console.log('DOM rendered')
        setInterval(() => {
        this.updateStreamUrl();
        }, 1000); 
    },
    

    methods: {
        updateStreamUrl() {
        // Agregar un timestamp a la URL para evitar el almacenamiento en caché
        this.videoStreamUrl = '//imacunamqtt.live:7001/aboveCam/';
        this.videoStreamUrl2 ='//imacunamqtt.live:7001/belowCam/';
        },

        captureImage(imageUrl) {
            console.log("Capturando imagen");

            // Crear un nuevo objeto de imagen
            const image = new Image();
            image.crossOrigin = 'anonymous';
            image.src = imageUrl;

            // Esperar a que la imagen se cargue
            image.onload = () => {
                console.log("Imagen cargada");

                // Crear un canvas para dibujar la imagen
                const canvas = document.createElement('canvas');
                canvas.width = image.width;
                canvas.height = image.height;

                // Dibujar la imagen en el canvas
                const context = canvas.getContext('2d');
                context.drawImage(image, 0, 0);

                // Obtener la URL de la imagen del canvas
                const capturedImageUrl = canvas.toDataURL('image/png');
                // Guardar la imagen automáticamente
                this.saveImage(capturedImageUrl);
            };
        },

        // Método para guardar la imagen automáticamente
        saveImage(imageUrl) {
            // Crear un enlace temporal para descargar la imagen
            const link = document.createElement('a');
            link.href = imageUrl;
            link.download = 'captura.png'; // Nombre del archivo a descargar
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
        
    }
}
</script>