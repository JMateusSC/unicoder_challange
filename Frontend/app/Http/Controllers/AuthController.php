<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Cookie;
use Illuminate\Support\Facades\Http;

class AuthController extends Controller
{
    public function indexLogin(){
        return view('login');
    }

    public function indexRegister(){
        return view('register');
    }

    public function login(Request $request){   
        $remember = $request->input('remember');
        $remember = $remember ? true : false;

        
        $data = [
            'email' => $request->email,
            'password' => $request->password,
        ];
        
        $apiUrl = 'http://127.0.0.1:8000/api/user/login';

        $response = Http::post($apiUrl, $data);

        if ($response->successful()) {
            $tokenData = $response->json();
            $tokenId = $tokenData['access_token'];

            if ($request->remember) {
                Cookie::queue('auth_token', $tokenId, 60 * 24); 
            } else {
                Session::put('auth_token', $tokenId);
            }
            return redirect('home');
        } else {
            $errors = ['invalid' => 'Email ou senha inválidos.'];
            return redirect('login')->withInput()->withErrors($errors);
        }
    }


    public function register(Request $request){   
       
        $data = [
            'username' => $request->username,
            'email' => $request->email,
            'password' => $request->password,
        ];
        
        $apiUrl = 'http://127.0.0.1:8000/api/user/register';

        $response = Http::post($apiUrl, $data);
        if ($response->successful()) {
            return redirect('login');
        } else {
            $errors = ['invalid' => 'Erro desconhecido.'];
            return redirect('register')->withInput()->withErrors($errors);
        }
    }
}
