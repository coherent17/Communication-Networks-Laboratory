package com.example.guessnumberapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.regex.Pattern;

public class MainActivity2 extends AppCompatActivity {

    EditText GuessNumber;
    Button enter;
    TextView hint;
    TextView numGuess;
    TextView BestRecord;
    Button restartButton;
    Button endButton;

    int randNum = 0, history = 999;
    int min = 1, max = 50, count = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        Bundle bundle = this.getIntent().getExtras();
        String studentID = (String)bundle.getString("studentID");
        String name = (String)bundle.getString("name");

        GuessNumber = (EditText)findViewById(R.id.GuessNumber);
        enter = (Button)findViewById(R.id.enter);
        hint = (TextView)findViewById(R.id.hint);
        numGuess = (TextView)findViewById(R.id.numGuess);
        BestRecord = (TextView)findViewById(R.id.BestRecord);
        restartButton = (Button)findViewById(R.id.restartButton);
        endButton = (Button)findViewById(R.id.endButton);

        randNum = (int)(Math.random() * 50 + 1);

        enter.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                String possibleNumber = GuessNumber.getText().toString();
                boolean isNumber = Pattern.matches("[0-9]+", possibleNumber);
                if(!isNumber){
                    hint.setText("請不要輸入數字以外的東西");
                    return;
                }
                int in = Integer.parseInt(GuessNumber.getText().toString());

                count++;
                numGuess.setText("猜測次數 : " + count);

                if(in <= max && in >= min){
                    if(in > randNum){
                        max = in;
                        hint.setText("請輸入"+ min + "~" + max + "的數字");
                    }
                    else if(in < randNum){
                        min = in;
                        hint.setText("請輸入"+ min + "~" + max + "的數字");
                    }
                    else if(in == randNum){
                        hint.setText("恭喜猜對");
                        if(count < history){
                            history = count;
                            BestRecord.setText("最佳紀錄 : " + history);
                        }
                    }
                }
                else{
                    hint.setText("請輸入"+ min + "~" + max + "的數字，請輸入正常值");
                }
            }
        });

        restartButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                randNum = (int)(Math.random() * 50 + 1);
                min = 0;
                max = 50;
                count = 0;
                hint.setText("請輸入"+ min + "~" + max + "的數字");
                numGuess.setText("猜測次數 : " + count);
            }
        });

        endButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent intent = new Intent();
                intent.setClass(MainActivity2.this, MainActivity3.class);
                Bundle bundle = new Bundle();
                bundle.putString("studentID",studentID);
                bundle.putString("name",name);
                bundle.putInt("history", history);
                intent.putExtras(bundle);
                startActivity(intent);
            }
        });

    }
}