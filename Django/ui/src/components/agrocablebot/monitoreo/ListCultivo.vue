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
                            <th>Id</th>
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
                        <tr>
                            <td>01</td>
                            <td>Lechuga</td>
                            <td>Dec 1, 2021</td>
                            <td>Felipe Betancourth</td>
                            <td>21</td>
                            <td>Dec 1, 2022</td>
                            <td>A tiempo</td>
                            <td><button class="btn btn-danger" type="button"><i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i></button><button class="btn btn-warning" type="button"><i class="fas fa-pencil-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i></button></td>
                        </tr>
                        <tr>
                            <td>02</td>
                            <td>Cilantro</td>
                            <td>Nov 15, 2021</td>
                            <td>Andres Juan</td>
                            <td>21</td>
                            <td>Dec 1, 2022</td>
                            <td>Lista para cosechar</td>
                            <td><button class="btn btn-danger" type="button"><i class="far fa-trash-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i></button><button class="btn btn-warning" type="button"><i class="fas fa-pencil-alt d-xl-flex justify-content-xl-center align-items-xl-center"></i></button></td>
                        </tr>
                        <tr>
                            <td>03</td>
                            <td>Albahaca</td>
                            <td>Nov 02, 2021</td>
                            <td>Sebasstian Jimenez</td>
                            <td>21</td>
                            <td>Dec 1, 2022</td>
                            <td>pronto para cosechar</td>
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
export default {
    
}
</script>