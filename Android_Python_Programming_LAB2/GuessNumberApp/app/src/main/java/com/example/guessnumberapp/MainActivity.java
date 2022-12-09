package com.example.guessnumberapp;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText studentID;
    EditText name;
    Button startButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        studentID = (EditText)findViewById(R.id.studentID);
        name = (EditText)findViewById(R.id.name);
        startButton = (Button)findViewById(R.id.startButton);

        startButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){

                //using intent to switch activity
                Intent intent = new Intent();
                intent.setClass(MainActivity.this, MainActivity2.class);

                //an object to put many variables into
                //and pass those variables to the next page through intent
                Bundle bundle = new Bundle();
                bundle.putString("studentID",studentID.getText().toString());
                bundle.putString("name",name.getText().toString());

                //pass bundle to intent
                intent.putExtras(bundle);
                startActivity(intent);
            }
        });
    }
}
