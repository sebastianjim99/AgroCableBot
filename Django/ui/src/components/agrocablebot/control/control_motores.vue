<template>
        
        <div class="col-md-9 col-xl-8 text-center mx-auto">
            <h2 class="divider-style">
                <span> Control de motores individualmente  
                <button class="btn btn-primary" @click="createConnection"> Conectarse </button>
                </span>
            </h2>
        </div>
        <div class="container">
        <div class="row row-cols-2">

            <div class="col content-motor" style="max-width: 600px;">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorA" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>

                    <span class="d-inline" style="vertical-align: middle;">Motor A</span>

                    <svg @click="Recoger_motorA" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>

                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorA">
                </p>
            </div>

            <div class="col content-motor" style="max-width: 600px;">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorB" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>

                    <span class="d-inline" style="vertical-align: middle;">Motor B</span>

                    <svg @click="Recoger_motorB" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>

                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorB">
                </p>
            </div>
            <div class="col content-motor" style="max-width: 600px;">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorC" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>

                    <span class="d-inline" style="vertical-align: middle;">Motor C</span>

                    <svg @click="Recoger_motorC" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>

                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorC">
                </p>
            </div>
            <div class="col content-motor" style="max-width: 600px;">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorD" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>

                    <span class="d-inline" style="vertical-align: middle;">Motor D</span>

                    <svg @click="Recoger_motorD" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>

                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorD">
                </p>
            </div>
        </div>
    </div>



</template>

<script>
import mqtt from 'mqtt';
import Swal from 'sweetalert2';

export default {

    data(){
        return{
            pasos_motorA: 10,
            pasos_motorB: 10,
            pasos_motorC: 10,
            pasos_motorD: 10,

            connection: {
                protocol: "ws",
                host: '172.17.91.30' ,               //"imacunamqtt.live",
                // ws: 8083; wss: 8084
                port: 8083,
                endpoint: "/mqtt",
                clean: true,
                connectTimeout: 30 * 1000, // ms
                reconnectPeriod: 4000, // ms
                clientId: "emqx_vue_" + Math.random().toString(16).substring(2, 8),
                username: "imacuna",
                password: "pi",
            },
        }
    },

    methods: {
        
        createConnection() {
            try {
                this.connecting = true;
                const { protocol, host, port, endpoint, ...options } = this.connection;
                const connectUrl = `${protocol}://${host}:${port}${endpoint}`;
                this.client = mqtt.connect(connectUrl, options);
                if (this.client.on) {
                    this.client.on("connect", () => {
                        this.connecting = false;
                        console.log("Connection succeeded!");
                        Swal.fire({
                            icon: 'success',
                            title: '¡Éxito!',
                            text:  'Conexión exitosa con el servidor mqtt',
                        });
                    });
                    this.client.on("reconnect", this.handleOnReConnect);
                    this.client.on("error", (error) => {
                        console.log("Connection failed", error);
                    });
                }
            } catch (error) {
                this.connecting = false;
                console.log("mqtt.connect error", error);
            }
        },

        handleOnReConnect() {
            this.retryTimes += 1;
            if (this.retryTimes > 5) {
                try {
                    this.client.end();
                    this.initData();
                    this.$message.error("Limite de reconexiones");
                } catch (error) {
                    this.$message.error(error.toString());
                }
            }
        },

        Recoger_motorA(){
            const mensaje = `{ "GCODE": "G10 A${this.pasos_motorA}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                console.log(mensaje)
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorA(){
            const mensaje = `{ "GCODE": "G10 A-${this.pasos_motorA}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Recoger_motorB(){
            const mensaje = `{ "GCODE": "G10 B${this.pasos_motorB}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorB(){
            const mensaje = `{ "GCODE": "G10 B-${this.pasos_motorB}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Recoger_motorC(){
            const mensaje = `{ "GCODE": "G10 C${this.pasos_motorC}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorC(){
            const mensaje = `{ "GCODE": "G10 C-${this.pasos_motorC}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Recoger_motorD(){
            const mensaje = `{ "GCODE": "G10 D${this.pasos_motorD}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorD(){
            const mensaje = `{ "GCODE": "G10 D-${this.pasos_motorD}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },

    }

}
</script>

<style>
.content-motor{
    justify-content: center;
}
.text-motor{
    width: 100%;
    justify-content: center ;
    align-content: center;
    font-size: 22px;
}
</style>