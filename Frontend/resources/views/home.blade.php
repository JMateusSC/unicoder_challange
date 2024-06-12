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
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="AddModal">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
                </div>
            </div>
        </div>
    </main>
@endsection