<template>


    <section>
    <div class="container text-center py-4 py-xl-5">
        <div class="row mb-5">
            <div class="col">
                <h2>Resumen del calendario</h2>
            </div>
            <div class="col-md-8 col-xl-6 text-center mx-auto">
                <p class="w-lg-50"></p>
            </div>
        </div>
        <div class="row gy-4 row-cols-1 row-cols-md-2">
            <div class="col-xxl-4" style="display: flex;margin-bottom: 20px;">
                <div class="d-flex flex-column flex-lg-row">
                    <div class="w-100"><img class="rounded img-fluid d-block w-100 fit-cover" style="height: 100px;width: 100px;" src="@/assets/iconos/reigo.png" width="257" height="200" /></div>
                    <div class="py-4 py-lg-0 px-lg-4">
                        <h4>UltimoRiego:</h4>
                        <p>10/102023</p>
                    </div>
                </div>
            </div>
            <div class="col-xxl-4" style="display: flex;">
                <div class="d-flex flex-column flex-lg-row">
                    <div><img style="height: 100px;width: 100px;overflow: visible;display: block;position: static;" src="@/assets/iconos/presion.png" width="257" height="200" /></div>
                    <div class="py-4 py-lg-0 px-lg-4" style="width: auto;">
                        <h4 style="width: auto;">Ultimo censado de presión</h4>
                        <p>10/102023</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row gy-4 row-cols-1 row-cols-md-2">
            <div class="col-xxl-4" style="display: flex;">
                <div class="d-flex flex-column flex-lg-row">
                    <div><img style="height: 100px;width: 100px;overflow: visible;display: block;position: static;" src="@/assets/iconos/temperatura.png" width="257" height="200" /></div>
                    <div class="py-4 py-lg-0 px-lg-4" style="width: auto;">
                        <h4 style="width: auto;">Ultimo censado de Temperatura</h4>
                        <p>10/102023</p>
                    </div>
                </div>
            </div>
            <div class="col-xxl-4" style="display: flex;">
                <div class="d-flex flex-column flex-lg-row">
                    <div><img style="height: 100px;width: 100px;overflow: visible;display: block;position: static;" src="@/assets/iconos/humedad.png" width="257" height="200" /></div>
                    <div class="py-4 py-lg-0 px-lg-4" style="width: auto;">
                        <h4 style="width: auto;">Ultimo censado de humedad</h4>
                        <p>10/102023</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </section>

</template>

<script>
export default {

    name: "Calendar_resum",
}
</script>