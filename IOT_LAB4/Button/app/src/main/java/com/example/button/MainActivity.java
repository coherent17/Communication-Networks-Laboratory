package com.example.button;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button_up = (Button)findViewById(R.id.up);
        Button button_down = (Button)findViewById(R.id.down);
        Button button_left = (Button)findViewById(R.id.left);
        Button button_right = (Button)findViewById(R.id.right);
        Button button_stop = (Button)findViewById(R.id.stop);


        button_up.setOnClickListener(new Button.OnClickListener(){

            @Override

            public void onClick(View v) {
                System.out.println("up");
                new SendData().execute("w");

            }

        });

        button_down.setOnClickListener(new Button.OnClickListener(){

            @Override

            public void onClick(View v) {
                System.out.println("down");
                new SendData().execute("x");

            }

        });

        button_left.setOnClickListener(new Button.OnClickListener(){

            @Override

            public void onClick(View v) {
                System.out.println("left");
                new SendData().execute("a");

            }

        });

        button_right.setOnClickListener(new Button.OnClickListener(){

            @Override

            public void onClick(View v) {
                System.out.println("right");
                new SendData().execute("d");

            }

        });

        button_stop.setOnClickListener(new Button.OnClickListener(){

            @Override

            public void onClick(View v) {
                System.out.println("stop");
                new SendData().execute("s");

            }

        });
    }
}