package com.example.app0811562;

import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {

    //variable declaration
    TextView showtext;
    Button demobutton;
    Button backbutton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //connect the object by ID
        showtext = (TextView)findViewById(R.id.showtext);
        demobutton = (Button)findViewById(R.id.demobutton);
        backbutton = (Button)findViewById(R.id.backbutton);


        //demo button: increase text size and show "Pass"
        demobutton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                int size = (int)showtext.getTextSize();
                size = size + 3;
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size);
                showtext.setText("Pass");
            }
        });


        //back button: decrease text size and show "Android Lab1 demo"
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