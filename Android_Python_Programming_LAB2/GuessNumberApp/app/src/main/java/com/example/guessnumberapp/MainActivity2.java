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

    //parameter in guessing game
    int randNum = 0, history = 999;
    int min = 1, max = 50, count = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        //using this pointer to get the bundle from the intent
        //and extract the parameter from the last page
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

        //get a random number from 0 ~ 50
        //Math.random return a number between 0 ~ 0.9999999999999 approach 1
        randNum = (int)(Math.random() * 50 + 1);

        enter.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){

                //assert the user give the non-number input, check if the string isNumber
                String possibleNumber = GuessNumber.getText().toString();
                boolean isNumber = Pattern.matches("[0-9]+", possibleNumber);
                if(!isNumber){
                    hint.setText("請不要輸入數字以外的東西");
                    return;
                }

                //make sure the user give the number as the input,
                //otherwise, Integer.parseInt() will make app crash
                int in = Integer.parseInt(GuessNumber.getText().toString());

                //if the user give a valid input, increase the count
                count++;
                numGuess.setText("猜測次數 : " + count);

                //tune the range for the min and max, and give the corresponding hint
                if(in <= max && in >= min){
                    if(in > randNum){
                        max = in;
                        hint.setText("請輸入"+ min + "~" + max + "的數字");
                    }
                    else if(in < randNum){
                        min = in;
                        hint.setText("請輸入"+ min + "~" + max + "的數字");
                    }

                    //make a correct guess, compare the current count to the best record (history)
                    else if(in == randNum){
                        hint.setText("恭喜猜對");
                        if(count < history){
                            history = count;
                            BestRecord.setText("最佳紀錄 : " + history);
                        }
                    }
                }

                //make sure the user input the range between min ~ max
                else{
                    hint.setText("請輸入"+ min + "~" + max + "的數字，請輸入正常值");
                }
            }
        });

        //reset the guessing number game parameter and reset count
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

        //pass the studentID, name , and best record (history) to the next activity
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