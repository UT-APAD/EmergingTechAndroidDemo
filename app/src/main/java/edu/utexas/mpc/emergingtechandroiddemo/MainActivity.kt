package edu.utexas.mpc.emergingtechandroiddemo

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Button
import android.widget.TextView
import com.android.volley.RequestQueue
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.google.gson.Gson

class MainActivity : AppCompatActivity() {

    lateinit var textView: TextView
    lateinit var button: Button
    lateinit var queue: RequestQueue
    lateinit var gson: Gson

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        textView = this.findViewById(R.id.text)
        button = this.findViewById(R.id.button)
        button.setOnClickListener({ requestWeather() })
        queue = Volley.newRequestQueue(this)
        gson = Gson()
    }

    fun requestWeather(){
        val url = StringBuilder("https://api.openweathermap.org/data/2.5/weather?id=4254010&appid=fb0819e6aee758f949628649626be70d").toString()
        val stringRequest = object : StringRequest(com.android.volley.Request.Method.GET, url,
                com.android.volley.Response.Listener<String> { response ->
                    //textView.text = response
                    val weatherResult = gson.fromJson(response, WeatherResult::class.java)
                    textView.text = weatherResult.weather.get(0).description
                },
                com.android.volley.Response.ErrorListener { println("******That didn't work!") }) {}
        // Add the request to the RequestQueue.
        queue.add(stringRequest)
    }
}

class WeatherResult(val id: Int, val name: String, val cod: Int, val coord: Coordinates, val main: WeatherMain, val weather: Array<Weather>)
class Coordinates(val lon: Double, val lat: Double)
class Weather(val id: Int, val main: String, val description: String, val icon: String)
class WeatherMain(val temp: Double, val pressure: Int, val humidity: Int, val temp_min: Double, val temp_max: Double)
