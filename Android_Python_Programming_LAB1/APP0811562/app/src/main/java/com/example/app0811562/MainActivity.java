package com.example.app0811562;

import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {
    TextView showtext;
    Button demobutton;
    Button backbutton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        showtext = (TextView)findViewById(R.id.showtext);
        demobutton = (Button)findViewById(R.id.demobutton);
        backbutton = (Button)findViewById(R.id.backbutton);
        demobutton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                int size = (int)showtext.getTextSize();
                size = size + 3;
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size);
                showtext.setText("Pass");
            }
        });



        backbutton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                int size = (int)showtext.getTextSize();
                size = size - 3;
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size);
                showtext.setText("Android Lab1 demo");
            }
        });
    }
}