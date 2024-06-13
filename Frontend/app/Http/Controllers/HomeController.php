<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Cookie;
use Illuminate\Support\Facades\Http;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function index(){
        $token = Session::get('auth_token', Cookie::get('auth_token'));

        $apiUrl = 'http://127.0.0.1:8000/api/tasks/get_all';
        $response = Http::withToken($token)->get($apiUrl);

        if ($response->successful()) {
            $data = $response->json();
            return view('home', compact('data'));
        } else {
            $errors = ['invalid' => 'Erro desconhecido.'];
            return redirect('login')->withInput()->withErrors($errors);
        }
    }
    public function create (Request $request){
        $token = Session::get('auth_token', Cookie::get('auth_token'));

        $data = [
            'status' => 'TODO',
            'title' => $request->title,
            'description'=> $request->addObs,
            'dead_line'=> $request->addDate,
            'expected_time'=> $request->time,
            'registered_time'=>0
        ];

        $apiUrl = 'http://127.0.0.1:8000/api/tasks/create';
        $response = Http::withToken($token)->post($apiUrl, $data);
        if ($response->successful()) {
            return redirect('home');
        } else {
            $errors = ['invalid' => 'Erro desconhecido.'];
            return redirect('login')->withInput()->withErrors($errors);
        }
    }
}
