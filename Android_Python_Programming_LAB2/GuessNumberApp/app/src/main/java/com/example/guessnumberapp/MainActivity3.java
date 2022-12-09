package com.example.guessnumberapp;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity3 extends AppCompatActivity {

    TextView studentID;
    TextView name;
    TextView history;
    Button BackButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        studentID = (TextView)findViewById(R.id.studentID);
        name = (TextView)findViewById(R.id.name);
        history = (TextView)findViewById(R.id.history);
        BackButton = (Button)findViewById(R.id.BackButton);

        //extract the data from last 2 activity
        Bundle bundle = this.getIntent().getExtras();
        String studentIDTEXT = (String)bundle.getString("studentID");
        String nameTEXT = (String)bundle.getString("name");
        int historyTEXT = (int)bundle.getInt("history");

        //show the data
        studentID.setText("學號:         " + studentIDTEXT);
        name.setText("姓名:         " + nameTEXT);
        history.setText("最佳紀錄:         " + historyTEXT);

        //go back to the main activity
        BackButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent intent = new Intent();
                intent.setClass(MainActivity3.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}