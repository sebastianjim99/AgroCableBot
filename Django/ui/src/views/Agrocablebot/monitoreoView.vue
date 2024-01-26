<template>

    <div class="">
        <navbar_monitoreo />
    </div>
    <!-- Seccion de Trasmision en vivo camas -->
    <div style="width: 100%; height: 100%; position: relative; background: rgba(230, 230, 230, 0.47)">
        <div class="position-relative bg-success-subtle bg-opacity-50 row">
            <div style="width: 100%; height: 100%; text-align: center; color: #FB6542; font-size: 70px; font-family: Questrial; font-weight: 400; word-wrap: break-word">
                Transmisión en vivo
            </div>
            <div style="width: 100%; height: 100%; color: #375E97; font-size: 50px; font-family: Roboto; font-weight: 300; word-wrap: break-word">
                AgroCableBot
            </div>
            <div class="container py-4 py-xl-5">
                <div class="row gy-4 row-cols-1 row-cols-md-2" style="margin-top: -23px;">
                    <div class="col">
                        <div class="card"><img class="card-img-top w-100 d-block fit-cover" style="height: 200px;" src="https://cdn.bootstrapstudio.io/placeholders/1400x800.png" width="634" height="200" />
                            <div class="card-body p-4">
                                <p class="card-text">Cámara Efector final</p>
                            </div>
                        </div>
                    </div>
                    <div class="col" style="padding-left: 46px;padding-right: 58px;">
                        <div class="card"><img class="card-img-top w-100 d-block fit-cover" style="height: 200px;" src="https://cdn.bootstrapstudio.io/placeholders/1400x800.png" width="634" height="200" />
                            <div class="card-body p-4">
                                <p class="card-text">Cámara Efector final</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
                       
        </div>

    </div>

    



    
</template>

<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
export default{
    components:{
        navbar_monitoreo,
    }
}

</script>
