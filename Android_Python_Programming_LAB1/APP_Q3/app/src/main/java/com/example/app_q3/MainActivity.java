package com.example.app_q3;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    //variable declaration
    TextView TopText;
    Button setbutton;
    Button resetbutton;
    EditText Name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //connect object by ID
        TopText = (TextView)findViewById(R.id.TopText);
        setbutton = (Button)findViewById(R.id.setbutton);
        resetbutton = (Button)findViewById(R.id.resetbutton);
        Name = (EditText)findViewById(R.id.Name);


        //set button: show the "Welcome to Android" with the string on EditText
        setbutton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                TopText.setText("Welcome to Android, "+ Name.getText().toString());
            }
        });

        //reset button: reset the string in TopText to "Hello World"
        resetbutton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                TopText.setText("Hello World");
            }
        });

    }
}