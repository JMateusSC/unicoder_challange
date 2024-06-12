@extends('layouts.layouts')

@section('content')
 
    
    <main class="main-content w-100 p-5 m-auto">
        <div class="panel panel-default">
            <div class="panel-body">
                @include('common.errors')
            </div>
        </div>
        <button type="button" class="floating-btn" data-bs-toggle="modal" data-bs-target="#ModalAdd" >
            + 
        </button>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h1 class="textPurple textBold text-center">Lista de Tarefas</h1>
            </div>
            <hr class="line">
            <div class="row" >
                <div class="col-md-4 p-2">
                    <h4 class="text-center textTodo">TODO</h4>
                    <div class="m-2 p-3 card-todo">
                        <div class="card p-2">
                            <p class="textCardTitle">Título:</p>
                            <p class="text-center">TESTE</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 p-2">
                    <h4 class="text-center textDoing">DOING</h4>
                    <div class="m-2 p-3 card-doing">
                        <div class="card p-2">
                            <p class="textCardTitle">Título:</p>
                            <p class="text-center">TESTE</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 p-2">
                    <h4 class="text-center textDone">DONE</h4>
                    <div class="m-2 p-3 card-done">
                        <div class="card p-2">
                            <p class="textCardTitle">Título:</p>
                            <p class="text-center">TESTE</p>
                        </div>
                    </div>
                </div>
                
            </div>     
        </div>
        <div class="modal fade" id="ModalAdd" tabindex="-1" aria-labelledby="AddModal" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <!-- Header -->
                    <div class="modal-header pb-0">
                        <h3 id="restrictionAddModalTitle" class="modal-title">Nova Tarefa</h3>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <!-- Body -->
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="AddTitle" class="form-label">TíTulo:</label>
                            <input type="text" class="form-control time" id="AddTitle" placeholder="Insira o Título" name="time">
                        </div>

                        <div class="mb-3">
                            <div class="row">
                                <div class="col-lg">
                                    <label for="restrictionAddDate" class="form-label">Data Limite: </label>
                                    <input type="date" class="form-control addDate" id="restrictionaddDate" name="addDate">
                                    <div class="invalid-feedback">Insira a data limite</div>
                                </div>
                                </span>
                                <div class="col-lg">
                                    <label for="expectedTime" class="form-label">Tempo Esperado:</label>
                                    <input type="text" class="form-control time" id="expectedTime" placeholder="Insira o Tempo Esperado" name="time">
                                <div class="invalid-feedback">Insira o Tempo Esperado</div>
                            </div>
                        </div>
                            
                        </div>                    
                        <div class="mb-3">
                            <label for="restrictionAddDescriptions" class="form-label">Descrição</label>
                            <textarea class="form-control addObs" id="restrictionAddDescriptions" placeholder="Observações/detalhes da tarefa" rows="5" name="addObs"></textarea>
                        </div>
                    </div>
                    <div class="modal-footer pt-0">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Cancelar</button>
                        <button type="button" class="btn btn-primary light add_restriction" id="btnSaveEvent">Salvar</button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <div class="modal fade" id="restrictionAddModal" tabindex="-1" role="dialog" aria-labelledby="restrictionAddModalTitle" aria-hidden="true">
        
    </div>
@endsection