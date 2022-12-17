package com.example.lab3_set;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.NumberPicker;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import org.w3c.dom.Text;

public class timer_fragment extends Fragment {

    View root;
    NumberPicker minutes;
    NumberPicker seconds;
    TextView counter;
    Button begin;
    Button reStart;
    CountDownTimer countdown;
    Boolean flag;       //avoid multi countdown simutaneously


    @Nullable
    @Override
    public View onCreateView(@NonNull @org.jetbrains.annotations.NotNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        root = inflater.inflate(R.layout.timer_fragment, container, false);
        minutes = (NumberPicker) root.findViewById(R.id.minutes);
        minutes.setMinValue(0);
        minutes.setMaxValue(59);

        seconds = (NumberPicker)  root.findViewById(R.id.seconds);
        seconds.setMinValue(0);
        seconds.setMaxValue(59);

        counter = (TextView) root.findViewById(R.id.counter);
        begin = (Button) root.findViewById(R.id.begin);
        reStart = (Button) root.findViewById(R.id.reStart);
        flag = true;

        begin.setOnClickListener(new View.OnClickListener(){
            @Override

            public void onClick(View v){
                if(flag){
                    flag = false;

                    //get the user wanted time duration
                    int m = minutes.getValue();
                    int s = seconds.getValue();

                    //transfer into msec
                    long time_left = (m * 60 + s) * 1000;
                    counter.setText(String.format("%02d:%02d", m, s));

                    countdown = new CountDownTimer(time_left, 1000) {
                        @Override
                        public void onTick(long millisUntilFinished) {
                            int s = (int)(millisUntilFinished/1000);      //ms -> s
                            int m = (int)(s / 60);                        //s -> m
                            s = s - m * 60;
                            counter.setText(String.format("%02d:%02d", m, s));
                        }

                        @Override
                        public void onFinish() {
                            //when countdown finished
                            flag = true;
                            counter.setText("00:00");
                        }
                    }.start();
                }
            }
        });

        reStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int m = minutes.getValue();
                int s = seconds.getValue();
                counter.setText(String.format("%02d:%02d", m, s));
                countdown.cancel();
                flag = true;
            }
        });

        return root;
    }
}

