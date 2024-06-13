<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\HomeController;



Route::get('/home', [HomeController::class,'index'])->name('login');
Route::get('/login', [AuthController::class,'indexLogin'])->name('login');
Route::post('/login', [AuthController::class,'login']);

Route::get('/register', [AuthController::class,'indexRegister'])->name('register');
Route::post('/register', [AuthController::class,'register']);

Route::post('/task', [HomeController::class,'create'])->name('create');

Route::get('/logout', [AuthController::class,'logout'])->name('logout');