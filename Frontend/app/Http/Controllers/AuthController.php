<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class AuthController extends Controller
{
    public function indexLogin(){
        return view('login');
    }

    public function indexRegister(){
        return view('register');
    }
}
